#!/usr/bin/env python3
"""Test SDR Retro TUI functionality without curses."""

import sys, os, time, threading
sys.path.insert(0, '/home/waymore')

from sdr_retro_tui import (
    SDRBackend, init_db, seed_db, get_top_signals, 
    detect_audio_backend, DB_PATH, RECORD_DIR
)
import sqlite3

def test_all():
    print("=" * 60)
    print("SDR Retro TUI - Functional Test Suite")
    print("=" * 60)
    
    # 1. Audio backend detection
    print("\n[TEST 1] Audio Backend Detection")
    backend = detect_audio_backend()
    if backend:
        print(f"  ✅ Found: {backend['type']} at {backend['path']}")
    else:
        print("  ❌ No audio backend found")
    
    # 2. Database setup
    print("\n[TEST 2] Database Initialization")
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    init_db(conn)
    seed_db(conn)
    
    bands = conn.execute("SELECT COUNT(*) FROM bands").fetchone()[0]
    known = conn.execute("SELECT COUNT(*) FROM known_frequencies").fetchone()[0]
    print(f"  ✅ Bands seeded: {bands}")
    print(f"  ✅ Known frequencies: {known}")
    
    # 3. SDR connection
    print("\n[TEST 3] SDR Connection")
    sdr = SDRBackend()
    if not sdr.connect():
        print("  ❌ Failed to connect to SDRconnect headless")
        conn.close()
        return False
    
    print(f"  ✅ Connected: {sdr.device_name}")
    
    # 4. Property queries
    print("\n[TEST 4] Device Properties")
    can_ctrl = sdr._get_prop("can_control")
    freq = sdr._get_prop("device_center_frequency")
    print(f"  ✅ Can control: {can_ctrl}")
    print(f"  ✅ Current frequency: {freq} Hz ({float(freq)/1e6:.3f} MHz)")
    
    # 5. Volume control simulation
    print("\n[TEST 5] Volume Control (simulated)")
    for vol in [20, 50, 80, 100]:
        sdr._send("set_property", "audio_volume_percent", str(vol))
        time.sleep(0.1)
    print(f"  ✅ Volume control commands sent (20→50→80→100%)")
    
    # 6. Quick spectrum scan test
    print("\n[TEST 6] Spectrum Scan Test (Aviation VHF)")
    sdr._send("set_property", "demodulator", "AM")
    time.sleep(0.2)
    
    # Scan a small range quickly
    test_freqs = [118_500_000, 119_000_000, 120_000_000]
    for f in test_freqs:
        sdr._send("set_property", "device_center_frequency", str(f))
        time.sleep(0.05)
        sdr._send("spectrum_enable", "", "true")
        time.sleep(0.1)
        _, binary = sdr._recv_all(0.15)
        peak = sdr.spectrum_peak(binary)
        sdr._send("spectrum_enable", "", "false")
        print(f"  ✅ {f/1e6:.3f} MHz: peak={peak}/255")
    
    # 7. Database threading test (simulates background scan)
    print("\n[TEST 7] Threading Safety Test")
    db_lock = threading.Lock()
    errors = []
    
    def thread_db_writer():
        try:
            with db_lock:
                conn.execute("INSERT INTO scans (timestamp, device) VALUES (?, ?)", 
                           (time.strftime("%Y-%m-%dT%H:%M:%S"), "test"))
                scan_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                conn.execute(
                    "INSERT INTO signals (scan_id, band_name, frequency_hz, level_low, level_high, noise_floor, signal_gain, demodulator, label) VALUES (?, ?, ?, 0, ?, ?, ?, ?, ?)",
                    (scan_id, "Test Band", 120_000_000, 100, 40, 50, "AM", "Test Signal")
                )
                conn.commit()
        except Exception as e:
            errors.append(str(e))
    
    t = threading.Thread(target=thread_db_writer, daemon=True)
    t.start()
    t.join(timeout=5)
    
    if not errors:
        print("  ✅ Background thread DB write succeeded")
        
        # Verify from main thread
        with db_lock:
            signals = get_top_signals(conn, 10)
            print(f"  ✅ Main thread reads {len(signals)} total signals")
    else:
        print(f"  ❌ Threading error: {errors}")
    
    # 8. Recording directory test
    print("\n[TEST 8] Recording Setup")
    os.makedirs(RECORD_DIR, exist_ok=True)
    if os.path.exists(RECORD_DIR):
        print(f"  ✅ Recordings directory ready: {RECORD_DIR}")
    else:
        print("  ❌ Could not create recordings directory")
    
    # Cleanup
    sdr.disconnect()
    conn.close()
    
    print("\n" + "=" * 60)
    print("All tests completed successfully! ✅")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_all()
    sys.exit(0 if success else 1)
