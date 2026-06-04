#!/bin/bash
# SDR Band Scanner using websocat + SDRconnect WebSocket API
# Scans aviation, marine, and weather bands for active signals

WS="ws://127.0.0.1:5555"

send_cmd() {
    # Send a JSON command to SDRconnect
    echo "$1" | websocat -1 --no-close "$WS" 2>/dev/null
}

get_prop() {
    # Get a property value
    local prop="$1"
    send_cmd "{\"event_type\":\"get_property\",\"property\":\"$prop\"}" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('value',''))" 2>/dev/null
}

set_freq() {
    # Set center frequency in Hz
    local freq="$1"
    send_cmd "{\"event_type\":\"set_property\",\"property\":\"device_center_frequency\",\"value\":\"$freq\"}"
    sleep 0.3
}

capture_spectrum_peak() {
    # Capture spectrum bins and find peak level (0-255)
    # Binary payload type 3 = unsigned 8-bit spectrum FFT bins
    
    # Enable spectrum streaming
    send_cmd "{\"event_type\":\"spectrum_enable\",\"property\":\"\",\"value\":\"true\"}"
    sleep 0.2
    
    # Capture binary data for ~0.5 seconds, extract peak byte value
    local peak=0
    websocat --timeout-internal 1 "$WS" </dev/null 2>/dev/null | \
        python3 -c "
import sys
data = sys.stdin.buffer.read(65536)
if len(data) >= 2:
    # Skip 2-byte payload type header, find max byte value in spectrum bins
    peak = max(data[2:]) if len(data) > 2 else 0
print(peak)
" 2>/dev/null || echo "0"
    
    # Disable spectrum streaming
    send_cmd "{\"event_type\":\"spectrum_enable\",\"property\":\"\",\"value\":\"false\"}"
}

scan_band() {
    local name="$1"
    local freq_start="$2"
    local freq_end="$3"
    local step="$4"
    local demod="$5"
    
    echo ""
    echo "============================================================"
    echo "Scanning: $name"
    echo "Range: $(echo "$freq_start / 1000000" | bc) - $(echo "$freq_end / 1000000" | bc) MHz"
    echo "Step: $(echo "$step / 1000" | bc) kHz | Demodulator: $demod"
    echo "============================================================"
    
    # Set demodulator mode
    send_cmd "{\"event_type\":\"set_property\",\"property\":\"demodulator\",\"value\":\"$demod\"}"
    sleep 0.2
    
    local freq=$freq_start
    while [ "$freq" -le "$freq_end" ]; do
        set_freq "$freq"
        
        # Capture spectrum peak
        local level=$(capture_spectrum_peak)
        
        # Only report signals above threshold (80 out of 255)
        if [ "$level" -gt 80 ] 2>/dev/null; then
            local freq_mhz=$(echo "scale=3; $freq / 1000000" | bc)
            # Create a simple bar chart
            local bar_len=$((level / 6))
            [ "$bar_len" -gt 40 ] && bar_len=40
            local bar=""
            for ((i=0; i<bar_len; i++)); do bar+="█"; done
            for ((i=bar_len; i<40; i++)); do bar+="░"; done
            
            echo "  ${freq_mhz} MHz [${bar}] ${level}/255"
        fi
        
        freq=$((freq + step))
    done
}

# Main execution
echo "SDR Band Scanner - SDRconnect WebSocket API"
echo "============================================="

# Verify device is ready
can_control=$(get_prop "can_control")
active_device=$(get_prop "active_device")
echo "Device: $active_device"
echo "Can control: $can_control"

if [ "$can_control" != "true" ]; then
    echo "ERROR: Device cannot be controlled. Is SDRconnect running?"
    exit 1
fi

# Ensure device streaming is enabled
send_cmd "{\"event_type\":\"device_stream_enable\",\"property\":\"\",\"value\":\"true\"}"
sleep 0.5

echo ""
echo "Starting scan..."
echo "(This will take several minutes - scanning ~800+ frequencies)"
echo ""

# Scan aviation VHF (118-137 MHz, 25 kHz steps)
scan_band "Aviation VHF" 118000000 137000000 25000 "AM"

# Scan marine VHF (156-163 MHz, 25 kHz steps)  
scan_band "Marine VHF" 156000000 163000000 25000 "NFM"

# Scan NOAA Weather Radio (162.400-162.575 MHz, 25 kHz steps)
scan_band "NOAA Weather Radio" 162400000 162575000 25000 "AM"

echo ""
echo "============================================================"
echo "Scan complete!"
echo "============================================================"
