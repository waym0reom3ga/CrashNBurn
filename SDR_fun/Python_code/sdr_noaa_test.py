#!/usr/bin/env python3
"""Test NOAA weather band sensitivity with different LNA settings."""

import json
import struct
import time
import sys
import websocket

WS = "ws://127.0.0.1:5555"

# Exact NOAA Weather Radio frequencies
NOAA_FREQS = [
    (162_400_000, "WX1"),
    (162_425_000, "WX2"),
    (162_450_000, "WX3 - Vermont/Maine area"),
    (162_475_000, "WX4"),
    (162_500_000, "WX5"),
    (162_525_000, "WX6"),
    (162_550_000, "WX7"),
]

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

def measure_freq(ws, freq_hz, lna_state):
    """Measure signal at a frequency with specific LNA setting."""
    # Set LNA gain
    send(ws, "set_property", "lna_state", str(lna_state))
    time.sleep(0.2)
    
    # Tune to frequency
    send(ws, "set_property", "device_center_frequency", str(freq_hz))
    time.sleep(0.15)
    
    # Set narrow bandwidth for better sensitivity (AM weather radio is ~10 kHz)
    send(ws, "set_property", "filter_bandwidth", "20000")  # 20 kHz
    time.sleep(0.1)
    
    # Enable spectrum and measure
    send(ws, "spectrum_enable", "", "true")
    time.sleep(0.2)
    _, binary = recv_all(ws, 0.3)
    peak = spectrum_peak(binary)
    send(ws, "spectrum_enable", "", "false")
    
    return peak

def main():
    print("NOAA Weather Band Sensitivity Test")
    print("=" * 60)
    
    ws = ws_connect()
    
    can_control = get_prop(ws, "can_control")
    if can_control != "true":
        send(ws, "device_stream_enable", "", "true")
        time.sleep(1.0)
        recv_all(ws, 1.0)
    
    # Test different LNA settings on NOAA frequencies
    lna_settings = [0, 3, 6, 9]  # Low to high gain
    
    print("\nTesting each NOAA frequency at different LNA gain levels:")
    print("(Higher LNA = more sensitivity but also more noise)")
    print()
    
    results = {}
    
    for freq_hz, name in NOAA_FREQS:
        results[freq_hz] = {"name": name, "levels": {}}
        
        for lna in lna_settings:
            level = measure_freq(ws, freq_hz, lna)
            results[freq_hz]["levels"][lna] = level
        
        # Display row
        print(f"{freq_hz/1e6:.3f} MHz ({name}):")
        for lna in lna_settings:
            level = results[freq_hz]["levels"][lna]
            bar_len = min(level // 5, 40)
            bar = "#" * bar_len + "-" * (40 - bar_len)
            print(f"  LNA {lna}: {level:3d}/255 [{bar}]")
        print()
    
    # Find best settings
    print("=" * 60)
    print("ANALYSIS:")
    print("=" * 60)
    
    best_freq = None
    best_lna = None
    best_level = 0
    
    for freq_hz, data in results.items():
        for lna, level in data["levels"].items():
            if level > best_level:
                best_level = level
                best_freq = freq_hz
                best_lna = lna
    
    print(f"\nBest signal found:")
    print(f"  Frequency: {best_freq/1e6:.3f} MHz ({results[best_freq]['name']})")
    print(f"  LNA setting: {best_lna}")
    print(f"  Level: {best_level}/255")
    
    # Check if any signal is significantly above noise floor (~80-90)
    significant = []
    for freq_hz, data in results.items():
        max_level = max(data["levels"].values())
        best_lna_for_freq = max(data["levels"], key=data["levels"].get)
        if max_level > 100:  # Above typical noise floor
            significant.append((freq_hz, data["name"], max_level, best_lna_for_freq))
    
    if significant:
        print(f"\nPotentially detectable signals (level > 100):")
        for freq, name, level, lna in sorted(significant, key=lambda x: -x[2]):
            print(f"  {freq/1e6:.3f} MHz ({name}) - Level: {level}/255 at LNA {lna}")
    else:
        print("\nNo signals significantly above noise floor detected.")
        print("Possible reasons:")
        print("  - Antenna not optimized for 162 MHz (needs ~1/4 wave = ~46cm)")
        print("  - Building blockage reducing VHF reception")
        print("  - Weather stations may be silent between broadcasts")
    
    # Reset to reasonable LNA setting
    send(ws, "set_property", "lna_state", "3")
    
    ws.close()

if __name__ == "__main__":
    main()
