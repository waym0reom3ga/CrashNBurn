#!/usr/bin/env python3
"""
crt_effects.py — CRT visual effects engine for terminal UIs.

Extracted from crt_editor.py and adapted for Galaxy SDR.
Provides: scanlines, phosphor glow, static noise, flicker, vignette, scroll blur, boot animation.
Supports 5 color themes with xterm-256 palette conversion.

Dependencies: stdlib only (curses, time, random, math)
"""

import curses
import time
import random
import math
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# COLOR THEMES
# ─────────────────────────────────────────────────────────────────────────────

THEMES = {
    "phosphor_green": {
        "fg":       (0,   255, 70),
        "bg":       (0,   12,  0),
        "dim":      (0,   100, 20),
        "bright":   (120, 255, 120),
        "cursor_bg":(0,   200, 50),
        "status_bg":(0,   40,  0),
        "glow":     (0,   60,  10),
        "noise_ch":  "\u00b7\u2219 \u2591\u2592",
        "scanline_ch": "\u2500",
    },
    "amber": {
        "fg":       (255, 176, 0),
        "bg":       (18,  8,   0),
        "dim":      (120, 70,  0),
        "bright":   (255, 220, 80),
        "cursor_bg":(200, 140, 0),
        "status_bg":(40,  18,  0),
        "glow":     (50,  20,  0),
        "noise_ch":  "\u00b7\u2219 \u2591",
        "scanline_ch": "\u2500",
    },
    "blue": {
        "fg":       (80,  180, 255),
        "bg":       (0,   5,   20),
        "dim":      (20,  60,  120),
        "bright":   (160, 220, 255),
        "cursor_bg":(40,  120, 200),
        "status_bg":(0,   10,  40),
        "glow":     (0,   10,  40),
        "noise_ch":  "\u00b7\u2219 \u2591\u2592",
        "scanline_ch": "\u2500",
    },
    "white": {
        "fg":       (220, 220, 220),
        "bg":       (10,  10,  10),
        "dim":      (90,  90,  90),
        "bright":   (255, 255, 255),
        "cursor_bg":(180, 180, 180),
        "status_bg":(30,  30,  30),
        "glow":     (20,  20,  20),
        "noise_ch":  "\u00b7\u2219 \u2591",
        "scanline_ch": "\u2500",
    },
    "synthwave": {
        "fg":       (255, 100, 220),
        "bg":       (10,  0,   25),
        "dim":      (100, 30,  120),
        "bright":   (120, 255, 230),
        "cursor_bg":(180, 50,  200),
        "status_bg":(20,  0,   50),
        "glow":     (20,  0,   40),
        "noise_ch":  "\u00b7\u2219 \u2591\u2592\u2593",
        "scanline_ch": "\u2500",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# COLOR PAIR MANAGEMENT
# ─────────────────────────────────────────────────────────────────────────────

_next_pair = 1
_pair_cache: dict = {}


def reset_color_pairs():
    """Reset color pair cache (call when theme changes)."""
    global _next_pair, _pair_cache
    _next_pair = 1
    _pair_cache.clear()


def rgb_to_256(r: int, g: int, b: int) -> int:
    """Convert 0-255 RGB to nearest xterm-256 colour index."""
    if r == g == b:
        if r < 8:   return 16
        if r > 248: return 231
        return round((r - 8) / 247 * 23) + 232
    ri = round(r / 255 * 5)
    gi = round(g / 255 * 5)
    bi = round(b / 255 * 5)
    return 16 + 36 * ri + 6 * gi + bi


def alloc_pair(fg256: int, bg256: int) -> int:
    """Allocate or retrieve a curses color pair."""
    global _next_pair
    key = (fg256, bg256)
    if key not in _pair_cache:
        if _next_pair >= curses.COLOR_PAIRS:
            return 1
        curses.init_pair(_next_pair, fg256, bg256)
        _pair_cache[key] = _next_pair
        _next_pair += 1
    return _pair_cache[key]


def theme_pair(theme_name: str, key: str, bg_override: Optional[str] = None) -> int:
    """Get curses color pair attribute for a theme color key."""
    t = THEMES[theme_name]
    fg = rgb_to_256(*t[key])
    bg_col = bg_override if bg_override else "bg"
    bg = rgb_to_256(*t[bg_col])
    return curses.color_pair(alloc_pair(fg, bg))


# ─────────────────────────────────────────────────────────────────────────────
# CRT CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

class CRTConfig:
    """Runtime configuration for CRT effects."""

    def __init__(self):
        # CRT effects toggles
        self.scanlines = True
        self.scanline_intensity = 2      # 1=subtle 2=medium 3=heavy
        self.phosphor_glow = True
        self.static_noise = True
        self.noise_density = 0.015       # fraction of cells that flicker per frame
        self.flicker = True
        self.flicker_rate = 0.04         # probability of a flicker frame
        self.vignette = True
        self.scroll_blur = True          # brief "smear" on scroll
        self.boot_animation = True

        # Theme
        self.theme = "phosphor_green"

    def to_dict(self) -> dict:
        """Serialize config to dictionary for JSON storage."""
        return {
            "theme": self.theme,
            "scanlines": self.scanlines,
            "scanline_intensity": self.scanline_intensity,
            "phosphor_glow": self.phosphor_glow,
            "static_noise": self.static_noise,
            "noise_density": self.noise_density,
            "flicker": self.flicker,
            "flicker_rate": self.flicker_rate,
            "vignette": self.vignette,
            "scroll_blur": self.scroll_blur,
            "boot_animation": self.boot_animation,
        }

    def from_dict(self, data: dict):
        """Load config from dictionary (JSON)."""
        for key, val in data.items():
            if hasattr(self, key):
                setattr(self, key, val)


# ─────────────────────────────────────────────────────────────────────────────
# CRT EFFECT ENGINE
# ─────────────────────────────────────────────────────────────────────────────

class CRTEngine:
    """
    Renders CRT effects on top of terminal content using curses.
    All effects are character-cell approximations of CRT monitor behavior.
    """

    def __init__(self, cfg: CRTConfig):
        self.cfg = cfg
        self._frame = 0
        self._flicker_on = True
        self._scroll_smear = 0  # frames of scroll blur remaining

    def tick(self):
        """Advance one frame. Call once per render cycle."""
        self._frame += 1
        if self.cfg.flicker:
            self._flicker_on = random.random() > self.cfg.flicker_rate
        else:
            self._flicker_on = True

    def notify_scroll(self):
        """Call when content scrolls to trigger blur effect."""
        if self.cfg.scroll_blur:
            self._scroll_smear = 3

    def get_flicker_attr(self) -> int:
        """Return extra dim attribute during flicker frames."""
        if not self._flicker_on:
            return curses.A_DIM
        return 0

    def should_noise(self, row: int, col: int) -> bool:
        """Check if a cell should show static noise this frame."""
        if not self.cfg.static_noise:
            return False
        seed = (self._frame * 1009 + row * 337 + col * 17) & 0xFFFF
        return (seed / 0xFFFF) < self.cfg.noise_density

    def scanline_dim(self, row: int) -> bool:
        """Return True if this row should be dimmed as a scanline."""
        if not self.cfg.scanlines:
            return False
        period = {1: 4, 2: 3, 3: 2}.get(self.cfg.scanline_intensity, 3)
        return (row % period) == 0

    def vignette_dim(self, row: int, col: int, rows: int, cols: int) -> bool:
        """Return True if position is in the vignette shadow zone."""
        if not self.cfg.vignette:
            return False
        dr = min(row, rows - 1 - row) / max(rows, 1)
        dc = min(col, cols - 1 - col) / max(cols, 1)
        edge = min(dr, dc)
        return edge < 0.04

    def smear_active(self) -> bool:
        """Return True if scroll blur is still active."""
        if self._scroll_smear > 0:
            self._scroll_smear -= 1
            return True
        return False


# ─────────────────────────────────────────────────────────────────────────────
# BOOT ANIMATION
# ─────────────────────────────────────────────────────────────────────────────

def boot_animation(stdscr, cfg: CRTConfig):
    """Play CRT-style boot animation with scanline wipe-in."""
    if not cfg.boot_animation:
        return

    rows, cols = stdscr.getmaxyx()
    theme_name = cfg.theme

    # ASCII art logo for Galaxy SDR
    art = [
        "\u256d\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256f",
        "\u2502  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588  \u2502",
        "\u2502 \u2591\u2591 GALAXY SDR \u2591\u2591                     \u2502",
        "\u2502 \u2591\u2591 Device-Agnostic SDR TUI \u2591\u2591       \u2502",
        "\u2502  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588  \u2502",
        "\u2570\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256f",
        "",
        "  Initializing phosphor display...",
    ]

    # Scanline wipe-in (30 frames)
    for frame in range(30):
        stdscr.erase()
        t = frame / 29.0
        visible_rows = int(t * rows)

        # Noise fill below scan line
        for r in range(rows):
            for c in range(cols - 1):
                if r > visible_rows:
                    ch = random.choice("\u2593\u2592\u2591 \u00b7\u2219")
                    try:
                        stdscr.addch(r, c, ch, theme_pair(theme_name, "dim"))
                    except curses.error:
                        pass

        # Art in center (visible above scan line)
        start_r = max(0, rows // 2 - len(art) // 2)
        for i, line in enumerate(art):
            r = start_r + i
            if r >= visible_rows or r >= rows:
                continue
            c = max(0, cols // 2 - len(line) // 2)
            attr = theme_pair(theme_name, "bright") | curses.A_BOLD if i < 6 else theme_pair(theme_name, "fg")
            try:
                stdscr.addstr(r, c, line[:cols - c - 1], attr)
            except curses.error:
                pass

        stdscr.refresh()
        time.sleep(0.04)

    # Linger briefly
    time.sleep(0.3)

    # Fade out (15 frames)
    for frame in range(15):
        alpha = 1 - frame / 15
        stdscr.erase()
        for r in range(rows):
            for c in range(0, cols - 1, 3):
                if random.random() > alpha:
                    ch = random.choice("\u2593\u2592\u2591\u00b7\u2219 ")
                    try:
                        stdscr.addch(r, c, ch, theme_pair(theme_name, "dim"))
                    except curses.error:
                        pass
        stdscr.refresh()
        time.sleep(0.03)

    # Final clear
    stdscr.erase()
    stdscr.refresh()


# ─────────────────────────────────────────────────────────────────────────────
# SETTINGS MENU RENDERER
# ─────────────────────────────────────────────────────────────────────────────

def build_settings_items():
    """Build list of settings for the menu."""
    return [
        # (label, attr_name, type, options_or_range)
        ("\u2500\u2500 CRT Effects \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500", None, "header", None),
        ("Scanlines",         "scanlines",          "bool",   None),
        ("Scanline Intensity","scanline_intensity",  "int",    (1, 3)),
        ("Phosphor Glow",     "phosphor_glow",      "bool",   None),
        ("Static Noise",      "static_noise",       "bool",   None),
        ("Noise Density",     "noise_density",      "float",  (0.005, 0.1, 0.005)),
        ("Flicker",           "flicker",            "bool",   None),
        ("Flicker Rate",      "flicker_rate",       "float",  (0.01, 0.20, 0.01)),
        ("Vignette",          "vignette",           "bool",   None),
        ("Scroll Blur",       "scroll_blur",        "bool",   None),
        ("Boot Animation",    "boot_animation",     "bool",   None),
        ("\u2500\u2500 Theme \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500", None, "header", None),
        ("Color Theme",       "theme",              "choice", list(THEMES.keys())),
    ]


def draw_settings_menu(stdscr, cfg: CRTConfig, cursor: int) -> int:
    """
    Draw settings overlay menu. Returns updated cursor position.
    Handles input and returns new cursor index (or -1 to close).
    """
    rows, cols = stdscr.getmaxyx()
    theme_name = cfg.theme

    # Dim the background by redrawing with dim attribute
    for r in range(rows):
        for c in range(cols - 1):
            try:
                ch = stdscr.inch(r, c) & 0xFF
                stdscr.addch(r, c, chr(ch) if ch else " ",
                            theme_pair(theme_name, "dim") | curses.A_DIM)
            except curses.error:
                pass

    items = build_settings_items()
    panel_w = min(64, cols - 4)
    max_visible = rows - 8
    panel_h = min(len(items) + 6, rows - 2)
    px = (cols - panel_w) // 2
    py = (rows - panel_h) // 2

    # Panel border
    battr = theme_pair(theme_name, "bright", "status_bg") | curses.A_BOLD
    try:
        stdscr.addstr(py, px, ("\u256d" + "\u2500" * (panel_w - 2) + "\u256f")[:panel_w], battr)
        title = f"  \u2699  GALAXY SDR CRT Settings  \u2699  "
        stdscr.addstr(py + 1, px, ("\u2502" + title.center(panel_w - 2) + "\u2502")[:panel_w], battr)
        stdscr.addstr(py + 2, px, ("\u2564" + "\u2500" * (panel_w - 2) + "\u2565")[:panel_w], battr)
    except curses.error:
        pass

    # Scroll list to keep cursor visible
    start = max(0, cursor - max_visible + 1)
    for i, (label, attr, typ, opts) in enumerate(items[start:start + max_visible]):
        row = py + 3 + i
        if row >= py + panel_h - 2:
            break
        idx = i + start
        selected = (idx == cursor)

        if typ == "header":
            val_str = ""
            row_attr = theme_pair(theme_name, "dim", "status_bg")
        else:
            val = getattr(cfg, attr)
            if typ == "bool":
                val_str = "[ON] " if val else "[off]"
            elif typ == "int":
                val_str = f"[ {val} ]"
            elif typ == "float":
                val_str = f"[{val:.3f}]"
            elif typ == "choice":
                val_str = f"[ {val} ]"
            else:
                val_str = str(val)
            row_attr = (theme_pair(theme_name, "bright", "status_bg") | curses.A_BOLD
                       if selected else theme_pair(theme_name, "fg", "status_bg"))

        prefix = "\u25b6 " if selected else "  "
        line = f"\u2502 {prefix}{label:<32}{val_str:>16} \u2502"
        try:
            stdscr.addstr(row, px, line[:panel_w], row_attr)
        except curses.error:
            pass

    # Bottom border + hint
    bot = py + panel_h - 2
    hint = " \u2191\u2193 Navigate  \u2190\u2192 Change  Esc Close "
    try:
        stdscr.addstr(bot, px, ("\u2564" + "\u2500" * (panel_w - 2) + "\u2565")[:panel_w], battr)
        stdscr.addstr(bot + 1, px, ("\u2502" + hint.center(panel_w - 2) + "\u2502")[:panel_w],
                     theme_pair(theme_name, "dim", "status_bg"))
    except curses.error:
        pass

    return cursor


def handle_settings_input(key: int, cfg: CRTConfig, cursor: int) -> tuple:
    """
    Process settings menu input. Returns (new_cursor, should_close).
    """
    items = build_settings_items()

    if key in (27,):  # Escape
        return cursor, True  # Close menu

    if key == curses.KEY_UP and cursor > 0:
        # Skip headers
        new_cursor = cursor - 1
        while new_cursor > 0 and items[new_cursor][2] == "header":
            new_cursor -= 1
        return new_cursor, False

    if key == curses.KEY_DOWN and cursor < len(items) - 1:
        # Skip headers
        new_cursor = cursor + 1
        while new_cursor < len(items) and items[new_cursor][2] == "header":
            new_cursor += 1
        return min(new_cursor, len(items) - 1), False

    if key in (curses.KEY_LEFT, curses.KEY_RIGHT):
        direction = -1 if key == curses.KEY_LEFT else 1
        label, attr, typ, opts = items[cursor]
        if attr is None:
            return cursor, False  # Header, can't adjust

        val = getattr(cfg, attr)
        if typ == "bool":
            setattr(cfg, attr, not val)
        elif typ == "int":
            lo, hi = opts
            setattr(cfg, attr, max(lo, min(hi, val + direction)))
        elif typ == "float":
            lo, hi, step = opts
            new_val = round(val + direction * step, 4)
            setattr(cfg, attr, max(lo, min(hi, new_val)))
        elif typ == "choice":
            idx = opts.index(val) if val in opts else 0
            setattr(cfg, attr, opts[(idx + direction) % len(opts)])

        # Reset color pairs when theme changes
        if attr == "theme":
            reset_color_pairs()

    return cursor, False
