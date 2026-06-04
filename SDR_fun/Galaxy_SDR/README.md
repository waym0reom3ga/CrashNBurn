# Galaxy SDR

Device-agnostic retro TUI for any SDR dongle with **CRT visual effects engine**.

## Features

### Core Functionality
- **Dynamic device detection** - Automatically identifies RSP1A, RTL-SDR, or unknown devices
- **22-band database** - Pre-configured bands from Time Signals to GSM uplink
- **Auto-demodulation** - Correct demodulator selected per band (AM/NFM/WBFM)
- **Full device scan** - Sweep entire frequency range with adaptive step sizes
- **Band selection menu** - Toggle which bands to display and scan
- **Persistent settings** - Volume, top-N, clip duration saved between sessions

### CRT Visual Effects
- **5 Color Themes**: phosphor_green, amber, blue, white, synthwave
- **Scanlines** - Adjustable intensity (subtle/medium/heavy)
- **Phosphor Glow** - Background glow effect matching theme color
- **Static Noise** - Random character flickering like old CRT monitors
- **Screen Flicker** - Occasional frame dimming for authenticity
- **Vignette** - Corner darkening simulating tube curvature
- **Scroll Blur** - Brief smear effect when scrolling through stations
- **Boot Animation** - Scanline wipe-in with ASCII art logo

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
| **T** | **CRT settings menu (themes, effects toggles)** |
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

Settings persist in `~/.sdr_retro/config.json` including CRT effects configuration.

## File Structure

- `galaxy_sdr.py` - Main application with SDR backend and TUI
- `crt_effects.py` - CRT visual effects engine (themes, scanlines, noise, flicker)
- `test_galaxy_sdr.py` - Functional test suite
