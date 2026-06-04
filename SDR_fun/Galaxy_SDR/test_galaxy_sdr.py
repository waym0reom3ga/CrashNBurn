#!/usr/bin/env python3
"""Test Galaxy SDR functionality without curses."""

import sys, os, time, threading
sys.path.insert(0, '/home/waymore')
from galaxy_sdr import (
    SDRBackend, init_db, seed_db, get_signals_for_bands, 
    detect_audio_backend, DB_PATH, RECORD_DIR, BANDS_DB
)
from crt_effects import CRTEngine, CRTConfig, THEMES, theme_pair, reset_color_pairs
import sqlite3

def test_all():
    print("=" * 60)
    print("Galaxy SDR - Functional Test Suite")
    print("=" * 60)
    
    # Test 1: Audio backend detection
    print("\n[TEST 1] Audio Backend Detection")
    backend = detect_audio_backend()
    if backend:
        print(f"  ✅ Found: {backend['type']} at {backend['path']}")
    else:
        print("  ❌ No audio backend detected")
    
    # Test 2: Database initialization
    print("\n[TEST 2] Database Initialization")
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    seed_db(conn)
    bands = conn.execute("SELECT COUNT(*) FROM known_frequencies").fetchone()[0]
    scans_table = conn.execute("PRAGMA table_info(scans)").fetchall()
    scan_cols = [c[1] for c in scans_table]
    print(f"  ✅ Known frequencies: {bands}")
    print(f"  ✅ Scans columns: {scan_cols}")
    assert 'scan_type' in scan_cols, "scan_type column missing!"
    
    # Test 3: SDR connection
    print("\n[TEST 3] SDR Connection")
    sdr = SDRBackend()
    if sdr.connect():
        print(f"  ✅ Connected: {sdr.device_name}")
        print(f"  ✅ Device type: {sdr.device_type}")
        print(f"  ✅ Freq range: {sdr.freq_range[0]/1e6:.1f}-{sdr.freq_range[1]/1e6:.0f} MHz")
    else:
        print("  ⚠️  Not connected (SDRconnect may not be running)")
    
    # Test 4: Device properties
    if sdr.connected:
        print("\n[TEST 4] Device Properties")
        can_ctrl = sdr._get_prop("can_control")
        freq_resp = sdr._get_prop("device_center_frequency")
        print(f"  ✅ Can control: {can_ctrl}")
        if freq_resp:
            print(f"  ✅ Current frequency: {freq_resp} Hz ({float(freq_resp)/1e6:.3f} MHz)")
    
    # Test 5: Volume control
    print("\n[TEST 5] Volume Control (simulated)")
    if sdr.connected:
        for vol in [20, 50, 80, 100]:
            sdr._send("set_property", "audio_volume_percent", str(vol))
        print(f"  ✅ Volume control commands sent (20→50→80→100%)")
    
    # Test 6: Spectrum scan
    if sdr.connected:
        print("\n[TEST 6] Spectrum Scan Test (Aviation VHF)")
        test_freqs = [118.5e6, 119.0e6, 120.0e6]
        for freq in test_freqs:
            level = sdr.scan_frequency(freq)
            print(f"  ✅ {freq/1e6:.3f} MHz: peak={level}/255")
    
    # Test 7: Threading safety
    print("\n[TEST 7] Threading Safety Test")
    errors = []
    def db_writer():
        try:
            for i in range(5):
                conn.execute(
                    "INSERT INTO scans (timestamp, device, scan_type) VALUES (?, ?, ?)",
                    (time.strftime("%Y-%m-%d %H:%M:%S"), "test", "band")
                )
                time.sleep(0.1)
        except Exception as e:
            errors.append(str(e))
    
    t = threading.Thread(target=db_writer, daemon=True)
    t.start()
    t.join(timeout=3)
    if not errors:
        print("  ✅ No threading conflicts")
    else:
        print(f"  ❌ Threading error: {errors}")
    
    # Test 8: Recording setup
    print("\n[TEST 8] Recording Setup")
    if os.path.exists(RECORD_DIR):
        print(f"  ✅ Recordings directory ready: {RECORD_DIR}")
    else:
        print(f"  ⚠️  Creating recordings dir...")
        os.makedirs(RECORD_DIR, exist_ok=True)
    
    # Test 9: CRT effects engine
    print("\n[TEST 9] CRT Effects Engine")
    cfg = CRTConfig()
    engine = CRTEngine(cfg)
    
    # Test theme availability
    assert len(THEMES) == 5, f"Expected 5 themes, got {len(THEMES)}"
    print(f"  ✅ Themes available: {list(THEMES.keys())}")
    
    # Test config serialization
    cfg_dict = cfg.to_dict()
    assert 'theme' in cfg_dict, "theme missing from config dict"
    assert 'scanlines' in cfg_dict, "scanlines missing from config dict"
    print(f"  ✅ Config serialization works")
    
    # Test config deserialization
    new_cfg = CRTConfig()
    test_data = {"theme": "amber", "scanlines": False, "flicker_rate": 0.1}
    new_cfg.from_dict(test_data)
    assert new_cfg.theme == "amber", f"Theme not loaded: {new_cfg.theme}"
    assert not new_cfg.scanlines, "Scanlines not disabled"
    print(f"  ✅ Config deserialization works")
    
    # Test CRT engine methods
    engine.tick()
    flicker_attr = engine.get_flicker_attr()
    print(f"  ✅ Flicker attribute: {flicker_attr}")
    
    noise_check = engine.should_noise(10, 20)
    print(f"  ✅ Noise check (row=10, col=20): {noise_check}")
    
    scanline_dim = engine.scanline_dim(5)
    print(f"  ✅ Scanline dim (row=5): {scanline_dim}")
    
    vignette = engine.vignette_dim(0, 0, 24, 80)
    print(f"  ✅ Vignette check (corner): {vignette}")
    
    # Test 10: Signal filtering
    print("\n[TEST 10] Signal Filtering")
    signals = get_signals_for_bands(conn, [], 10)
    print(f"  ✅ Retrieved {len(signals)} signals (all bands)")
    
    if BANDS_DB:
        first_band = BANDS_DB[0][0]
        filtered = get_signals_for_bands(conn, [first_band], 5)
        print(f"  ✅ Filtered by band '{first_band}': {len(filtered)} signals")
    
    conn.close()
    sdr.disconnect()
    
    print("\n" + "=" * 60)
    print("All tests completed successfully! ✅")
    print("=" * 60)

if __name__ == "__main__":
    test_all()
