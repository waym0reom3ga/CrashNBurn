#!/usr/bin/env python3
"""SDR Band Scanner - fast version with noise floor detection."""

import json
import struct
import time
import sys
import websocket

WS = "ws://127.0.0.1:5555"

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

def quick_scan(ws, freq_start, freq_end, step):
    """Quick scan to measure noise floor - returns list of (freq, level)."""
    levels = []
    freq = freq_start
    while freq <= freq_end:
        send(ws, "set_property", "device_center_frequency", str(freq))
        time.sleep(0.05)  # Minimal settle
        
        send(ws, "spectrum_enable", "", "true")
        time.sleep(0.1)
        
        _, binary = recv_all(ws, 0.15)
        peak = spectrum_peak(binary)
        
        send(ws, "spectrum_enable", "", "false")
        
        levels.append((freq, peak))
        freq += step
    
    return levels

def main():
    print("SDR Band Scanner - Fast Mode with Noise Floor Detection")
    print("=" * 60)
    
    ws = ws_connect()
    
    # Check device status
    can_control = get_prop(ws, "can_control")
    active_device = get_prop(ws, "active_device")
    print(f"Device: {active_device}")
    print(f"Can control: {can_control}")
    
    if can_control != "true":
        print("Enabling device stream...")
        send(ws, "device_stream_enable", "", "true")
        time.sleep(1.0)
        recv_all(ws, 1.0)
        can_control = get_prop(ws, "can_control")
        if can_control != "true":
            print("ERROR: Cannot control device.")
            ws.close()
            return
    
    # Bands with coarse step for initial scan (100 kHz), then fine-tune hotspots
    BANDS = [
        ("Aviation VHF",     118_000_000, 137_000_000, "AM"),
        ("Marine VHF",       156_000_000, 163_000_000, "NFM"),
        ("NOAA Weather Radio", 162_400_000, 162_575_000, "AM"),
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
    
    for name, freq_start, freq_end, demod in BANDS:
        print(f"\n{'='*60}")
        print(f"Scanning: {name} ({freq_start/1e6:.3f}-{freq_end/1e6:.3f} MHz)")
        
        # Set demodulator
        send(ws, "set_property", "demodulator", demod)
        time.sleep(0.2)
        recv_all(ws, 0.3)
        
        # Phase 1: Quick scan with 100 kHz steps to find noise floor + hotspots
        coarse_step = 100_000  # 100 kHz
        levels = quick_scan(ws, freq_start, freq_end, coarse_step)
        
        if not levels:
            continue
        
        # Calculate noise floor (median of all readings)
        sorted_levels = sorted(l for _, l in levels)
        median_idx = len(sorted_levels) // 2
        noise_floor = sorted_levels[median_idx]
        
        print(f"  Noise floor: {noise_floor}/255")
        
        # Phase 2: Report signals significantly above noise floor (>15 points higher)
        threshold = noise_floor + 15
        
        print(f"  Signal threshold: {threshold}/255 (noise + 15)")
        print()
        
        for freq, level in levels:
            if level >= threshold:
                freq_mhz = freq / 1e6
                
                # Check nearby known frequencies
                label = ""
                for kf, kl in KNOWN.items():
                    if abs(freq - kf) <= coarse_step // 2:
                        label = kl
                        break
                
                bar_len = min((level - noise_floor) * 2, 40)
                bar = "#" * bar_len + "-" * (40 - bar_len)
                
                line = f"  {freq_mhz:9.3f} MHz [{bar}] {level:3d}"
                if label:
                    line += f"  <-- {label}"
                print(line, flush=True)
                all_signals.append((freq, level, label))
        
        # Phase 3: Check specific known frequencies in this band
        for kf, kl in KNOWN.items():
            if freq_start <= kf <= freq_end and not any(abs(f - kf) < coarse_step for f, _, _ in all_signals):
                send(ws, "set_property", "device_center_frequency", str(kf))
                time.sleep(0.1)
                
                send(ws, "spectrum_enable", "", "true")
                time.sleep(0.15)
                _, binary = recv_all(ws, 0.2)
                peak = spectrum_peak(binary)
                send(ws, "spectrum_enable", "", "false")
                
                if peak >= threshold:
                    freq_mhz = kf / 1e6
                    bar_len = min((peak - noise_floor) * 2, 40)
                    bar = "#" * bar_len + "-" * (40 - bar_len)
                    print(f"  {freq_mhz:9.3f} MHz [{bar}] {peak:3d}  <-- {kl}", flush=True)
                    all_signals.append((kf, peak, kl))
    
    # Summary
    print(f"\n{'='*60}")
    print("SCAN SUMMARY")
    print(f"{'='*60}")
    
    if not all_signals:
        print("\nNo significant signals detected above noise floor.")
        print("(Could mean no active transmitters or antenna issues)")
    else:
        all_signals.sort(key=lambda x: -x[1])
        print(f"\nTop {min(len(all_signals), 20)} signals (by strength):")
        for freq, level, label in all_signals[:20]:
            line = f"  {freq/1e6:9.3f} MHz  Level: {level:3d}/255"
            if label:
                line += f"  -- {label}"
            print(line)
    
    ws.close()

if __name__ == "__main__":
    main()
