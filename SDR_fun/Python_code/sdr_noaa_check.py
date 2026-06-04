#!/usr/bin/env python3
"""Quick NOAA frequency check."""
import json, struct, time, websocket

WS = "ws://127.0.0.1:5555"
ws = websocket.create_connection(WS, timeout=3)

def send(ws, et, p="", v=""):
    ws.send(json.dumps({"event_type": et, "property": p, "value": str(v)}))

def recv_all(ws, t=0.2):
    texts, binary = [], b''
    ws.settimeout(t)
    start = time.time()
    while time.time() - start < t:
        try:
            msg = ws.recv()
            if isinstance(msg, str): texts.append(json.loads(msg))
            else: binary += msg
        except: break
    return texts, binary

# Set high sensitivity for weather band
send(ws, "set_property", "lna_state", "9")
time.sleep(0.2)
send(ws, "set_property", "demodulator", "AM")
time.sleep(0.1)

NOAA = [
    (162_400_000, "WX1"),
    (162_425_000, "WX2"), 
    (162_450_000, "WX3 - VT/ME"),
    (162_475_000, "WX4"),
    (162_500_000, "WX5"),
    (162_525_000, "WX6"),
    (162_550_000, "WX7"),
]

print("NOAA Weather Band - Exact Frequency Check")
print("=" * 50)
for freq, name in NOAA:
    send(ws, "set_property", "device_center_frequency", str(freq))
    time.sleep(0.15)
    
    # Measure spectrum peak
    send(ws, "spectrum_enable", "", "true")
    time.sleep(0.2)
    _, binary = recv_all(ws, 0.3)
    
    if len(binary) >= 2:
        payload_type = struct.unpack_from("<H", binary, 0)[0]
        if payload_type == 3:
            peak = max(binary[2:]) if len(binary) > 2 else 0
        else:
            peak = 0
    else:
        peak = 0
    
    send(ws, "spectrum_enable", "", "false")
    
    bar_len = min(peak // 5, 40)
    bar = "#" * bar_len + "-" * (40 - bar_len)
    print(f"{freq/1e6:.3f} MHz ({name:12}): {peak:3d}/255 [{bar}]")

ws.close()
