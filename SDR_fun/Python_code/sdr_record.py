#!/usr/bin/env python3
"""SDR Signal Recorder - records 30-second audio segments of detected signals."""

import json
import struct
import time
import csv
import sys
import os
import wave
from datetime import datetime

import websocket

WS = "ws://127.0.0.1:5555"
SIGNALS_CSV = "/home/waymore/sdr_signals.csv"
RECORD_DIR = "/home/waymore/sdr_recordings"
DURATION = 30  # seconds per recording

def ws_connect():
    return websocket.create_connection(WS, timeout=3)

def send(ws, event_type, prop="", val=""):
    ws.send(json.dumps({"event_type": event_type, "property": prop, "value": str(val)}))

def recv_all(ws, timeout=0.5):
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

def record_audio(ws, freq_hz, demodulator, duration=30):
    """Record audio from SDRconnect for specified duration. Returns raw PCM bytes."""
    # Set frequency and demodulator
    send(ws, "set_property", "device_center_frequency", str(freq_hz))
    time.sleep(0.2)
    
    send(ws, "set_property", "demodulator", demodulator)
    time.sleep(0.2)
    
    # Set reasonable audio parameters
    send(ws, "set_property", "audio_volume_percent", "100")
    send(ws, "set_property", "audio_mute", "false")
    recv_all(ws, 0.3)
    
    # Enable audio streaming (binary payload type 1 = signed 16-bit PCM stereo @48kHz LRLR)
    send(ws, "audio_stream_enable", "", "true")
    time.sleep(0.5)
    
    # Record for specified duration
    print(f"  Recording {duration}s...", end="", flush=True)
    audio_chunks = []
    start_time = time.time()
    
    while time.time() - start_time < duration:
        texts, binary = recv_all(ws, 0.5)
        if binary and len(binary) >= 2:
            payload_type = struct.unpack_from("<H", binary, 0)[0]
            if payload_type == 1:  # Audio data (signed 16-bit PCM stereo @48kHz)
                audio_chunks.append(binary[2:])  # Skip 2-byte header
    
    # Disable audio streaming
    send(ws, "audio_stream_enable", "", "false")
    
    total_bytes = sum(len(c) for c in audio_chunks)
    print(f" {total_bytes} bytes captured ({total_bytes/96000:.1f}s of audio)")
    
    return b''.join(audio_chunks)

def save_wav(filepath, pcm_data):
    """Save PCM data as WAV file (signed 16-bit stereo @48kHz)."""
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(2)      # Stereo
        wav_file.setsampwidth(2)       # 16-bit
        wav_file.setframerate(48000)   # 48kHz sample rate
        wav_file.writeframes(pcm_data)

def main():
    print("SDR Signal Recorder")
    print("=" * 50)
    
    # Read signals from CSV
    if not os.path.exists(SIGNALS_CSV):
        print(f"ERROR: Signals file not found: {SIGNALS_CSV}")
        print("Run sdr_document.py first to create it.")
        return
    
    with open(SIGNALS_CSV, 'r') as f:
        reader = csv.DictReader(f)
        signals = list(reader)
    
    if not signals:
        print("No signals found in CSV file.")
        return
    
    # Sort by signal strength (descending) and take top 20
    signals.sort(key=lambda x: -int(x["level"]))
    signals_to_record = signals[:20]
    
    print(f"Found {len(signals)} signals, recording top {len(signals_to_record)}")
    print(f"Duration per signal: {DURATION}s")
    print(f"Output directory: {RECORD_DIR}")
    print()
    
    # Create output directory
    os.makedirs(RECORD_DIR, exist_ok=True)
    
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
        return
    
    for i, sig in enumerate(signals_to_record):
        freq_hz = int(sig["frequency_hz"])
        demodulator = sig["demodulator"]
        level = int(sig["level"])
        label = sig.get("label", "")
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        freq_str = f"{freq_hz/1e6:.3f}".replace(".", "_")
        safe_label = "".join(c if c.isalnum() else "_" for c in label)[:20]
        filename = f"{timestamp}_{freq_str}MHz_{i+1:02d}_L{level}"
        if safe_label and safe_label != "_":
            filename += f"_{safe_label}"
        filepath = os.path.join(RECORD_DIR, f"{filename}.wav")
        
        print(f"[{i+1}/{len(signals_to_record)}] Recording {freq_hz/1e6:.3f} MHz "
              f"(Level: {level}/255) [{sig['band_name']}]")
        if label:
            print(f"  Label: {label}")
        
        # Record audio
        pcm_data = record_audio(ws, freq_hz, demodulator, DURATION)
        
        if pcm_data and len(pcm_data) > 0:
            save_wav(filepath, pcm_data)
            file_size_kb = os.path.getsize(filepath) / 1024
            print(f"  Saved: {filepath} ({file_size_kb:.0f} KB)")
        else:
            print(f"  WARNING: No audio captured!")
        
        # Brief pause between recordings
        time.sleep(0.5)
    
    ws.close()
    
    print(f"\n{'='*50}")
    print("Recording complete!")
    print(f"All files saved to: {RECORD_DIR}/")

if __name__ == "__main__":
    main()
