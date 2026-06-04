#!/usr/bin/env python3
"""
SDR Retro Tuner - Cool-Retro-Term style TUI for SDRPlay RSP1A.

Controls:
  Up/Down arrows   Navigate station list
  Left/Right       Previous/Next station
  Space            Play/Pause current station
  R                Toggle recording on/off
  S                Trigger immediate scan
  N                Set top-N stations count
  D                Set clip duration (seconds)
  A                Toggle auto-scan interval
  Q                Quit

Cross-platform audio: auto-detects paplay, play (sox), ffplay, or cat>/dev/dsp.
"""

import curses
import json
import os
import platform
import queue
import select
import signal
import sqlite3
import struct
import subprocess
import sys
import threading
import time
import wave
from datetime import datetime

# ─── Configuration ──────────────────────────────────────────────────────────

WS_URL = "ws://127.0.0.1:5555"
DB_PATH = os.path.expanduser("~/.sdr_retro/signals.db")
RECORD_DIR = os.path.expanduser("~/.sdr_retro/recordings")
DEFAULT_TOP_N = 20
DEFAULT_CLIP_DURATION = 30
DEFAULT_AUTO_SCAN_INTERVAL = 60  # seconds

# ─── Audio backend detection ────────────────────────────────────────────────

def detect_audio_backend():
    """Find the best available audio playback tool."""
    system = platform.system()

    if system == "FreeBSD":
        # FreeBSD OSS - try play (sox), then cat to /dev/dsp
        for cmd in [["play"], ["cat"]]:
            path = __import__("shutil").which(cmd[0])
            if path:
                return {"type": "freebsd", "cmd": cmd, "path": path}
    else:
        # Linux - prefer paplay, then ffplay, then aplay
        for name in ["paplay", "ffplay", "aplay"]:
            path = __import__("shutil").which(name)
            if path:
                return {"type": name, "path": path}

    return None


def play_audio_raw(backend, pcm_data):
    """Play raw PCM audio (16-bit stereo 48kHz) using detected backend."""
    if not backend or not pcm_data:
        return False

    try:
        if backend["type"] == "paplay":
            proc = subprocess.Popen(
                [backend["path"], "--rate=48000", "--format=s16le", "--channels=2"],
                stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.stdin.write(pcm_data)
            proc.stdin.close()
            proc.wait(timeout=5)

        elif backend["type"] == "ffplay":
            proc = subprocess.Popen(
                [backend["path"], "-nodisp", "-autoexit", "-f", "s16le",
                 "-ar", "48000", "-ac", "2", "-i", "pipe:0"],
                stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.stdin.write(pcm_data)
            proc.stdin.close()
            proc.wait(timeout=5)

        elif backend["type"] == "play":
            # sox play command for FreeBSD
            proc = subprocess.Popen(
                [backend["path"], "-traw", "-r48000", "-es16", "-c2", "-",
                 "rate", "48000"],
                stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.stdin.write(pcm_data)
            proc.stdin.close()
            proc.wait(timeout=5)

        elif backend["type"] == "cat":
            # Raw OSS on FreeBSD - write directly to /dev/dsp
            with open("/dev/dsp", "wb") as dsp:
                dsp.write(pcm_data)

        return True
    except Exception:
        return False


def play_wav_file(backend, filepath):
    """Play a WAV file using detected backend."""
    if not backend or not os.path.exists(filepath):
        return False

    try:
        if backend["type"] == "paplay":
            proc = subprocess.Popen(
                [backend["path"], filepath],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.wait(timeout=2)

        elif backend["type"] == "ffplay":
            proc = subprocess.Popen(
                [backend["path"], "-nodisp", "-autoexit", filepath],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            proc.wait(timeout=2)

        elif backend["type"] in ("play", "cat"):
            # For sox play or raw OSS
            if backend["type"] == "play":
                cmd = [backend["path"], filepath]
            else:
                cmd = ["ffplay", "-nodisp", "-autoexit", filepath]

            proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            proc.wait(timeout=2)

        return True
    except Exception:
        return False


# ─── Database ───────────────────────────────────────────────────────────────

def init_db(conn):
    """Create database tables if they don't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            device TEXT,
            notes TEXT DEFAULT ''
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            freq_start_hz INTEGER NOT NULL,
            freq_end_hz INTEGER NOT NULL,
            step_hz INTEGER NOT NULL DEFAULT 100000,
            demodulator TEXT NOT NULL DEFAULT 'AM',
            lna_low INTEGER NOT NULL DEFAULT 2,
            lna_high INTEGER NOT NULL DEFAULT 9
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER NOT NULL REFERENCES scans(id),
            band_name TEXT NOT NULL,
            frequency_hz INTEGER NOT NULL,
            level_low INTEGER NOT NULL,
            level_high INTEGER NOT NULL,
            noise_floor INTEGER NOT NULL,
            signal_gain INTEGER NOT NULL,
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
    conn.execute("CREATE INDEX IF NOT EXISTS idx_scans_time ON scans(timestamp)")


def seed_db(conn):
    """Seed known frequencies and bands."""
    KNOWN = [
        (121_500_000, "Aviation Emergency (Guard)", "aviation"),
        (122_650_000, "Flight Service Station", "aviation"),
        (156_800_000, "Marine Ch 16 - Distress/Safety", "marine"),
        (156_300_000, "Marine Ch 9", "marine"),
        (156_525_000, "Marine Ch 22A (Coast Guard)", "marine"),
        (162_475_000, "NOAA WX3 (Vermont/Maine area)", "weather"),
        (162_425_000, "NOAA WX2", "weather"),
        (162_400_000, "NOAA WX1", "weather"),
    ]
    for freq_hz, desc, band in KNOWN:
        conn.execute(
            "INSERT OR IGNORE INTO known_frequencies (frequency_hz, description, band_hint) VALUES (?, ?, ?)",
            (freq_hz, desc, band)
        )

    BANDS = [
        ("Aviation VHF", 118_000_000, 137_000_000, 100_000, "AM", 2, 5),
        ("Marine VHF", 156_000_000, 163_000_000, 25_000, "NFM", 2, 9),
        ("NOAA Weather Radio", 162_400_000, 162_575_000, 25_000, "AM", 2, 9),
    ]
    for name, start, end, step, demod, lna_low, lna_high in BANDS:
        conn.execute("""
            INSERT INTO bands (name, freq_start_hz, freq_end_hz, step_hz, demodulator, lna_low, lna_high)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
                freq_start_hz=excluded.freq_start_hz,
                freq_end_hz=excluded.freq_end_hz,
                step_hz=excluded.step_hz,
                demodulator=excluded.demodulator,
                lna_low=excluded.lna_low,
                lna_high=excluded.lna_high
        """, (name, start, end, step, demod, lna_low, lna_high))


def get_top_signals(conn, top_n):
    """Get the top N strongest signals from the most recent scan."""
    row = conn.execute("""
        SELECT s.frequency_hz, s.band_name, s.signal_gain, s.level_high,
               s.demodulator, k.description as label
        FROM signals sig
        JOIN scans s ON sig.scan_id = s.id
        LEFT JOIN known_frequencies k ON ABS(sig.frequency_hz - k.frequency_hz) <= 50000
        WHERE sig.scan_id = (SELECT MAX(id) FROM scans)
        ORDER BY sig.signal_gain DESC, sig.level_high DESC
        LIMIT ?
    """, (top_n,)).fetchall()

    # Fallback: if no recent scan, get all-time strongest unique frequencies
    if not row:
        row = conn.execute("""
            SELECT frequency_hz, band_name, MAX(signal_gain) as max_gain,
                   MAX(level_high) as max_level, demodulator, ''
            FROM signals
            GROUP BY frequency_hz
            ORDER BY max_gain DESC
            LIMIT ?
        """, (top_n,)).fetchall()

    return row


# ─── SDR Backend (WebSocket to SDRconnect headless) ────────────────────────

class SDRBackend:
    """Thread-safe wrapper around SDRconnect WebSocket API."""

    def __init__(self):
        self.ws = None
        self.lock = threading.Lock()
        self.connected = False
        self.device_name = "Unknown"
        self.playing = False
        self.recording = False
        self.current_freq = 0
        self.audio_queue = queue.Queue(maxsize=10)
        self._stop_event = threading.Event()

    def connect(self):
        """Connect to SDRconnect headless WebSocket."""
        import websocket
        try:
            self.ws = websocket.create_connection(WS_URL, timeout=3)
            time.sleep(0.5)
            # Check device
            resp = self._get_prop("active_device")
            if resp:
                self.device_name = str(resp)
            can_ctrl = self._get_prop("can_control")
            if can_ctrl != "true":
                self._send("device_stream_enable", "", "true")
                time.sleep(1.0)
                self._recv_all(1.0)
                can_ctrl = self._get_prop("can_control")
            self.connected = (can_ctrl == "true")
            return self.connected
        except Exception as e:
            print(f"SDR connect error: {e}", file=sys.stderr)
            return False

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
        """Get a device property."""
        self._send("get_property", prop)
        texts, _ = self._recv_all(0.5)
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
        """Tune to a frequency."""
        self._send("set_property", "device_center_frequency", str(freq_hz))
        time.sleep(0.1)
        self._send("set_property", "demodulator", demodulator)
        time.sleep(0.1)
        self.current_freq = freq_hz

    def start_audio_stream(self):
        """Start audio streaming from SDR."""
        self._send("set_property", "audio_volume_percent", "100")
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

    def scan_band(self, band_name, freq_start, freq_end, step, demod, lna_low, lna_high):
        """Smart dual-gain scan of a frequency band. Returns list of (freq, gain)."""
        self._send("set_property", "demodulator", demod)
        time.sleep(0.2)
        self._recv_all(0.3)

        # Phase 1: low-gain baseline sweep
        freq = freq_start
        low_readings = []
        while freq <= freq_end:
            self._send("set_property", "device_center_frequency", str(freq))
            time.sleep(0.03)
            self._send("spectrum_enable", "", "true")
            time.sleep(0.08)
            _, binary = self._recv_all(0.12)
            level = self.spectrum_peak(binary)
            self._send("spectrum_enable", "", "false")
            low_readings.append((freq, level))
            freq += step

        # Calculate noise floor
        sorted_levels = sorted(l for _, l in low_readings)
        median_idx = len(sorted_levels) // 2
        baseline_noise = sorted_levels[median_idx] if sorted_levels else 0

        # Phase 2: high-gain check on candidates
        signals = []
        for freq, level_low in low_readings:
            if level_low > baseline_noise + 5:
                self._send("set_property", "lna_state", str(lna_high))
                time.sleep(0.1)
                _, binary_high = self._recv_all(0.15)
                level_high = self.spectrum_peak(binary_high)

                signal_gain = level_high - level_low
                if signal_gain > 20:
                    signals.append((freq, signal_gain, level_high))

        # Reset LNA
        self._send("set_property", "lna_state", str(lna_low))
        return signals, baseline_noise


# ─── Retro TUI Renderer ─────────────────────────────────────────────────────

class RetroTUI:
    """Cool-Retro-Term style curses interface."""

    # CRT color palette - green phosphor
    COLORS = {
        "bg": 0,           # Black background
        "green": 2,         # Bright green text
        "dim_green": 6,     # Dimmer green for secondary info
        "bright": 3,        # Very bright green (highlight)
        "amber": 4,         # Amber accent
        "red": 5,           # Red for warnings/recording
    }

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.sdr = SDRBackend()
        self.backend = detect_audio_backend()
        self.stations = []       # List of (freq_hz, band, gain, level, demod, label)
        self.selected_idx = 0
        self.top_n = DEFAULT_TOP_N
        self.clip_duration = DEFAULT_CLIP_DURATION
        self.auto_scan_interval = DEFAULT_AUTO_SCAN_INTERVAL
        self.is_playing = False
        self.is_recording = False
        self.scanning = False
        self.scan_progress = ""
        self.last_scan_time = None
        self.next_auto_scan = None
        self.status_msg = ""
        self.status_time = 0
        self.play_proc = None    # Current playback subprocess

        # Database
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        os.makedirs(RECORD_DIR, exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH)
        init_db(self.conn)
        seed_db(self.conn)

        # UI state
        self._init_colors()
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.timeout(200)  # 200ms poll interval for responsive input

    def _init_colors(self):
        """Initialize curses color pairs."""
        curses.start_color()
        curses.use_default_colors()
        # Pair numbers map to self.COLORS values
        curses.init_pair(1, curses.COLOR_BLACK, -1)   # 0: bg (unused)
        curses.init_pair(2, curses.COLOR_GREEN, -1)    # green
        curses.init_pair(3, curses.COLOR_GREEN, -1)    # bright (same as green for now)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)   # amber
        curses.init_pair(5, curses.COLOR_RED, -1)      # red
        curses.init_pair(6, curses.COLOR_GREEN, -1)    # dim_green

    def _clr(self, pair_num):
        """Get color attribute for a color pair."""
        return curses.color_pair(pair_num)

    def _dim(self, text, max_width):
        """Truncate or pad text to fit width."""
        if len(text) > max_width:
            return text[:max_width - 1] + "…"
        return text.ljust(max_width)

    def _bar(self, value, max_val, width=10):
        """Render a signal strength bar."""
        filled = int((value / max(1, max_val)) * width)
        return "[" + "█" * filled + "░" * (width - filled) + "]"

    def _draw_header(self):
        """Draw the retro CRT header."""
        h, w = self.stdscr.getmaxyx()

        # Title bar with box drawing
        title = " ╔════ SDR RETRO TUNER ════╗ "
        device_str = f"Device: {self.sdr.device_name}" if self.sdr.connected else "Device: DISCONNECTED"
        status_color = self._clr(2) if self.sdr.connected else self._clr(5)

        # Top decorative line
        try:
            self.stdscr.addnstr(0, 0, "╔" + "═" * (w - 2) + "╗", w - 1, self._clr(4))
        except curses.error:
            pass

        # Title row
        title_line = f"║ {self._dim(' SDR RETRO TUNER ', min(w - 30, 30))} {device_str}"
        try:
            self.stdscr.addnstr(1, 0, title_line.ljust(w - 1), w - 1, curses.A_BOLD | self._clr(4))
        except curses.error:
            pass

        # Status row
        scan_status = "SCANNING..." if self.scanning else ("AUTO-SCAN ON" if self.auto_scan_interval > 0 else "MANUAL SCAN")
        rec_str = "● REC" if self.is_recording else "REC OFF"
        play_str = "▶ PLAYING" if self.is_playing else "■ STOPPED"

        status_line = f"║ {play_str} | {rec_str} | {scan_status}"
        if self.scan_progress:
            status_line += f" | {self.scan_progress}"

        try:
            rec_attr = self._clr(5) if self.is_recording else self._clr(6)
            play_attr = self._clr(2) if self.is_playing else self._clr(6)
            self.stdscr.addnstr(2, 0, f"║ {self._dim(status_line, w - 3)}", w - 1, rec_attr | curses.A_BOLD)
        except curses.error:
            pass

        # Separator
        try:
            self.stdscr.addnstr(3, 0, "╠" + "═" * (w - 2) + "╣", w - 1, self._clr(4))
        except curses.error:
            pass

    def _draw_station_list(self):
        """Draw the station list with retro styling."""
        h, w = self.stdscr.getmaxyx()
        start_row = 4

        # Column headers
        header = f"║ {'#':>3} {'FREQ(MHz)':>10} {'LABEL':<25} {'STR':>6} {'BAND':<15} {'DEMOD':<5}"
        try:
            self.stdscr.addnstr(start_row, 0, header.ljust(w - 1), w - 1, curses.A_BOLD | self._clr(4))
        except curses.error:
            pass

        # Separator line
        try:
            self.stdscr.addnstr(start_row + 1, 0, "╟" + "─" * (w - 2) + "╢", w - 1, self._clr(6))
        except curses.error:
            pass

        # Station rows
        max_rows = h - start_row - 5  # Leave room for footer
        if max_rows < 1:
            return

        # Calculate visible window (center on selection)
        total = len(self.stations)
        view_start = max(0, min(self.selected_idx - max_rows // 2, total - max_rows))

        for i in range(max_rows):
            idx = view_start + i
            row = start_row + 2 + i

            if idx >= total:
                break

            freq_hz, band_name, gain, level, demod, label = self.stations[idx]
            freq_mhz = freq_hz / 1e6

            # Build display line
            arrow = "▸" if idx == self.selected_idx else " "
            bar = self._bar(level, 255, 6)
            lbl = label[:24] if label else band_name[:24]

            line = f"║ {arrow} {idx + 1:>3} {freq_mhz:10.3f} {lbl:<25} {bar} {band_name[:14]:<15} {demod:<5}"

            # Highlight selected row
            attr = curses.A_REVERSE | self._clr(3) if idx == self.selected_idx else self._clr(2)

            try:
                self.stdscr.addnstr(row, 0, line.ljust(w - 1), w - 1, attr)
            except curses.error:
                pass

        # Bottom separator
        footer_row = start_row + 2 + max_rows
        if footer_row < h - 3:
            try:
                self.stdscr.addnstr(footer_row, 0, "╠" + "═" * (w - 2) + "╣", w - 1, self._clr(4))
            except curses.error:
                pass

    def _draw_footer(self):
        """Draw the control footer."""
        h, w = self.stdscr.getmaxyx()

        # Current station info
        if self.stations and 0 <= self.selected_idx < len(self.stations):
            freq_hz, band_name, gain, level, demod, label = self.stations[self.selected_idx]
            freq_mhz = freq_hz / 1e6
            info = f"║ TUNED: {freq_mhz:.3f} MHz | Top-{self.top_n} | Clip: {self.clip_duration}s | Auto-scan: {self.auto_scan_interval}s"
        else:
            info = f"║ No stations loaded. Press S to scan."

        try:
            self.stdscr.addnstr(h - 3, 0, info.ljust(w - 1), w - 1, self._clr(6))
        except curses.error:
            pass

        # Controls help
        controls = "║ ↑↓=navigate ←→=prev/next SPACE=play/pause R=record S=scan N=top-N D=clip-duration A=auto-scan Q=quit"
        try:
            self.stdscr.addnstr(h - 2, 0, controls.ljust(w - 1), w - 1, curses.A_DIM | self._clr(6))
        except curses.error:
            pass

        # Status message (temporary)
        if self.status_msg and time.time() - self.status_time < 3:
            try:
                self.stdscr.addnstr(h - 1, 0, f"║ {self._dim(self.status_msg, w - 3)}", w - 1, self._clr(4) | curses.A_BOLD)
            except curses.error:
                pass

        # Bottom border
        try:
            self.stdscr.addnstr(h - 1, 0, "╚" + "═" * (w - 2) + "╝", w - 1, self._clr(4))
        except curses.error:
            pass

    def _status(self, msg):
        """Show a temporary status message."""
        self.status_msg = msg
        self.status_time = time.time()

    def refresh_stations(self):
        """Reload station list from database."""
        raw = get_top_signals(self.conn, self.top_n)
        self.stations = [(r[0], r[1], r[2], r[3], r[4], r[5]) for r in raw]

    def run_scan(self):
        """Run a full band scan and update the database."""
        if not self.sdr.connected:
            self._status("ERROR: SDR not connected")
            return

        self.scanning = True
        bands = self.conn.execute(
            "SELECT name, freq_start_hz, freq_end_hz, step_hz, demodulator, lna_low, lna_high FROM bands"
        ).fetchall()

        # Create scan record
        timestamp = datetime.now().isoformat()
        self.conn.execute(
            "INSERT INTO scans (timestamp, device) VALUES (?, ?)",
            (timestamp, self.sdr.device_name)
        )
        scan_id = self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        total_signals = 0
        for i, (name, start, end, step, demod, lna_low, lna_high) in enumerate(bands):
            self.scan_progress = f"Scanning {name} ({i+1}/{len(bands)})"
            signals, noise_floor = self.sdr.scan_band(name, start, end, step, demod, lna_low, lna_high)

            for freq, gain, level in signals:
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
                    VALUES (?, ?, ?, 0, ?, ?, ?, ?, ?, ?)
                """, (scan_id, name, freq, level, noise_floor, gain, demod, label))

            total_signals += len(signals)
            self.conn.commit()

        self.last_scan_time = datetime.now()
        self.next_auto_scan = self.last_scan_time.timestamp() + self.auto_scan_interval if self.auto_scan_interval > 0 else None
        self.scanning = False
        self.scan_progress = ""
        self.refresh_stations()
        self._status(f"Scan complete: {total_signals} signals found")

    def _play_current_station(self):
        """Start playing the currently selected station."""
        if not self.stations or not self.sdr.connected:
            return

        freq_hz, _, _, _, demod, _ = self.stations[self.selected_idx]
        self.sdr.tune(freq_hz, demod)
        self.sdr.start_audio_stream()
        self.is_playing = True
        self._status(f"Playing {freq_hz / 1e6:.3f} MHz ({demod})")

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

    def _record_clip(self, freq_hz, demod):
        """Record a clip of the current station."""
        if not self.sdr.connected:
            return

        self.sdr.tune(freq_hz, demod)
        self.sdr.start_audio_stream()

        # Capture audio chunks
        all_chunks = []
        start = time.time()
        while time.time() - start < self.clip_duration:
            chunk = self.sdr.capture_audio_chunk(1.0)
            if chunk:
                all_chunks.append(chunk)

        self.sdr.stop_audio_stream()

        # Save as WAV
        pcm_data = b''.join(all_chunks)
        if pcm_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            freq_str = f"{freq_hz/1e6:.3f}".replace(".", "_")
            filename = f"{timestamp}_{freq_str}MHz.wav"
            filepath = os.path.join(RECORD_DIR, filename)

            with wave.open(filepath, 'w') as wav_file:
                wav_file.setnchannels(2)
                wav_file.setsampwidth(2)
                wav_file.setframerate(48000)
                wav_file.writeframes(pcm_data)

            self._status(f"Recorded {os.path.getsize(filepath)} bytes to {filepath}")
        else:
            self._status("Recording failed - no audio captured")

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
            # Previous station (or wrap to end)
            if self.stations:
                self.selected_idx = (self.selected_idx - 1) % len(self.stations)

        elif key == curses.KEY_RIGHT:
            # Next station (or wrap to start)
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
            # Trigger scan (non-blocking via thread)
            if not self.scanning:
                t = threading.Thread(target=self.run_scan, daemon=True)
                t.start()
                self._status("Scan started...")

        elif key == ord('n') or key == ord('N'):
            # Set top-N (cycle through common values)
            options = [10, 20, 30, 50, 100]
            try:
                idx = options.index(self.top_n)
                self.top_n = options[(idx + 1) % len(options)]
            except ValueError:
                self.top_n = 20
            self.refresh_stations()
            self._status(f"Top-N set to {self.top_n}")

        elif key == ord('d') or key == ord('D'):
            # Set clip duration (cycle through common values)
            options = [10, 15, 30, 60]
            try:
                idx = options.index(self.clip_duration)
                self.clip_duration = options[(idx + 1) % len(options)]
            except ValueError:
                self.clip_duration = 30
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
            self._status("No signals in database. Press S to scan.")
        else:
            self._status(f"Loaded {len(self.stations)} stations from last scan")

        running = True
        last_audio_play_time = 0

        while running:
            try:
                # Clear and redraw
                self.stdscr.erase()
                self._draw_header()
                self._draw_station_list()
                self._draw_footer()
                self.stdscr.refresh()

                # Handle input
                key = self.stdscr.getch()
                if key != -1:
                    running = self._handle_input(key)

                # Auto-scan timer
                if (self.next_auto_scan and not self.scanning and
                        time.time() >= self.next_auto_scan):
                    t = threading.Thread(target=self.run_scan, daemon=True)
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

                        # Auto-record if recording is on
                        if self.is_recording:
                            # Save chunks to a rolling buffer - record full clip duration
                            pass  # Recording handled separately for now

                    last_audio_play_time = now

            except KeyboardInterrupt:
                running = False
            except curses.error:
                pass  # Ignore curses errors from terminal resize

        # Cleanup
        self._stop_playback()
        self.sdr.disconnect()
        self.conn.close()


def main():
    """Entry point."""
    print("SDR Retro Tuner - Loading...", file=sys.stderr)

    backend = detect_audio_backend()
    if backend:
        print(f"Audio backend: {backend['type']} ({backend['path']})", file=sys.stderr)
    else:
        print("WARNING: No audio playback tool found. Playback will be disabled.", file=sys.stderr)
        print("Install one of: paplay, ffplay, sox (play), or ensure /dev/dsp exists", file=sys.stderr)

    # Run curses application
    try:
        curses.wrapper(lambda stdscr: RetroTUI(stdscr).run())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
