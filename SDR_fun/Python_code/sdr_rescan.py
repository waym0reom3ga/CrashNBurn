#!/usr/bin/env python3
"""SDR Signal Rescanner - checks which previously detected signals are still active."""

import json
import struct
import time
import sqlite3
import sys
from datetime import datetime

import websocket

WS = "ws://127.0.0.1:5555"
DB_PATH = "/home/waymore/sdr_signals.db"

def ws_connect():
    return websocket.create_connection(WS, timeout=3)

def send(ws, event_type, prop="", val=""):
    ws.send(json.dumps({"event_type": event_type, "property": prop, "value": str(val)}))

def recv_all(ws, timeout=0.2):
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

def measure_signal(ws, freq_hz, demodulator):
    """Measure signal level at a specific frequency."""
    send(ws, "set_property", "device_center_frequency", str(freq_hz))
    time.sleep(0.1)
    
    send(ws, "set_property", "demodulator", demodulator)
    time.sleep(0.15)
    
    send(ws, "spectrum_enable", "", "true")
    time.sleep(0.15)
    _, binary = recv_all(ws, 0.2)
    peak = spectrum_peak(binary)
    send(ws, "spectrum_enable", "", "false")
    
    return peak

def main():
    print("SDR Signal Rescanner - Activity Check")
    print("=" * 60)
    
    conn = sqlite3.connect(DB_PATH)
    
    # Get the most recent scan's signals
    latest_scan = conn.execute("""
        SELECT s.id, s.timestamp 
        FROM scans s ORDER BY s.timestamp DESC LIMIT 1
    """).fetchone()
    
    if not latest_scan:
        print("ERROR: No previous scans found. Run sdr_tracker.py first.")
        conn.close()
        return
    
    scan_id, timestamp = latest_scan
    print(f"Latest scan #{scan_id} at {timestamp}")
    
    # Get signals from that scan, sorted by level descending
    signals = conn.execute("""
        SELECT frequency_hz, level, noise_floor, demodulator, label, band_name
        FROM signals WHERE scan_id = ? ORDER BY level DESC LIMIT 20
    """, (scan_id,)).fetchall()
    
    if not signals:
        print("No signals found in latest scan.")
        conn.close()
        return
    
    print(f"Rescanning {len(signals)} strongest signals...")
    print()
    
    ws = ws_connect()
    
    can_control = get_prop(ws, "can_control")
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
    
    # Rescan each signal
    results = []
    active_count = 0
    weak_count = 0
    inactive_count = 0
    
    for i, (freq_hz, prev_level, noise_floor, demodulator, label, band_name) in enumerate(signals):
        curr_level = measure_signal(ws, freq_hz, demodulator)
        
        # Determine status based on signal above noise floor
        signal_above_noise = curr_level - noise_floor
        
        if signal_above_noise >= 15:
            status = "ACTIVE"
            active_count += 1
        elif signal_above_noise >= 8:
            status = "WEAK"
            weak_count += 1
        else:
            status = "INACTIVE"
            inactive_count += 1
        
        level_change = curr_level - prev_level
        
        results.append({
            "frequency_hz": freq_hz,
            "previous_level": prev_level,
            "current_level": curr_level,
            "level_change": level_change,
            "noise_floor": noise_floor,
            "status": status,
            "demodulator": demodulator,
            "label": label,
            "band_name": band_name,
        })
        
        # Display result with visual bar
        arrow = "↑" if level_change > 0 else ("↓" if level_change < 0 else "→")
        bar_len = min(curr_level // 5, 40)
        bar = "#" * bar_len + "-" * (40 - bar_len)
        
        status_tag = {"ACTIVE": "[ACTIVE]", "WEAK": "[ WEAK ]", "INACTIVE": "[GONE]"}[status]
        
        print(f"[{i+1:2d}/{len(signals)}] {freq_hz/1e6:9.3f} MHz {status_tag} "
              f"{curr_level:3d}/255 [{bar}] Δ{arrow}{abs(level_change)}")
        if label:
            print(f"       Label: {label}")
    
    # Store rescan results in database as a new scan entry
    rescan_timestamp = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO scans (timestamp, device, notes) VALUES (?, ?, ?)",
        (rescan_timestamp, "rescan", f"Rescan of scan #{scan_id}")
    )
    rescan_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    
    for r in results:
        if r["status"] != "INACTIVE":  # Only store active/weak signals
            conn.execute("""
                INSERT INTO signals (scan_id, band_name, frequency_hz, level, noise_floor, 
                                   signal_above_noise, demodulator, label)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (rescan_id, r["band_name"], r["frequency_hz"], r["current_level"],
                  r["noise_floor"], r["current_level"] - r["noise_floor"],
                  r["demodulator"], r["label"]))
    
    conn.commit()
    
    # Summary
    print(f"\n{'='*60}")
    print("RESCAN SUMMARY")
    print(f"{'='*60}")
    print(f"Signals rescanned: {len(results)}")
    print(f"Active signals:    {active_count} ({active_count/len(results)*100:.0f}%)")
    print(f"Weak signals:      {weak_count} ({weak_count/len(results)*100:.0f}%)")
    print(f"Inactive signals:  {inactive_count}/{len(results)}")
    print()
    
    # Show active signals sorted by current level
    active_signals = [r for r in results if r["status"] == "ACTIVE"]
    weak_signals = [r for r in results if r["status"] == "WEAK"]
    inactive_signals = [r for r in results if r["status"] == "INACTIVE"]
    
    if active_signals:
        print("Active signals (sorted by current level):")
        active_signals.sort(key=lambda x: -x["current_level"])
        for s in active_signals[:10]:
            label_str = f" -- {s['label']}" if s['label'] else ""
            change_str = f"+{s['level_change']}" if s['level_change'] > 0 else str(s['level_change'])
            print(f"  {s['frequency_hz']/1e6:9.3f} MHz  Current: {s['current_level']:3d}/255 "
                  f"(was {s['previous_level']:3d}, Δ{change_str}){label_str}")
    
    if weak_signals:
        print("\nWeak signals:")
        for s in weak_signals:
            label_str = f" -- {s['label']}" if s['label'] else ""
            print(f"  {s['frequency_hz']/1e6:9.3f} MHz  Current: {s['current_level']:3d}/255{label_str}")
    
    if inactive_signals:
        print("\nInactive signals:")
        for s in inactive_signals:
            label_str = f" -- {s['label']}" if s['label'] else ""
            print(f"  {s['frequency_hz']/1e6:9.3f} MHz  Current: {s['current_level']:3d}/255 "
                  f"(was {s['previous_level']:3d}){label_str}")
    
    # Show database stats
    total_scans = conn.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
    total_signals = conn.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    unique_freqs = conn.execute("SELECT COUNT(DISTINCT frequency_hz) FROM signals").fetchone()[0]
    
    print(f"\nDatabase stats: {total_scans} scans, {total_signals} signal entries, "
          f"{unique_freqs} unique frequencies")
    print(f"Database file: {DB_PATH}")
    
    conn.close()
    ws.close()

if __name__ == "__main__":
    main()
