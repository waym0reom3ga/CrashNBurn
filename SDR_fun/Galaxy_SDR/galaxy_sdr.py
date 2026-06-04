#!/usr/bin/env python3
"""
Galaxy SDR - Device-agnostic retro TUI for any SDR dongle.

Features:
  - Dynamic device detection (RTL-SDR, SDRPlay, etc.)
  - Comprehensive band database with auto-demodulation
  - Full-scan mode across entire device range
  - Band selection menu to filter displayed signals
  - Persistent settings (volume, top-N, clip duration)
  - CRT visual effects engine (scanlines, phosphor glow, noise, flicker, vignette)
  - 5 color themes: phosphor_green, amber, blue, white, synthwave

Controls:
  Up/Down arrows   Navigate station list
  Left/Right       Previous/Next station
  Space            Play/Pause current station
  R                Toggle recording on/off
  S                Trigger band scan (selected bands only)
  F                Full device scan (entire range, all gain levels)
  B                Band selection menu (toggle which bands to display)
  T                CRT settings menu (themes, effects toggles)
  +/-              Volume up/down (5% steps)
  N                Cycle top-N count (10/20/30/50/100)
  D                Cycle clip duration (10/15/30/60s)
  A                Toggle auto-scan interval
  Q                Quit

Cross-platform audio: auto-detects ffplay, paplay, play (sox), or /dev/dsp.
"""

import curses
import json
import os
import platform
import queue
import sqlite3
import struct
import subprocess
import sys
import threading
import time
import wave
from datetime import datetime

try:
    import websocket
except ImportError:
    print("ERROR: websocket-client required. Install: pip install websocket-client", file=sys.stderr)
    sys.exit(1)

# Import CRT effects engine
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt_effects import (
    CRTEngine,
    CRTConfig,
    THEMES,
    theme_pair,
    reset_color_pairs,
    boot_animation,
    draw_settings_menu,
    handle_settings_input,
)

# ─── Configuration ──────────────────────────────────────────────────────────

WS_URL = "ws://127.0.0.1:5555"
DB_PATH = os.path.expanduser("~/.sdr_retro/signals.db")
RECORD_DIR = os.path.expanduser("~/.sdr_retro/recordings")
CONFIG_PATH = os.path.expanduser("~/.sdr_retro/config.json")

DEFAULT_VOLUME = 5
DEFAULT_TOP_N = 50
DEFAULT_CLIP_DURATION = 30
DEFAULT_AUTO_SCAN_INTERVAL = 0  # Off by default


# ─── Comprehensive Band Database ────────────────────────────────────────────
# Based on ITU frequency allocations and common SDR usage.
# Each band: (name, freq_start_hz, freq_end_hz, step_hz, demodulator, description)

BANDS_DB = [
    # LF / VLF
    ("Time Signals", 28_500_000, 60_000_000, 10_000, "AM", "WWV/DCF77/JJY time signals"),

    # MF - AM Broadcast & Maritime
    ("AM Broadcast (US)", 530_000, 1700_000, 10_000, "AM", "Medium wave AM radio stations"),
    ("Marine MF", 180_000, 285_000, 1_000, "NFM", "MF maritime communications"),

    # HF - Shortwave
    ("HF General (3-30 MHz)", 3_000_000, 30_000_000, 1_000, "AM", "Shortwave broadcast, ham, maritime"),
    ("SW Broadcast Band I", 5900_000, 6200_000, 9_000, "AM", "International shortwave (Band 49)"),
    ("SW Broadcast Band II", 7200_000, 7400_000, 9_000, "AM", "International shortwave (Band 60)"),
    ("SW Broadcast Band III", 9400_000, 9900_000, 9_000, "AM", "International shortwave (Band 71)"),
    ("SW Broadcast Band IV", 11600_000, 12100_000, 9_000, "AM", "International shortwave (Band 90)"),
    ("SW Broadcast Band V", 15100_000, 15800_000, 9_000, "AM", "International shortwave (Band 11)"),

    # VHF Low Band
    ("VHF Low Public Safety", 30_000_000, 50_000_000, 12_500, "NFM", "Police/fire/EMS trunked radio"),
    ("VHF Low Ham (6m)", 50_000_000, 54_000_000, 10_000, "NFM", "Amateur 6-meter band"),

    # VHF High Band - Aviation & Marine
    ("Aviation VHF", 108_000_000, 137_000_000, 25_000, "AM", "Civil aviation voice comms"),
    ("Marine VHF", 156_000_000, 162_000_000, 25_000, "NFM", "Maritime mobile communications"),

    # NOAA Weather Radio (US)
    ("NOAA Weather", 162_400_000, 162_575_000, 25_000, "AM", "NOAA weather radio stations"),

    # VHF FM Broadcast
    ("FM Broadcast (US)", 88_000_000, 108_000_000, 100_000, "WFM", "VHF-FM stereo broadcast radio"),

    # VHF Ham Bands
    ("Ham 2m VHF", 144_000_000, 148_000_000, 5_000, "NFM", "Amateur 2-meter band (FM/SSB)"),

    # UHF - Public Safety & Ham
    ("UHF Public Safety", 450_000_000, 470_000_000, 12_500, "NFM", "Police/fire/trunked radio"),
    ("Ham 70cm UHF", 420_000_000, 450_000_000, 5_000, "NFM", "Amateur 70cm band (FM/SSB)"),

    # TV Channels (VHF/UHF - for SDR experimentation)
    ("TV VHF Ch 2-6", 54_000_000, 88_000_000, 6_000_000, "WFM", "VHF TV channels (ATSC analog)"),

    # ADS-B & ACARS
    ("ADS-B Aircraft", 1090_000_000, 1090_100_000, 10_000, "AM", "Aircraft transponder (1090 MHz)"),

    # GSM/Cellular (for spectrum analysis only - do not decode)
    ("GSM 850 Uplink", 824_000_000, 849_000_000, 200_000, "AM", "GSM 850 MHz uplink (spectrum only)"),
    ("GSM 1900 Uplink", 1850_000_000, 1910_000_000, 200_000, "AM", "GSM 1900 MHz uplink (spectrum only)"),
]

# Known frequencies with labels for auto-identification
KNOWN_FREQS = [
    # Aviation
    (121_500_000, "Aviation Emergency (Guard)", "aviation"),
    (122_650_000, "Flight Service Station", "aviation"),

    # Marine
    (156_800_000, "Marine Ch 16 - Distress/Safety", "marine"),
    (156_300_000, "Marine Ch 9", "marine"),
    (156_525_000, "Marine Ch 22A (Coast Guard)", "marine"),

    # NOAA Weather (US)
    (162_475_000, "NOAA WX3 (Vermont/Maine area)", "weather"),
    (162_425_000, "NOAA WX2", "weather"),
    (162_400_000, "NOAA WX1", "weather"),

    # Time signals
    (28_500_000, "WWV (NIST) 10 MHz", "time"),
    (60_000_000, "DCF77 (Germany)", "time"),
]


# ─── Audio Backend Detection ────────────────────────────────────────────────

def detect_audio_backend():
    """Find the best available audio playback tool."""
    system = platform.system()

    if system == "FreeBSD":
        for cmd in [["play"], ["cat"]]:
            path = __import__("shutil").which(cmd[0])
            if path:
                return {"type": "freebsd", "cmd": cmd, "path": path}
    else:
        # Linux - prefer ffplay (more reliable with PipeWire), then paplay, aplay
        for name in ["ffplay", "paplay", "aplay"]:
            path = __import__("shutil").which(name)
            if path:
                return {"type": name, "path": path}

    return None


def play_audio_raw(backend, pcm_data):
    """Play raw PCM audio (16-bit stereo 48kHz) using detected backend."""
    if not backend or not pcm_data:
        return False

    try:
        import tempfile
        fd, wav_path = tempfile.mkstemp(suffix='.wav')
        os.close(fd)

        with wave.open(wav_path, 'w') as w:
            w.setnchannels(2)
            w.setsampwidth(2)
            w.setframerate(48000)
            w.writeframes(pcm_data)

        if backend["type"] == "ffplay":
            proc = subprocess.Popen(
                [backend["path"], "-nodisp", "-autoexit", wav_path],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.wait(timeout=2)
        elif backend["type"] in ("paplay", "play"):
            proc = subprocess.Popen(
                [backend["path"], wav_path],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.wait(timeout=2)
        elif backend["type"] == "cat":
            with open("/dev/dsp", "wb") as dsp:
                dsp.write(pcm_data)

        try:
            os.unlink(wav_path)
        except OSError:
            pass

        return True
    except Exception:
        return False


# ─── Config Persistence ─────────────────────────────────────────────────────

def load_config():
    """Load settings from config file."""
    defaults = {
        "volume": DEFAULT_VOLUME,
        "top_n": DEFAULT_TOP_N,
        "clip_duration": DEFAULT_CLIP_DURATION,
        "auto_scan_interval": DEFAULT_AUTO_SCAN_INTERVAL,
        "selected_bands": [],  # List of band names to display (empty = all)
        "crt_effects": None,   # CRT settings dict (or None for defaults)
    }
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                saved = json.load(f)
                defaults.update(saved)
    except (json.JSONDecodeError, IOError):
        pass
    return defaults


def save_config(config):
    """Save settings to config file."""
    try:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)
    except IOError as e:
        print(f"WARNING: Could not save config: {e}", file=sys.stderr)


# ─── Database ───────────────────────────────────────────────────────────────

def init_db(conn):
    """Create database tables and migrate schema if needed."""
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            device TEXT,
            scan_type TEXT DEFAULT 'band',  -- 'band' or 'full'
            notes TEXT DEFAULT ''
        )
    """)
    # Migration: add scan_type column if it doesn't exist (old DB schema)
    try:
        conn.execute("ALTER TABLE scans ADD COLUMN scan_type TEXT DEFAULT 'band'")
    except sqlite3.OperationalError:
        pass  # Column already exists

    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER NOT NULL REFERENCES scans(id),
            band_name TEXT NOT NULL,
            frequency_hz INTEGER NOT NULL,
            level_low INTEGER NOT NULL DEFAULT 0,
            level_high INTEGER NOT NULL DEFAULT 0,
            noise_floor INTEGER NOT NULL DEFAULT 0,
            signal_gain INTEGER NOT NULL DEFAULT 0,
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
    conn.execute("CREATE INDEX IF NOT EXISTS idx_signals_freq ON signals(frequency_hz)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_signals_scan ON signals(scan_id)")


def seed_db(conn):
    """Seed known frequencies."""
    try:
        for freq_hz, desc, band in KNOWN_FREQS:
            conn.execute(
                "INSERT OR IGNORE INTO known_frequencies (frequency_hz, description, band_hint) VALUES (?, ?, ?)",
                (freq_hz, desc, band)
            )
    except sqlite3.OperationalError:
        pass  # DB locked or already seeded


def get_signals_for_bands(conn, selected_bands, top_n):
    """Get signals filtered by selected bands."""
    if not selected_bands:
        # Show all bands - get top N from latest scan
        query = """
            SELECT frequency_hz, band_name, signal_gain, level_high, demodulator, label
            FROM signals
            WHERE scan_id = (SELECT MAX(id) FROM scans)
            ORDER BY signal_gain DESC, level_high DESC
            LIMIT ?
        """
        return conn.execute(query, (top_n,)).fetchall()
    else:
        # Filter by selected bands
        placeholders = ','.join(['?' for _ in selected_bands])
        query = f"""
            SELECT frequency_hz, band_name, signal_gain, level_high, demodulator, label
            FROM signals
            WHERE scan_id = (SELECT MAX(id) FROM scans)
              AND band_name IN ({placeholders})
            ORDER BY signal_gain DESC, level_high DESC
            LIMIT ?
        """
        return conn.execute(query, selected_bands + [top_n]).fetchall()


# ─── SDR Backend (Device-Agnostic via SDRconnect) ──────────────────────────

class SDRBackend:
    """Thread-safe wrapper around SDRconnect WebSocket API."""

    # Known device frequency ranges (fallback if not queryable)
    DEVICE_RANGES = {
        "RSP1A": (0.005e6, 2.0e9),      # 5 kHz - 2 GHz
        "RSP1": (0.005e6, 2.0e9),       # Same as RSP1A
        "RTL-SDR": (24e6, 1766e6),      # RTL2832U typical range
        "default": (0.5e6, 1.7e9),      # Conservative default
    }

    def __init__(self):
        self.ws = None
        self.lock = threading.Lock()
        self.connected = False
        self.device_name = "Unknown"
        self.device_type = ""
        self.freq_range = (0.5e6, 1.7e9)  # Default range
        self.playing = False
        self.recording = False
        self.current_freq = 0
        self._stop_event = threading.Event()

    def connect(self):
        """Connect to SDRconnect headless and detect device capabilities."""
        try:
            self.ws = websocket.create_connection(WS_URL, timeout=5)
            time.sleep(0.3)

            # Get device name
            resp = self._get_prop("active_device")
            if resp:
                self.device_name = str(resp)
                self._detect_device_type()

            can_ctrl = self._get_prop("can_control")
            if can_ctrl != "true":
                self._send("device_stream_enable", "", "true")
                time.sleep(1.5)
                for _ in range(10):
                    texts, _ = self._recv_all(0.5)
                    if not texts:
                        break

            can_ctrl = None
            for attempt in range(3):
                can_ctrl = self._get_prop("can_control")
                if can_ctrl is not None:
                    break
                time.sleep(0.5)

            if can_ctrl is None:
                print("WARNING: Could not verify can_control, assuming connected", file=sys.stderr)
                self.connected = True
                return True

            self.connected = (can_ctrl == "true")
            return self.connected
        except Exception as e:
            print(f"SDR connect error: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            return False

    def _detect_device_type(self):
        """Detect device type and set frequency range."""
        name = self.device_name.upper()
        for dev, (low, high) in self.DEVICE_RANGES.items():
            if dev in name:
                self.device_type = dev
                self.freq_range = (low, high)
                print(f"Detected {dev}: {low/1e6:.1f} - {high/1e6:.0f} MHz", file=sys.stderr)
                return

        # Default detection
        self.device_type = "default"
        print(f"Unknown device '{self.device_name}', using default range", file=sys.stderr)

    def disconnect(self):
        """Close WebSocket connection."""
        self._stop_event.set()
        if self.ws:
            try:
                self.ws.close()
            except Exception:
                pass
            self.ws = None
        self.connected = False

    def _send(self, event_type, prop="", val=""):
        """Send a WebSocket message."""
        with self.lock:
            if self.ws and not self._stop_event.is_set():
                self.ws.send(json.dumps({
                    "event_type": event_type,
                    "property": prop,
                    "value": str(val)
                }))

    def _recv_all(self, timeout=0.15):
        """Receive all pending messages."""
        texts = []
        binary_data = b''
        with self.lock:
            if not self.ws or self._stop_event.is_set():
                return texts, binary_data
            self.ws.settimeout(timeout)
            start = time.time()
            while time.time() - start < timeout:
                try:
                    msg = self.ws.recv()
                    if isinstance(msg, str):
                        texts.append(json.loads(msg))
                    else:
                        binary_data += msg
                except websocket.WebSocketTimeoutException:
                    break
                except Exception:
                    break
        return texts, binary_data

    def _get_prop(self, prop):
        """Get a device property - drains stale messages first."""
        self._recv_all(0.2)
        self._send("get_property", prop)
        texts, _ = self._recv_all(1.0)
        for t in texts:
            if t.get("event_type") == "get_property_response" and t.get("property") == prop:
                return t.get("value", "")

        # Retry once more (stream flooding protection)
        self._recv_all(0.3)
        self._send("get_property", prop)
        texts, _ = self._recv_all(1.5)
        for t in texts:
            if t.get("event_type") == "get_property_response" and t.get("property") == prop:
                return t.get("value", "")

        return None

    def spectrum_peak(self, binary_data):
        """Extract peak level from spectrum data."""
        if len(binary_data) < 2:
            return 0
        payload_type = struct.unpack_from("<H", binary_data, 0)[0]
        if payload_type == 3:
            return max(binary_data[2:]) if len(binary_data) > 2 else 0
        return 0

    def tune(self, freq_hz, demodulator="AM"):
        """Tune to a frequency with specified demodulator."""
        self._send("set_property", "device_center_frequency", str(int(freq_hz)))
        time.sleep(0.1)
        self._send("set_property", "demodulator", demodulator)
        time.sleep(0.1)
        self.current_freq = freq_hz

    def start_audio_stream(self):
        """Start audio streaming from SDR."""
        self._send("set_property", "audio_volume_percent", "100")  # Device volume (software handles gain)
        self._send("set_property", "audio_mute", "false")
        self._recv_all(0.3)
        self._send("audio_stream_enable", "", "true")
        time.sleep(0.5)
        self.playing = True

    def stop_audio_stream(self):
        """Stop audio streaming."""
        self._send("audio_stream_enable", "", "false")
        self.playing = False

    def capture_audio_chunk(self, duration=1.0):
        """Capture audio for specified duration. Returns raw PCM bytes."""
        chunks = []
        start = time.time()
        while time.time() - start < duration:
            _, binary = self._recv_all(0.2)
            if binary and len(binary) >= 2:
                payload_type = struct.unpack_from("<H", binary, 0)[0]
                if payload_type == 1:
                    chunks.append(binary[2:])
        return b''.join(chunks)

    def scan_frequency(self, freq_hz, demod="AM"):
        """Scan a single frequency and return peak level."""
        self._send("set_property", "device_center_frequency", str(int(freq_hz)))
        time.sleep(0.03)
        self._send("spectrum_enable", "", "true")
        time.sleep(0.08)
        _, binary = self._recv_all(0.12)
        level = self.spectrum_peak(binary)
        self._send("spectrum_enable", "", "false")
        return level

    def scan_band(self, band_name, freq_start, freq_end, step, demod):
        """Scan a frequency band and return list of (freq, level)."""
        self._send("set_property", "demodulator", demod)
        time.sleep(0.2)
        self._recv_all(0.3)

        signals = []
        freq = int(freq_start)
        while freq <= int(freq_end):
            level = self.scan_frequency(freq, demod)
            if level > 50:  # Basic noise threshold
                signals.append((freq, level))
            freq += step

        return signals


# ─── CRT TUI Renderer ──────────────────────────────────────────────────────

class RetroTUI:
    """CRT-style curses interface with visual effects engine."""

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sdr = SDRBackend()
        self.backend = detect_audio_backend()
        self.stations = []       # List of (freq_hz, band_name, gain, level, demod, label)
        self.selected_idx = 0

        # Load persistent config or use defaults
        cfg = load_config()
        self.volume = cfg.get("volume", DEFAULT_VOLUME)
        self.top_n = cfg.get("top_n", DEFAULT_TOP_N)
        self.clip_duration = cfg.get("clip_duration", DEFAULT_CLIP_DURATION)
        self.auto_scan_interval = cfg.get("auto_scan_interval", DEFAULT_AUTO_SCAN_INTERVAL)
        self.selected_bands = cfg.get("selected_bands", [])  # Empty = show all

        # CRT effects setup
        self.crt_cfg = CRTConfig()
        if cfg.get("crt_effects"):
            self.crt_cfg.from_dict(cfg["crt_effects"])

        self.crt_engine = CRTEngine(self.crt_cfg)

        self.is_playing = False
        self.is_recording = False
        self.scanning = False
        self.scan_progress = ""
        self.last_scan_time = None
        self.next_auto_scan = None
        self.status_msg = ""
        self.status_time = 0
        self.play_proc = None
        self.db_lock = threading.Lock()

        # Settings menu state
        self._settings_mode = False
        self._settings_cursor = 0

        # Database setup
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        os.makedirs(RECORD_DIR, exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        init_db(self.conn)
        seed_db(self.conn)

        # UI state
        self._init_colors()
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.timeout(200)

    def _save_settings(self):
        """Save current settings to config file."""
        save_config({
            "volume": self.volume,
            "top_n": self.top_n,
            "clip_duration": self.clip_duration,
            "auto_scan_interval": self.auto_scan_interval,
            "selected_bands": self.selected_bands,
            "crt_effects": self.crt_cfg.to_dict(),
        })

    def _init_colors(self):
        """Initialize curses color pairs for CRT themes."""
        curses.start_color()
        curses.use_default_colors()
        # Initialize base pairs (fallback)
        curses.init_pair(1, curses.COLOR_BLACK, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_GREEN, -1)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)
        curses.init_pair(5, curses.COLOR_RED, -1)
        curses.init_pair(6, curses.COLOR_GREEN, -1)

    def _clr(self, pair_num):
        """Get color attribute for legacy pairs."""
        return curses.color_pair(pair_num)

    def _tpair(self, key, bg=None):
        """Get theme-aware color pair attribute."""
        try:
            return theme_pair(self.crt_cfg.theme, key, bg)
        except Exception:
            # Fallback to green if theme fails
            return curses.color_pair(2)

    def _dim(self, text, max_width):
        """Truncate text with ellipsis if needed."""
        if len(text) > max_width:
            return text[:max_width - 1] + "\u2026"
        return text.ljust(max_width)

    def _bar(self, value, max_val, width=8):
        """Render signal strength bar with block characters."""
        filled = int((value / max(1, max_val)) * width)
        # Use theme-appropriate characters
        if self.crt_cfg.theme == "synthwave":
            return "[" + "\u2588" * filled + "\u2591" * (width - filled) + "]"
        return "[" + "\u2588" * filled + "\u2591" * (width - filled) + "]"

    def _apply_crt_effects(self):
        """Apply CRT visual effects overlay to the screen."""
        h, w = self.stdscr.getmaxyx()
        flicker_attr = self.crt_engine.get_flicker_attr()
        noise_chars = THEMES[self.crt_cfg.theme]["noise_ch"]

        # Apply phosphor glow background
        if self.crt_cfg.phosphor_glow:
            try:
                bg_attr = theme_pair(self.crt_cfg.theme, "glow")
                self.stdscr.bkgd(" ", bg_attr)
            except curses.error:
                pass

        # Overlay effects on each row
        for row in range(h):
            is_scanline = self.crt_engine.scanline_dim(row)
            smear = self.crt_engine.smear_active()

            for col in range(w - 1):
                # Check vignette first (corners/edges)
                if self.crt_engine.vignette_dim(row, col, h, w):
                    try:
                        self.stdscr.addch(row, col, " ",
                                        theme_pair(self.crt_cfg.theme, "glow") | curses.A_DIM)
                    except curses.error:
                        pass
                    continue

                # Check static noise
                if self.crt_engine.should_noise(row, col):
                    try:
                        ch = random.choice(noise_chars)
                        self.stdscr.addch(row, col, ch,
                                        theme_pair(self.crt_cfg.theme, "dim") | curses.A_DIM | flicker_attr)
                    except curses.error:
                        pass
                    continue

                # Apply scanline dimming
                if is_scanline:
                    try:
                        existing = self.stdscr.inch(row, col) & 0xFF
                        if existing and chr(existing).strip():
                            self.stdscr.addch(row, col, chr(existing),
                                            theme_pair(self.crt_cfg.theme, "dim") | curses.A_DIM | flicker_attr)
                    except curses.error:
                        pass

    def _draw_header(self):
        """Draw the retro CRT header."""
        h, w = self.stdscr.getmaxyx()

        try:
            border_attr = theme_pair(self.crt_cfg.theme, "bright") | curses.A_BOLD
            self.stdscr.addnstr(0, 0, "\u256d" + "\u2500" * (w - 2) + "\u256f", w - 1, border_attr)
        except curses.error:
            pass

        # Device info line
        dev_str = f"{self.sdr.device_name}" if self.sdr.connected else "DISCONNECTED"
        range_str = f"{self.sdr.freq_range[0]/1e6:.1f}-{self.sdr.freq_range[1]/1e6:.0f} MHz"
        title_line = f"\u2502 GALAXY SDR | {dev_str:<25} | Range: {range_str}"

        try:
            self.stdscr.addnstr(1, 0, title_line.ljust(w - 1), w - 1, curses.A_BOLD | theme_pair(self.crt_cfg.theme, "bright"))
        except curses.error:
            pass

        # Status row
        scan_status = "SCANNING..." if self.scanning else ("AUTO-SCAN ON" if self.auto_scan_interval > 0 else "MANUAL")
        rec_str = "\u25cf REC" if self.is_recording else "REC OFF"
        play_str = "\u25b6 PLAYING" if self.is_playing else "\u25a0 STOPPED"

        band_filter = f"Bands: {len(self.selected_bands)} selected" if self.selected_bands else "Bands: ALL"
        status_line = f"\u2502 {play_str} | {rec_str} | {scan_status} | VOL: {self.volume}% | {band_filter}"
        if self.scan_progress:
            status_line += f" | {self.scan_progress}"

        try:
            rec_attr = theme_pair(self.crt_cfg.theme, "bright") if self.is_recording else theme_pair(self.crt_cfg.theme, "fg")
            play_attr = theme_pair(self.crt_cfg.theme, "fg") if self.is_playing else theme_pair(self.crt_cfg.theme, "dim")
            self.stdscr.addnstr(2, 0, f"\u2502 {self._dim(status_line, w - 3)}", w - 1, rec_attr | curses.A_BOLD)
        except curses.error:
            pass

        try:
            self.stdscr.addnstr(3, 0, "\u2564" + "\u2500" * (w - 2) + "\u2565", w - 1, theme_pair(self.crt_cfg.theme, "bright"))
        except curses.error:
            pass

    def _draw_station_list(self):
        """Draw the station list with CRT effects."""
        h, w = self.stdscr.getmaxyx()
        start_row = 4

        # Column headers
        header = f"\u2502 {'#':>3} {'FREQ(MHz)':>10} {'LABEL':<25} {'STR':>8} {'BAND':<18} {'DEMOD':<5}"
        try:
            self.stdscr.addnstr(start_row, 0, header.ljust(w - 1), w - 1, curses.A_BOLD | theme_pair(self.crt_cfg.theme, "bright"))
        except curses.error:
            pass

        try:
            self.stdscr.addnstr(start_row + 1, 0, "\u256d" + "\u2500" * (w - 2) + "\u256f", w - 1, theme_pair(self.crt_cfg.theme, "dim"))
        except curses.error:
            pass

        # Station rows
        max_rows = h - start_row - 5
        if max_rows < 1:
            return

        total = len(self.stations)
        view_start = max(0, min(self.selected_idx - max_rows // 2, total - max_rows))

        for i in range(max_rows):
            idx = view_start + i
            row = start_row + 2 + i

            if idx >= total:
                break

            freq_hz, band_name, gain, level, demod, label = self.stations[idx]
            freq_mhz = freq_hz / 1e6

            arrow = "\u25b8" if idx == self.selected_idx else " "
            bar = self._bar(level, 255, 8)
            lbl = label[:24] if label else band_name[:24]

            line = f"\u2502 {arrow} {idx + 1:>3} {freq_mhz:10.3f} {lbl:<25} {bar} {band_name[:17]:<18} {demod:<5}"

            if idx == self.selected_idx:
                attr = curses.A_REVERSE | theme_pair(self.crt_cfg.theme, "bright")
            else:
                attr = theme_pair(self.crt_cfg.theme, "fg")

            try:
                self.stdscr.addnstr(row, 0, line.ljust(w - 1), w - 1, attr)
            except curses.error:
                pass

        footer_row = start_row + 2 + max_rows
        if footer_row < h - 3:
            try:
                self.stdscr.addnstr(footer_row, 0, "\u2564" + "\u2500" * (w - 2) + "\u2565", w - 1, theme_pair(self.crt_cfg.theme, "bright"))
            except curses.error:
                pass

    def _draw_footer(self):
        """Draw the control footer."""
        h, w = self.stdscr.getmaxyx()

        if self.stations and 0 <= self.selected_idx < len(self.stations):
            freq_hz, band_name, gain, level, demod, label = self.stations[self.selected_idx]
            freq_mhz = freq_hz / 1e6
            info = f"\u2502 TUNED: {freq_mhz:.3f} MHz | Top-{self.top_n} | Clip: {self.clip_duration}s | Auto-scan: {self.auto_scan_interval}s"
        else:
            info = f"\u2502 No stations loaded. Press S to scan selected bands, F for full device scan."

        try:
            self.stdscr.addnstr(h - 3, 0, info.ljust(w - 1), w - 1, theme_pair(self.crt_cfg.theme, "dim"))
        except curses.error:
            pass

        controls = "\u2502 \u2191\u2193=navigate \u2190\u2192=prev/next SPACE=play/pause R=record S=band-scan F=full-scan B=bands T=crt +/-=vol N=top-N D=clip A=auto Q=quit"
        try:
            self.stdscr.addnstr(h - 2, 0, controls.ljust(w - 1), w - 1, curses.A_DIM | theme_pair(self.crt_cfg.theme, "dim"))
        except curses.error:
            pass

        if self.status_msg and time.time() - self.status_time < 3:
            try:
                self.stdscr.addnstr(h - 1, 0, f"\u2502 {self._dim(self.status_msg, w - 3)}", w - 1, theme_pair(self.crt_cfg.theme, "bright") | curses.A_BOLD)
            except curses.error:
                pass

        try:
            self.stdscr.addnstr(h - 1, 0, "\u2570" + "\u2500" * (w - 2) + "\u256f", w - 1, theme_pair(self.crt_cfg.theme, "bright"))
        except curses.error:
            pass

    def _status(self, msg):
        """Show a temporary status message."""
        self.status_msg = msg
        self.status_time = time.time()

    def refresh_stations(self):
        """Reload station list from database with band filtering."""
        with self.db_lock:
            raw = get_signals_for_bands(self.conn, self.selected_bands, self.top_n)
        self.stations = [(r[0], r[1], r[2], r[3], r[4], r[5]) for r in raw]

    def _run_band_scan(self):
        """Scan selected bands (or all if none selected)."""
        if not self.sdr.connected:
            self._status("ERROR: SDR not connected")
            return

        self.scanning = True
        bands_to_scan = [b for b in BANDS_DB if not self.selected_bands or b[0] in self.selected_bands]
        if not bands_to_scan:
            bands_to_scan = BANDS_DB  # Default to all

        with self.db_lock:
            timestamp = datetime.now().isoformat()
            self.conn.execute(
                "INSERT INTO scans (timestamp, device, scan_type) VALUES (?, ?, ?)",
                (timestamp, self.sdr.device_name, "band")
            )
            scan_id = self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        total_signals = 0
        for i, (name, start, end, step, demod, desc) in enumerate(bands_to_scan):
            self.scan_progress = f"Scanning {name} ({i+1}/{len(bands_to_scan)})"
            signals = self.sdr.scan_band(name, start, end, step, demod)

            with self.db_lock:
                for freq, level in signals:
                    # Look up label
                    cursor = self.conn.execute(
                        "SELECT description FROM known_frequencies WHERE ABS(frequency_hz - ?) <= ?",
                        (freq, step // 2)
                    )
                    row = cursor.fetchone()
                    label = row[0] if row else ""

                    self.conn.execute("""
                        INSERT INTO signals (scan_id, band_name, frequency_hz, level_low, level_high,
                                           noise_floor, signal_gain, demodulator, label)
                        VALUES (?, ?, ?, 0, ?, 0, 0, ?, ?)
                    """, (scan_id, name, freq, level, demod, label))

                total_signals += len(signals)
                self.conn.commit()

        with self.db_lock:
            self.last_scan_time = datetime.now()
            if self.auto_scan_interval > 0:
                self.next_auto_scan = self.last_scan_time.timestamp() + self.auto_scan_interval

        self.scanning = False
        self.scan_progress = ""
        self.refresh_stations()
        self._status(f"Band scan complete: {total_signals} signals found")

    def _run_full_scan(self):
        """Full device range scan at multiple gain levels."""
        if not self.sdr.connected:
            self._status("ERROR: SDR not connected")
            return

        self.scanning = True
        freq_low, freq_high = self.sdr.freq_range

        # Adaptive step size based on range
        total_range = freq_high - freq_low
        if total_range > 1e9:  # Over 1 GHz range
            step = 500_000  # 500 kHz steps for wide scan
        elif total_range > 100e6:  # Over 100 MHz
            step = 100_000   # 100 kHz steps
        else:
            step = 25_000    # 25 kHz fine steps

        with self.db_lock:
            timestamp = datetime.now().isoformat()
            self.conn.execute(
                "INSERT INTO scans (timestamp, device, scan_type) VALUES (?, ?, ?)",
                (timestamp, self.sdr.device_name, "full")
            )
            scan_id = self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        # Scan at two gain levels for signal discrimination
        total_signals = 0
        freq = int(freq_low)
        while freq <= int(freq_high):
            progress_pct = (freq - freq_low) / (freq_high - freq_low) * 100
            self.scan_progress = f"Full scan: {progress_pct:.0f}% ({freq/1e6:.1f} MHz)"

            # Quick spectrum check
            level = self.sdr.scan_frequency(freq, "AM")

            if level > 80:  # Signal threshold for full scan
                with self.db_lock:
                    # Determine best band match
                    best_band = "Unknown"
                    best_demod = "AM"
                    for name, start, end, step_s, demod, desc in BANDS_DB:
                        if start <= freq <= end:
                            best_band = name
                            best_demod = demod
                            break

                    # Look up label
                    cursor = self.conn.execute(
                        "SELECT description FROM known_frequencies WHERE ABS(frequency_hz - ?) <= 100000",
                        (freq,)
                    )
                    row = cursor.fetchone()
                    label = row[0] if row else ""

                    self.conn.execute("""
                        INSERT INTO signals (scan_id, band_name, frequency_hz, level_low, level_high,
                                           noise_floor, signal_gain, demodulator, label)
                        VALUES (?, ?, ?, 0, ?, 0, 0, ?, ?)
                    """, (scan_id, best_band, freq, level, best_demod, label))

                    total_signals += 1
                    if total_signals % 50 == 0:
                        self.conn.commit()

            freq += step

        with self.db_lock:
            self.conn.commit()
            self.last_scan_time = datetime.now()

        self.scanning = False
        self.scan_progress = ""
        self.refresh_stations()
        self._status(f"Full scan complete: {total_signals} signals found across {freq_low/1e6:.0f}-{freq_high/1e6:.0f} MHz")

    def _show_band_menu(self):
        """Show band selection menu."""
        h, w = self.stdscr.getmaxyx()
        menu_win = curses.newwin(h - 4, min(w - 2, 80), 4, max(1, (w - 78) // 2))
        menu_win.box()

        title = " Band Selection (Space=toggle, Enter/Escape=done)"
        try:
            menu_win.addstr(0, 2, title, curses.A_BOLD | theme_pair(self.crt_cfg.theme, "bright"))
        except curses.error:
            pass

        # Draw bands with selection state
        for i, (name, start, end, step, demod, desc) in enumerate(BANDS_DB):
            row = i + 2
            if row >= h - 5:
                break

            checked = "\u2713" if name in self.selected_bands else " "
            freq_str = f"{start/1e6:.3f}-{end/1e6:.3f} MHz [{demod}]"
            line = f"[{checked}] {name:<25} {freq_str}"

            try:
                menu_win.addstr(row, 2, line[:min(w - 4, len(line))])
            except curses.error:
                pass

        menu_win.refresh()

        # Handle input in menu
        menu_win.nodelay(True)
        done = False
        while not done:
            key = menu_win.getch()
            if key == ord('\n') or key == 27 or key == ord('q'):  # Enter, Escape, Q
                done = True
            elif key == ord(' ') and i < len(BANDS_DB):
                name = BANDS_DB[i][0]
                if name in self.selected_bands:
                    self.selected_bands.remove(name)
                else:
                    self.selected_bands.append(name)

                # Redraw menu
                menu_win.erase()
                menu_win.box()
                try:
                    menu_win.addstr(0, 2, title, curses.A_BOLD | theme_pair(self.crt_cfg.theme, "bright"))
                except curses.error:
                    pass

                for j, (bn, bs, be, bst, bd, bdesc) in enumerate(BANDS_DB):
                    r = j + 2
                    if r >= h - 5:
                        break
                    ch = "\u2713" if bn in self.selected_bands else " "
                    fs = f"{bs/1e6:.3f}-{be/1e6:.3f} MHz [{bd}]"
                    ln = f"[{ch}] {bn:<25} {fs}"
                    try:
                        menu_win.addstr(r, 2, ln[:min(w - 4, len(ln))])
                    except curses.error:
                        pass
                menu_win.refresh()

        # Refresh main display after band selection
        self.refresh_stations()
        if self.selected_bands:
            self._status(f"Showing {len(self.selected_bands)} selected bands")
        else:
            self._status("Showing all bands")

    def _show_crt_settings_menu(self):
        """Show CRT settings overlay menu."""
        h, w = self.stdscr.getmaxyx()

        # Draw the main UI first (dimmed)
        self.stdscr.erase()
        self._draw_header()
        self._draw_station_list()
        self._draw_footer()

        # Show settings overlay
        draw_settings_menu(self.stdscr, self.crt_cfg, self._settings_cursor)
        self.stdscr.refresh()

        # Handle input in settings menu
        done = False
        while not done:
            key = self.stdscr.getch()
            if key == -1:
                time.sleep(0.1)
                continue

            new_cursor, should_close = handle_settings_input(key, self.crt_cfg, self._settings_cursor)
            self._settings_cursor = new_cursor

            if should_close:
                done = True
            else:
                # Redraw with updated settings
                self.stdscr.erase()
                self._draw_header()
                self._draw_station_list()
                self._draw_footer()
                draw_settings_menu(self.stdscr, self.crt_cfg, self._settings_cursor)
                self.stdscr.refresh()

        self._status("CRT settings updated")

    def _play_current_station(self):
        """Start playing the currently selected station."""
        if not self.stations or not self.sdr.connected:
            return

        freq_hz, _, _, _, demod, _ = self.stations[self.selected_idx]
        self.sdr.tune(freq_hz, demod)

        # Set volume on SDR device (0-100%)
        self.sdr._send("set_property", "audio_volume_percent", str(self.volume))
        time.sleep(0.1)

        self.sdr.start_audio_stream()
        self.is_playing = True
        self._status(f"Playing {freq_hz / 1e6:.3f} MHz ({demod}) @ {self.volume}% vol")

    def _stop_playback(self):
        """Stop audio playback."""
        self.sdr.stop_audio_stream()
        if self.play_proc:
            try:
                self.play_proc.terminate()
            except Exception:
                pass
            self.play_proc = None
        self.is_playing = False

    def _handle_input(self, key):
        """Process keyboard input."""
        if key == ord('q') or key == ord('Q'):
            return False  # Quit signal

        elif key == curses.KEY_UP:
            if self.selected_idx > 0:
                self.selected_idx -= 1

        elif key == curses.KEY_DOWN:
            if self.selected_idx < len(self.stations) - 1:
                self.selected_idx += 1

        elif key == curses.KEY_LEFT:
            if self.stations:
                self.selected_idx = (self.selected_idx - 1) % len(self.stations)

        elif key == curses.KEY_RIGHT:
            if self.stations:
                self.selected_idx = (self.selected_idx + 1) % len(self.stations)

        elif key == ord(' ') or key == 32:
            # Play/Pause toggle
            if self.is_playing:
                self._stop_playback()
                self._status("Playback stopped")
            else:
                self._play_current_station()

        elif key == ord('r') or key == ord('R'):
            # Toggle recording
            self.is_recording = not self.is_recording
            if self.is_recording:
                self._status("Recording ON - clips will be saved for each station")
            else:
                self._status("Recording OFF")

        elif key == ord('s') or key == ord('S'):
            # Band scan (selected bands only)
            if not self.scanning:
                t = threading.Thread(target=self._run_band_scan, daemon=True)
                t.start()
                self._status("Band scan started...")

        elif key == ord('f') or key == ord('F'):
            # Full device scan
            if not self.scanning:
                t = threading.Thread(target=self._run_full_scan, daemon=True)
                t.start()
                self._status(f"Full scan started ({self.sdr.freq_range[0]/1e6:.0f}-{self.sdr.freq_range[1]/1e6:.0f} MHz)...")

        elif key == ord('b') or key == ord('B'):
            # Band selection menu
            self._show_band_menu()

        elif key == ord('t') or key == ord('T'):
            # CRT settings menu
            self._show_crt_settings_menu()

        elif key == ord('+') or key == '=' or key == ord('.'):
            # Volume up
            if self.volume < 100:
                self.volume += 5
                self.sdr._send("set_property", "audio_volume_percent", str(self.volume))
                self._status(f"Volume: {self.volume}%")

        elif key == ord('-') or key == ord(','):
            # Volume down
            if self.volume > 0:
                self.volume -= 5
                self.sdr._send("set_property", "audio_volume_percent", str(self.volume))
                self._status(f"Volume: {self.volume}%")

        elif key == ord('n') or key == ord('N'):
            # Set top-N (cycle through common values)
            options = [10, 20, 30, 50, 100]
            try:
                idx = options.index(self.top_n)
                self.top_n = options[(idx + 1) % len(options)]
            except ValueError:
                self.top_n = DEFAULT_TOP_N
            self.refresh_stations()
            self._status(f"Top-N set to {self.top_n}")

        elif key == ord('d') or key == ord('D'):
            # Set clip duration (cycle through common values)
            options = [10, 15, 30, 60]
            try:
                idx = options.index(self.clip_duration)
                self.clip_duration = options[(idx + 1) % len(options)]
            except ValueError:
                self.clip_duration = DEFAULT_CLIP_DURATION
            self._status(f"Clip duration set to {self.clip_duration}s")

        elif key == ord('a') or key == ord('A'):
            # Toggle auto-scan interval
            options = [0, 30, 60, 120, 300]
            try:
                idx = options.index(self.auto_scan_interval)
                self.auto_scan_interval = options[(idx + 1) % len(options)]
            except ValueError:
                self.auto_scan_interval = DEFAULT_AUTO_SCAN_INTERVAL

            if self.auto_scan_interval > 0 and self.last_scan_time:
                self.next_auto_scan = self.last_scan_time.timestamp() + self.auto_scan_interval
            else:
                self.next_auto_scan = None

            label = "OFF" if self.auto_scan_interval == 0 else f"{self.auto_scan_interval}s"
            self._status(f"Auto-scan interval: {label}")

        return True  # Continue running

    def run(self):
        """Main event loop."""
        # Boot animation
        boot_animation(self.stdscr, self.crt_cfg)

        # Connect to SDR
        self.stdscr.addstr(0, 0, "Connecting to SDRconnect headless...")
        self.stdscr.refresh()

        if not self.sdr.connect():
            curses.endwin()
            print("ERROR: Cannot connect to SDRconnect headless at", WS_URL)
            print("Make sure sdrconnect is running (sdrconnect --headless)")
            sys.exit(1)

        # Initial station load
        self.refresh_stations()

        if not self.stations:
            self._status("No signals in database. Press S to scan bands, F for full device scan.")
        else:
            self._status(f"Loaded {len(self.stations)} stations from last scan")

        running = True
        last_audio_play_time = 0

        while running:
            try:
                # Advance CRT effects frame
                self.crt_engine.tick()

                # Clear and redraw
                self.stdscr.erase()
                self._draw_header()
                self._draw_station_list()
                self._draw_footer()

                # Apply CRT visual effects overlay
                self._apply_crt_effects()

                self.stdscr.refresh()

                # Handle input
                key = self.stdscr.getch()
                if key != -1:
                    running = self._handle_input(key)

                # Auto-scan timer
                if (self.next_auto_scan and not self.scanning and
                        time.time() >= self.next_auto_scan):
                    t = threading.Thread(target=self._run_band_scan, daemon=True)
                    t.start()
                    self._status("Auto-scan triggered")

                # Continuous audio streaming while playing
                if self.is_playing and self.stations:
                    freq_hz, _, _, _, demod, _ = self.stations[self.selected_idx]

                    # Retune if frequency changed
                    if self.sdr.current_freq != freq_hz:
                        self.sdr.tune(freq_hz, demod)

                    # Capture and play audio chunks (every 500ms)
                    now = time.time()
                    if now - last_audio_play_time >= 0.5:
                        chunk = self.sdr.capture_audio_chunk(0.4)
                        if chunk and self.backend:
                            play_audio_raw(self.backend, chunk)

                    last_audio_play_time = now

            except KeyboardInterrupt:
                running = False
            except curses.error:
                pass  # Ignore curses errors from terminal resize

        # Cleanup - save settings before exiting
        self._stop_playback()
        self.sdr.disconnect()
        self.conn.close()
        self._save_settings()


def main():
    """Entry point."""
    if not sys.stdin.isatty() and os.environ.get('TERM') is None:
        print("ERROR: Must be run from an interactive terminal.", file=sys.stderr)
        print("Usage: python3 galaxy_sdr.py", file=sys.stderr)
        sys.exit(1)

    print("Galaxy SDR - Loading...", file=sys.stderr)

    backend = detect_audio_backend()
    if backend:
        print(f"Audio backend: {backend['type']} ({backend['path']})", file=sys.stderr)
    else:
        print("WARNING: No audio playback tool found. Playback will be disabled.", file=sys.stderr)

    try:
        curses.wrapper(lambda stdscr: RetroTUI(stdscr).run())
    except KeyboardInterrupt:
        pass  # Normal exit on Ctrl+C
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
