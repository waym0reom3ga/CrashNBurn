#!/usr/bin/env python3
"""SDR Signal Documenter - scans bands and saves results to CSV."""

import json
import struct
import time
import csv
import sys
from datetime import datetime

import websocket

WS = "ws://127.0.0.1:5555"
OUTPUT_CSV = "/home/waymore/sdr_signals.csv"

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

def scan_band(ws, name, freq_start, freq_end, step, demod):
    """Scan a band and return list of (freq_hz, level, noise_floor)."""
    send(ws, "set_property", "demodulator", demod)
    time.sleep(0.2)
    recv_all(ws, 0.3)

    # Collect all readings first to determine noise floor
    readings = []
    freq = freq_start
    while freq <= freq_end:
        send(ws, "set_property", "device_center_frequency", str(freq))
        time.sleep(0.05)

        send(ws, "spectrum_enable", "", "true")
        time.sleep(0.1)
        _, binary = recv_all(ws, 0.15)
        peak = spectrum_peak(binary)
        send(ws, "spectrum_enable", "", "false")

        readings.append((freq, peak))
        freq += step

    # Calculate noise floor (median)
    sorted_levels = sorted(l for _, l in readings)
    median_idx = len(sorted_levels) // 2
    noise_floor = sorted_levels[median_idx] if sorted_levels else 0

    return [(f, l, noise_floor) for f, l in readings], noise_floor

def main():
    print("SDR Signal Documenter")
    print("=" * 50)
    
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
            return
    
    # Bands to scan (coarse step for speed)
    BANDS = [
        ("Aviation VHF",     118_000_000, 137_000_000, 100_000, "AM"),
        ("Marine VHF",       156_000_000, 163_000_000, 25_000, "NFM"),
        ("NOAA Weather Radio", 162_400_000, 162_575_000, 25_000, "AM"),
    ]
    
    KNOWN = {
        121_500_000: "Aviation Emergency (Guard)",
        122_650_000: "Flight Service Station",
        156_800_000: "Marine Ch 16 - Distress/Safety",
        156_300_000: "Marine Ch 9",
        156_525_000: "Marine Ch 22A (Coast Guard)",
        162_475_000: "NOAA WX3 (Montreal area)",
        162_425_000: "NOAA WX2",
        162_400_000: "NOAA WX1",
    }
    
    all_signals = []
    
    for name, freq_start, freq_end, step, demod in BANDS:
        print(f"\nScanning: {name} ({freq_start/1e6:.3f}-{freq_end/1e6:.3f} MHz)")
        
        readings, noise_floor = scan_band(ws, name, freq_start, freq_end, step, demod)
        threshold = noise_floor + 15
        
        print(f"  Noise floor: {noise_floor}/255 | Threshold: {threshold}/255")
        
        for freq, level, nf in readings:
            if level >= threshold:
                # Check known frequencies nearby
                label = ""
                for kf, kl in KNOWN.items():
                    if abs(freq - kf) <= step // 2:
                        label = kl
                        break
                
                all_signals.append({
                    "timestamp": datetime.now().isoformat(),
                    "band_name": name,
                    "frequency_hz": freq,
                    "frequency_mhz": round(freq / 1e6, 3),
                    "level": level,
                    "noise_floor": nf,
                    "signal_above_noise": level - nf,
                    "demodulator": demod,
                    "label": label,
                })
    
    # Write CSV
    if all_signals:
        fieldnames = ["timestamp", "band_name", "frequency_hz", "frequency_mhz", 
                      "level", "noise_floor", "signal_above_noise", "demodulator", "label"]
        
        with open(OUTPUT_CSV, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for sig in all_signals:
                writer.writerow(sig)
        
        print(f"\n{'='*50}")
        print(f"Saved {len(all_signals)} signals to {OUTPUT_CSV}")
        print(f"\nTop 10 by strength:")
        sorted_sigs = sorted(all_signals, key=lambda x: -x["level"])
        for s in sorted_sigs[:10]:
            label_str = f" -- {s['label']}" if s['label'] else ""
            print(f"  {s['frequency_mhz']:9.3f} MHz  Level: {s['level']:3d}/255  "
                  f"Above noise: +{s['signal_above_noise']}  [{s['band_name']}]{label_str}")
    else:
        print("\nNo significant signals detected.")
    
    ws.close()

if __name__ == "__main__":
    main()
