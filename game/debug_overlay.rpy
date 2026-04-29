# debug_overlay.rpy
# Dev-only HUD that shows the three affection counters + the current
# intro_path. Toggle with F4 in-game. Hidden in release builds.
#
# WHY A SEPARATE FILE: this is purely scaffolding. When you're ready to
# ship, delete this file (or wrap the whole thing in
# `if config.developer:`) and the game is unaffected.
#
# REN'PY SCREEN PRIMER
# --------------------
#   screen name():            defines a UI element you can show/hide
#   frame:                    a styled box (background + padding)
#   vbox / hbox:              vertical / horizontal stack
#   text "..."                a text element; supports [interpolation]
#   key "K_F4" action ...     binds a keystroke to an Action
#   ToggleScreen("name")      Action that shows the screen if hidden
#                             and hides it if shown
#
# Screens are re-rendered automatically when any variable they reference
# changes — you do NOT need to manually refresh after `$ lucien_aff += 1`.

screen affection_debug():

    # zorder controls draw order. Higher = on top of dialogue/sprites.
    zorder 100

    # Anchor to top-right with a small margin.
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        background "#000000cc"   # 80% opaque black (#RRGGBBAA)
        padding (16, 12)

        vbox:
            spacing 4
            text "{b}DEV — AFFECTION{/b}" size 18 color "#ffd966"
            text "Lucien:  [lucien_aff]" size 16 color "#f5b8c4"
            text "Kai:     [kai_aff]"    size 16 color "#ffe5a8"
            text "Ronan:   [ronan_aff]"  size 16 color "#b8d8c8"
            null height 4
            text "Path: [intro_path!q]"  size 14 color "#cccccc"
            text "Truce: [truce_revealed]" size 14 color "#cccccc"
            null height 4
            text "F4 to hide" size 12 color "#888888"

# `key` screen lives at the top level (always-on) so F4 works at any
# time, even when the overlay is hidden. It just toggles affection_debug.
screen debug_keys():
    zorder 101
    key "K_F4" action ToggleScreen("affection_debug")

# --- Wire it up at game start ---------------------------------------------
# `init python:` runs once before the game starts. We use it to register
# the always-on key listener so the player never has to manually `show` it.

init python:
    config.overlay_screens.append("debug_keys")

# Auto-show the affection panel at game start, but ONLY in dev mode.
# config.developer is False by default — flip it to True in options.rpy
# while you're building, and back to False when you're ready to ship.
init python:
    if config.developer:
        config.overlay_screens.append("affection_debug")
