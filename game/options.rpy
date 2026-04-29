# options.rpy
# Project-wide configuration. Ren'Py reads this at startup.
# `define` runs ONCE at game start (before any label). Use it for constants.
# `default` sets a variable's INITIAL value but lets it change during play
# and persist across save/load. Use `default` for game state, `define` for
# constants like the game name or window title.

define config.name = _("Forbidden Truce")

# Version string shown in the title bar and "About" screen.
define config.version = "0.1.0"

# Short description used by the launcher and itch.io exports.
define gui.about = _("A supernatural romance visual novel.")

# `build.name` is the slug used when packaging distributions.
# Keep it lowercase, no spaces — it becomes the .zip / .app filename.
define build.name = "forbidden_truce"

# Default save location follows config.name unless overridden here.
# Leaving this commented uses Ren'Py's per-OS default (good for now).
# define config.save_directory = "ForbiddenTruce-1577123456"

# --- Audio defaults --------------------------------------------------------
# These set the starting channel volumes (0.0–1.0). Players can override
# them in the preferences screen at runtime.
define config.default_music_volume = 0.6
define config.default_sound_volume = 0.8
define config.default_voice_volume = 1.0

# --- Window / display ------------------------------------------------------
# 1920x1080 is Ren'Py's modern default. Change here if you want a different
# native resolution; assets must match this aspect ratio for crisp rendering.
define config.screen_width = 1920
define config.screen_height = 1080

# Auto-skip read text when holding Tab. Players love this; keep it on.
define config.allow_skipping = True
