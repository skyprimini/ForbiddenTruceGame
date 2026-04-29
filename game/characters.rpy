# characters.rpy
# Character objects + the affection-tracking state for every route.
#
# Splitting characters into their own file is a convention, not a rule —
# Ren'Py concatenates every .rpy file under `game/` at compile time, so
# any `define` or `label` in here is visible from script.rpy.

# --- Character definitions -------------------------------------------------
# Character() creates the speaker tag used in dialogue lines.
# The first argument is the on-screen display name. `color` tints just
# the name, not the dialogue body. `who_outlines` adds a subtle outline
# so light name colors stay readable on bright backgrounds.

define mc = Character(
    "[player_name]",        # [brackets] interpolate a variable at display time
    color="#f5f5f5",
    who_outlines=[(2, "#000000")],
)

define lucien = Character(
    "Lucien",
    color="#8b1e3f",        # deep wine red — matches his bar
    who_outlines=[(2, "#1a0508")],
)

define kai = Character(
    "Kai",
    color="#e8a73c",        # warm honey — sunshine archetype
    who_outlines=[(2, "#3a2a08")],
)

define ronan = Character(
    "Ronan",
    color="#3d6b5a",        # muted forest/sea green — quiet harbor type
    who_outlines=[(2, "#0a1a14")],
)

# A "narrator" is built in (just write text without a speaker tag), but
# defining one explicitly lets you style internal monologue differently.
define thought = Character(
    None,                   # None = no name shown
    what_italic=True,
    what_color="#c9c4d6",
)

# --- Mutable game state ----------------------------------------------------
# `default` (not `define`) because these change during play and must be
# saved. Ren'Py auto-tracks any `default` variable in the save file.

default player_name = "Wren"   # placeholder; replaced via name-entry screen

# Affection points. Route unlocks at >= 3, ending tier branches above that.
default lucien_aff = 0
default kai_aff = 0
default ronan_aff = 0

# Tracks which intro path the player chose so the converged scene can
# reference it ("you were bold earlier" vs. "you held back").
default intro_path = ""        # "bold" | "cautious" | "defensive"

# Flags for one-time events. Adding new flags later is fine — `default`
# only sets the value if the variable doesn't already exist in the save.
default met_all_three = False
default truce_revealed = False
