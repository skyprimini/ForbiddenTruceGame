# script.rpy
# Entry point. Ren'Py looks for `label start:` to begin the game.
#
# QUICK SYNTAX PRIMER
# --------------------
#   label name:         a jump target / scene boundary
#   "string"            narration (no speaker tag)
#   speaker "string"    dialogue ("speaker" must be a defined Character)
#   scene bg foo        clear stage, set background to image "bg foo"
#   show char foo       overlay a character sprite (image "char foo")
#   hide char foo       remove that sprite
#   with dissolve       transition for the previous scene/show/hide
#   menu:               player choice block; each indented "label":
#                       line is one option
#   $ python_expr       inline Python (use for variable changes)
#   jump label_name     hard transfer (no return)
#   call label_name     subroutine — returns to caller on `return`
#   if / elif / else    standard Python conditionals
#
# IMAGE NAMING
# ------------
# Ren'Py auto-defines an image from any file in `game/images/`.
# A file named `images/bg/bg_shop_night.png` becomes the image `bg_shop_night`.
# You then reference it with `scene bg_shop_night`.
#
# --- Placeholder art -------------------------------------------------------
# Registering placeholders via `renpy.image()` inside an `init python:` block
# lets the game run with no real assets AND keeps the VS Code Ren'Py
# extension's linter quiet (the top-level `image foo = Solid(...)` form
# trips its parser, even though the engine accepts it).
#
# Drop a real PNG named `bg_shop_night.png` into game/images/bg/ to
# override the placeholder — Ren'Py prefers files over registered images.
# The "not defined" warnings the linter shows on `scene bg_shop_night`
# below are false positives; renpy.image() registers at runtime, not at
# parse time, so the static linter can't see the names. Safe to ignore.

init python:
    renpy.image("bg_shop_night", Solid("#0e0a1a"))
    renpy.image("bg_shop_dawn",  Solid("#3a2a44"))
    renpy.image("bg_cliff",      Solid("#1a2638"))
    renpy.image("lucien_neutral", Solid("#5a1428"))
    renpy.image("kai_neutral",    Solid("#a87520"))
    renpy.image("ronan_neutral",  Solid("#2a4a3a"))

# --- Game start ------------------------------------------------------------

label start:

    # `python:` block runs arbitrary Python. Used here to prompt for the
    # player's name. `renpy.input` blocks until the player presses Enter.
    python:
        player_name = renpy.input(
            "The deed lists your name as…",
            default="Wren",
            length=20,
        ).strip() or "Wren"

    scene bg shop_night
    with fade

    # Internal monologue using the `thought` character (italic, no name).
    thought "Midnight. The bell over the door hasn't rung in hours, and the shop smells like cedar and old smoke."
    thought "Grandma's letter said to be here when the clock struck twelve. It didn't say why."

    # A clock-strike SFX would play here. The `play sound` line is commented
    # because the file doesn't exist yet — uncomment once you add it.
    # play sound "audio/sfx/clock_chime.ogg"

    "The longcase clock in the corner begins to chime."
    "On the twelfth strike, the air pressure in the room changes."

    # Show all three sprites in sequence. `at` positions accept built-in
    # transforms (left/center/right) or your own from transforms.rpy.
    show char lucien neutral at left
    with dissolve
    show char kai neutral at center
    with dissolve
    show char ronan neutral at right
    with dissolve

    "Three figures stand where there had been empty floor."

    lucien "So. The keeper's blood lives on."
    kai "Oh — oh, you look just like her around the eyes. Hi. Hello. Sorry, this is a lot."
    ronan "...."

    $ met_all_three = True

    mc "Who — what — how did you get inside? The door's locked."
    lucien "We never left. Your grandmother bound us here a very long time ago."
    kai "Bound is a strong word. *Hosted.* She hosted us. There's tea involved usually."
    ronan "The truce holds because the shop holds. The shop holds because the keeper holds."

    "Three pairs of eyes settle on you, waiting."

    # ----------------------------------------------------------------
    # BRANCHING INTRO — the player picks a tone. Each branch sets
    # `intro_path` and nudges affection in different directions, then
    # all three jump to the same converged scene.
    # ----------------------------------------------------------------
    menu:
        "How do you respond?"

        "\"Then start talking. I want to know everything.\" (bold)":
            jump intro_bold

        "\"Slow down. One at a time — please.\" (cautious)":
            jump intro_cautious

        "\"Stay back. I don't know any of you.\" (defensive)":
            jump intro_defensive


# --- Branch A: BOLD --------------------------------------------------------

label intro_bold:

    $ intro_path = "bold"
    # Bold demands respect from Lucien, surprises Kai, makes Ronan wary.
    $ lucien_aff += 2
    $ kai_aff    += 1
    $ ronan_aff  -= 1

    mc "Then start talking. I want to know everything."

    lucien "...Bold. Good. Boldness is the only currency that ever bought my honesty."
    kai "Whoa. Okay. Coming in hot. I respect it."
    ronan "Bold gets people killed, in my experience."

    "Lucien's mouth curves — not quite a smile, not quite a threat."

    jump intro_converge


# --- Branch B: CAUTIOUS ----------------------------------------------------

label intro_cautious:

    $ intro_path = "cautious"
    $ lucien_aff -= 1
    $ kai_aff    += 2
    $ ronan_aff  += 1

    mc "Slow down. One at a time — please."

    kai "Yes! Yes, that's the right instinct. I'll go first because I'm the least scary, statistically."
    ronan "Smart. The ones who run in fast don't last."
    lucien "How disappointing. I had hoped for a little more spine."

    jump intro_converge


# --- Branch C: DEFENSIVE ---------------------------------------------------

label intro_defensive:

    $ intro_path = "defensive"
    $ lucien_aff -= 1
    $ kai_aff    -= 1
    $ ronan_aff  += 2

    mc "Stay back. I don't know any of you."

    ronan "...Good. That's the right answer."
    kai "Aw. I mean — fair. Totally fair."
    lucien "A frightened keeper. How novel."

    "Ronan steps slightly in front of the other two — not aggressive, just *between*."

    jump intro_converge


# --- Converged scene -------------------------------------------------------
# All three branches funnel here. The scene reads slightly differently
# depending on `intro_path`, but the plot beat — the truce reveal — is
# the same for everyone.

label intro_converge:

    "The shop seems to exhale around you. Floorboards settle. The clock ticks once, deliberate."

    # Use intro_path to color the converged narration without rewriting
    # the whole scene. This is the cheap, scalable way to handle branches:
    # converge often, vary flavor lines.
    if intro_path == "bold":
        thought "He's still watching me. Lucien. Like he's deciding something."
    elif intro_path == "cautious":
        thought "Kai's relieved. I can feel it from here."
    else:
        thought "Ronan hasn't taken his eyes off the door. He's listening for something."

    lucien "Three of us. One truce. Renewed every generation by a woman who shared your blood."
    kai "Vampires, witches, werewolves. We don't, uh, traditionally get along."
    ronan "We don't fight here. That's the only rule that ever mattered."
    lucien "And the rule only holds while a keeper draws breath inside these walls."

    $ truce_revealed = True

    mc "And if I refuse?"

    lucien "Then the truce ends at sunrise. And the town learns what we are."

    "Silence. The kind that has weight."

    mc "...I need to think."

    kai "Of course. Take the night. We'll be here — we kind of *have* to be."
    ronan "Door's still yours. Lock it if it helps."
    lucien "Decide before dawn, keeper."

    hide char lucien neutral
    hide char kai neutral
    hide char ronan neutral
    with dissolve

    scene bg shop_dawn
    with fade

    "You don't sleep. By the time grey light bleeds through the front window, you have an answer — but the night has rearranged something inside you."

    # ----------------------------------------------------------------
    # ROUTE GATING — the second divergence.
    # We pick the highest-affection love interest as the route lead,
    # but only if they cleared the threshold of 3. Otherwise the player
    # gets the "common route" ending and has to replay choosing differently.
    # ----------------------------------------------------------------

    $ scores = {"lucien": lucien_aff, "kai": kai_aff, "ronan": ronan_aff}
    $ leader = max(scores, key=scores.get)
    $ leader_score = scores[leader]

    if leader_score >= 3:
        if leader == "lucien":
            jump ending_lucien_locked
        elif leader == "kai":
            jump ending_kai_locked
        else:
            jump ending_ronan_locked
    else:
        jump ending_common


# --- Endings ---------------------------------------------------------------
# Each "ending" here is really a route OPENING — a one-scene teaser that
# locks the player into that love interest's path. You'll expand each into
# a full route in its own file later (lucien_route.rpy, etc.).

label ending_lucien_locked:
    scene bg shop_dawn
    show char lucien neutral at center
    with dissolve
    lucien "You stayed. I admit, I expected you to run."
    mc "I don't run from things I want to understand."
    lucien "Then understand this: I will tell you the truth, even when it cuts. That is the only gift I have left to give."
    "[Lucien's route unlocked.]"
    # Route is fully scaffolded in lucien_route.rpy — jump straight in.
    jump route_lucien_start

label ending_kai_locked:
    scene bg shop_dawn
    show char kai neutral at center
    with dissolve
    kai "You're still here! I brought scones. They're, um, slightly enchanted but in a good way."
    mc "Define 'good way.'"
    kai "You'll feel brave for about an hour. I figured you'd earned it."
    "[Kai's route unlocked.]"
    return

label ending_ronan_locked:
    scene bg cliff
    show char ronan neutral at center
    with dissolve
    ronan "Walk with me. The cliffs are quiet this early."
    mc "Are you always this direct?"
    ronan "Only with people I'd protect. Come on."
    "[Ronan's route unlocked.]"
    return

label ending_common:
    scene bg shop_dawn
    with fade
    "By dawn, none of the three has won your trust — not really."
    "You renew the truce out of duty, not connection. The shop holds. So do you."
    "But the nights ahead will be longer than they need to be."
    "[Common route — try again with different choices to unlock a romance.]"
    return
