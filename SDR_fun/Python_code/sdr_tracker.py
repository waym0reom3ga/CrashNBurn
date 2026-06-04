#!/usr/bin/env python3
"""SDR Signal Tracker v2 - Smart detection using dual-gain comparison."""

import json
import struct
import time
import sqlite3
import sys
from datetime import datetime

import websocket

WS = "ws://127.0.0.1:5555"
DB_PATH = "/home/waymore/sdr_signals_v2.db"

def init_db(conn):
    """Create database tables."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            device TEXT,
            notes TEXT DEFAULT ''
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            freq_start_hz INTEGER NOT NULL,
            freq_end_hz INTEGER NOT NULL,
            step_hz INTEGER NOT NULL DEFAULT 100000,
            demodulator TEXT NOT NULL DEFAULT 'AM',
            lna_low INTEGER NOT NULL DEFAULT 2,
            lna_high INTEGER NOT NULL DEFAULT 9
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER NOT NULL REFERENCES scans(id),
            band_name TEXT NOT NULL,
            frequency_hz INTEGER NOT NULL,
            level_low INTEGER NOT NULL,
            level_high INTEGER NOT NULL,
            noise_floor INTEGER NOT NULL,
            signal_gain INTEGER NOT NULL,
            demodulator TEXT NOT NULL,
            label TEXT DEFAULT '',
            UNIQUE(scan_id, frequency_hz)
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS known_frequencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frequency_hz INTEGER UNIQUE NOT NULL,
            description TEXT NOT NULL,
            band_hint TEXT DEFAULT ''
        )
    """)
    
    # Indexes
    conn.execute("CREATE INDEX IF NOT EXISTS idx_signals_freq ON signals(frequency_hz)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_signals_scan ON signals(scan_id)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_scans_time ON scans(timestamp)")

def seed_known_frequencies(conn):
    KNOWN = [
        (121_500_000, "Aviation Emergency (Guard)", "aviation"),
        (122_650_000, "Flight Service Station", "aviation"),
        (156_800_000, "Marine Ch 16 - Distress/Safety", "marine"),
        (156_300_000, "Marine Ch 9", "marine"),
        (156_525_000, "Marine Ch 22A (Coast Guard)", "marine"),
        (162_475_000, "NOAA WX3 (Vermont/Maine area)", "weather"),
        (162_425_000, "NOAA WX2", "weather"),
        (162_400_000, "NOAA WX1", "weather"),
    ]
    
    for freq_hz, desc, band in KNOWN:
        conn.execute(
            "INSERT OR IGNORE INTO known_frequencies (frequency_hz, description, band_hint) VALUES (?, ?, ?)",
            (freq_hz, desc, band)
        )

def seed_bands(conn):
    # Aviation: strong signals. Marine/Weather: dual-gain comparison needed
    BANDS = [
        ("Aviation VHF", 118_000_000, 137_000_000, 100_000, "AM", 2, 5),
        ("Marine VHF", 156_000_000, 163_000_000, 25_000, "NFM", 2, 9),
        ("NOAA Weather Radio", 162_400_000, 162_575_000, 25_000, "AM", 2, 9),
    ]
    
    for name, start, end, step, demod, lna_low, lna_high in BANDS:
        conn.execute("""
            INSERT INTO bands (name, freq_start_hz, freq_end_hz, step_hz, demodulator, lna_low, lna_high) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET 
                freq_start_hz=excluded.freq_start_hz,
                freq_end_hz=excluded.freq_end_hz,
                step_hz=excluded.step_hz,
                demodulator=excluded.demodulator,
                lna_low=excluded.lna_low,
                lna_high=excluded.lna_high
        """, (name, start, end, step, demod, lna_low, lna_high))

def ws_connect():
    return websocket.create_connection(WS, timeout=3)

def send(ws, event_type, prop="", val=""):
    ws.send(json.dumps({"event_type": event_type, "property": prop, "value": str(val)}))

def recv_all(ws, timeout=0.15):
    texts = []
    binary_data = b''
    ws.settimeout(timeout)
    start = time.time()
    while time.time() - start < timeout:
        try:
            msg = ws.recv()
            if isinstance(msg, str):
                texts.append(json.loads(msg))
            else:
                binary_data += msg
        except websocket.WebSocketTimeoutException:
            break
        except Exception as e:
            print(f"  [recv error: {e}]", file=sys.stderr)
            break
    return texts, binary_data

def get_prop(ws, prop):
    send(ws, "get_property", prop)
    texts, _ = recv_all(ws, 0.5)
    for t in texts:
        if t.get("event_type") == "get_property_response" and t.get("property") == prop:
            return t.get("value", "")
    return None

def spectrum_peak(binary_data):
    if len(binary_data) < 2:
        return 0
    payload_type = struct.unpack_from("<H", binary_data, 0)[0]
    if payload_type == 3:
        return max(binary_data[2:]) if len(binary_data) > 2 else 0
    return 0

def measure_dual_gain(ws, freq_hz, lna_low, lna_high):
    """Measure signal at both low and high gain settings."""
    # Low gain measurement
    send(ws, "set_property", "lna_state", str(lna_low))
    time.sleep(0.1)
    
    send(ws, "set_property", "device_center_frequency", str(freq_hz))
    time.sleep(0.05)
    
    send(ws, "spectrum_enable", "", "true")
    time.sleep(0.1)
    _, binary_low = recv_all(ws, 0.15)
    level_low = spectrum_peak(binary_low)
    
    # High gain measurement (same frequency)
    send(ws, "set_property", "lna_state", str(lna_high))
    time.sleep(0.1)
    
    _, binary_high = recv_all(ws, 0.15)
    level_high = spectrum_peak(binary_high)
    
    send(ws, "spectrum_enable", "", "false")
    
    return level_low, level_high

def scan_band_smart(ws, conn, band_name, freq_start, freq_end, step, demod, lna_low, lna_high):
    """Smart scan using dual-gain comparison to distinguish signals from noise."""
    send(ws, "set_property", "demodulator", demod)
    time.sleep(0.2)
    recv_all(ws, 0.3)

    # Phase 1: Quick low-gain sweep to establish baseline noise floor
    print(f"  Phase 1: Low-gain baseline (LNA={lna_low})...", end=" ", flush=True)
    freq = freq_start
    low_readings = []
    while freq <= freq_end:
        send(ws, "set_property", "device_center_frequency", str(freq))
        time.sleep(0.03)
        
        send(ws, "spectrum_enable", "", "true")
        time.sleep(0.08)
        _, binary = recv_all(ws, 0.12)
        level = spectrum_peak(binary)
        send(ws, "spectrum_enable", "", "false")
        
        low_readings.append((freq, level))
        freq += step
    
    # Calculate baseline noise floor from low-gain readings
    sorted_levels = sorted(l for _, l in low_readings)
    median_idx = len(sorted_levels) // 2
    baseline_noise = sorted_levels[median_idx] if sorted_levels else 0
    print(f"Noise floor: {baseline_noise}/255")

    # Phase 2: High-gain sweep on frequencies that showed anything above baseline at low gain
    print(f"  Phase 2: High-gain check (LNA={lna_high}) on candidates...")
    
    scan_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    signals_found = 0
    
    for freq, level_low in low_readings:
        # Only do high-gain measurement if low gain showed something above baseline
        if level_low > baseline_noise + 5:
            _, level_high = measure_dual_gain(ws, freq, lna_low, lna_high)
            
            # Real signals show significant gain increase with higher LNA
            # Noise amplifies predictably (~6-10 dB per LNA step), real signals stand out
            signal_gain = level_high - level_low
            
            if signal_gain > 20:  # Significant gain indicates real signal
                # Check for known frequency label
                cursor = conn.execute(
                    "SELECT description FROM known_frequencies WHERE ABS(frequency_hz - ?) <= ?",
                    (freq, step // 2)
                )
                row = cursor.fetchone()
                label = row[0] if row else ""

                conn.execute("""
                    INSERT INTO signals (scan_id, band_name, frequency_hz, level_low, level_high, 
                                       noise_floor, signal_gain, demodulator, label)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (scan_id, band_name, freq, level_low, level_high, baseline_noise, signal_gain, demod, label))
                
                signals_found += 1
    
    conn.commit()
    
    print(f"  Found {signals_found} real signals (gain > 20)")
    return signals_found

def show_history(conn):
    """Show scan history."""
    scans = conn.execute("""
        SELECT s.id, s.timestamp, COUNT(sig.id) as signal_count, 
               AVG(sig.level_high) as avg_level, MAX(sig.level_high) as max_level
        FROM scans s
        LEFT JOIN signals sig ON s.id = sig.scan_id
        GROUP BY s.id
        ORDER BY s.timestamp DESC
        LIMIT 10
    """).fetchall()
    
    print("\nRecent Scans:")
    print(f"{'ID':>4} {'Timestamp':<22} {'Signals':>8} {'Avg Level':>10} {'Max Level':>10}")
    print("-" * 60)
    for sid, ts, count, avg_l, max_l in scans:
        avg_str = f"{avg_l:.0f}" if avg_l else "N/A"
        max_str = f"{max_l}" if max_l else "N/A"
        print(f"{sid:>4} {ts:<22} {count:>8} {avg_str:>10} {max_str:>10}")

def main():
    print("SDR Signal Tracker v2 - Smart Dual-Gain Detection")
    print("=" * 50)
    
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    seed_known_frequencies(conn)
    seed_bands(conn)
    
    # Show existing history
    scan_count = conn.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
    signal_count = conn.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    
    if scan_count > 0:
        print(f"Existing database: {scan_count} scans, {signal_count} total signals")
        show_history(conn)
        print()
    
    ws = ws_connect()
    
    can_control = get_prop(ws, "can_control")
    active_device = get_prop(ws, "active_device")
    print(f"Device: {active_device}")
    print(f"Can control: {can_control}")
    
    if can_control != "true":
        send(ws, "device_stream_enable", "", "true")
        time.sleep(1.0)
        recv_all(ws, 1.0)
        can_control = get_prop(ws, "can_control")
        if can_control != "true":
            print("ERROR: Cannot control device.")
            ws.close()
            conn.close()
            return
    
    # Create scan record
    timestamp = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO scans (timestamp, device) VALUES (?, ?)",
        (timestamp, active_device or "unknown")
    )
    
    print(f"\nStarting smart scan at {timestamp}")
    print("=" * 50)
    
    # Get bands from database
    bands = conn.execute("SELECT name, freq_start_hz, freq_end_hz, step_hz, demodulator, lna_low, lna_high FROM bands").fetchall()
    
    total_signals = 0
    for name, start, end, step, demod, lna_low, lna_high in bands:
        print(f"\nScanning: {name} ({start/1e6:.3f}-{end/1e6:.3f} MHz)")
        count = scan_band_smart(ws, conn, name, start, end, step, demod, lna_low, lna_high)
        total_signals += count
    
    # Summary
    print(f"\n{'='*50}")
    print("Scan Complete")
    print(f"  Total real signals detected: {total_signals}")
    print(f"  Database: {DB_PATH}")
    
    # Show top signals from this scan
    scan_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    top = conn.execute("""
        SELECT frequency_hz, level_low, level_high, signal_gain, label, band_name 
        FROM signals WHERE scan_id = ? ORDER BY signal_gain DESC LIMIT 15
    """, (scan_id,)).fetchall()
    
    if top:
        print(f"\nTop 15 signals by gain (real vs noise):")
        for freq, low, high, gain, label, band in top:
            lbl = f" -- {label}" if label else ""
            print(f"  {freq/1e6:9.3f} MHz  Low: {low:3d} -> High: {high:3d} (Δ+{gain})  [{band}]{lbl}")
    
    conn.close()
    ws.close()

if __name__ == "__main__":
    main()
