# Galaxy SDR

Device-agnostic retro TUI for any SDR dongle with green phosphor CRT aesthetic.

## Features

- **Dynamic device detection** - Automatically identifies RSP1A, RTL-SDR, or unknown devices
- **22-band database** - Pre-configured bands from Time Signals to GSM uplink
- **Auto-demodulation** - Correct demodulator selected per band (AM/NFM/WBFM)
- **Full device scan** - Sweep entire frequency range with adaptive step sizes
- **Band selection menu** - Toggle which bands to display and scan
- **Persistent settings** - Volume, top-N, clip duration saved between sessions

## Requirements

- Python 3.10+
- SDR hardware (SDRPlay RSP1A, RTL-SDR, etc.)
- Audio backend: `ffplay` > `paplay` > `aplay` (Linux) | `play` > `/dev/dsp` (FreeBSD)

## Controls

| Key | Action |
|-----|--------|
| ↑↓ | Navigate station list |
| ←→ | Previous/next frequency |
| SPACE | Play/pause audio |
| R | Record toggle |
| S | Band scan (selected bands) |
| F | Full device scan |
| B | Band selection menu |
| +/- | Volume up/down (5% steps, starts at 5%) |
| N | Cycle top-N count (10/20/30/50/100) |
| D | Cycle clip duration (10/15/30/60s) |
| A | Toggle auto-scan interval |
| Q | Quit |

## Usage

```bash
# Ensure SDRconnect headless is running:
/usr/bin/sdrconnect-headless --websocket_port=5555 &

# Launch Galaxy SDR:
python3 galaxy_sdr.py
```

Settings persist in `~/.sdr_retro/config.json`.
