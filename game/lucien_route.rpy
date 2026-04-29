# lucien_route.rpy
# Lucien's romance route — entered from `ending_lucien_locked` in script.rpy
# once the player has 3+ Lucien affection.
#
# STRUCTURE PATTERN (copy this for kai_route.rpy and ronan_route.rpy):
#   1. route_<name>_start          — opening beat after the lock-in
#   2. <name>_act1, _act2, _act3   — major story beats (one label each)
#   3. branching choices inside acts adjust affection further
#   4. final affection threshold at end of act 3 picks ending tier:
#         >= 8  →  good ending
#         >= 5  →  neutral ending
#         else  →  bad ending
#
# Acts are deliberately small here so you can flesh them out without
# unpacking a giant scaffold.

# --- Route-local state -----------------------------------------------------
# `default` vars are global, but prefixing with the route name keeps them
# from colliding with Kai's / Ronan's flags later.

default lucien_trust_broken = False    # set True if player betrays him
default lucien_blood_pact   = False    # gating flag for the good ending
default lucien_act          = 0        # 0/1/2/3 — current act for save scumming

# --- Placeholder art unique to this route ---------------------------------
# Real PNGs at game/images/bg/wine_bar.png etc. will override these.
image bg wine_bar    = Solid("#2a0814")
image bg shop_study  = Solid("#1f1428")
image char lucien smile  = Solid("#7a1e35")
image char lucien guarded = Solid("#3d0a18")


# --- Entry point ----------------------------------------------------------

label route_lucien_start:

    $ lucien_act = 1

    scene bg shop_dawn
    show char lucien neutral at center
    with dissolve

    "The dawn light catches the silver at his temples. He looks tired in a way that has nothing to do with sleep."

    lucien "I'll be at the bar tonight. Le Caveau, on Harbor Street. After dark."
    lucien "If you want answers, come find me. If you don't — I'll understand. Most do not."

    mc "I'll come."

    lucien "...We'll see."

    hide char lucien neutral
    with dissolve

    jump lucien_act1


# ============================================================================
# ACT 1 — The wine bar
# ============================================================================

label lucien_act1:

    scene bg wine_bar
    with fade

    "Le Caveau is empty when you arrive. One candle on the bar. One glass already poured."

    show char lucien guarded at center
    with dissolve

    lucien "You're punctual. That's either a virtue or a warning sign."

    menu:
        "How do you respond?"

        "\"I keep my word. Always.\"":
            $ lucien_aff += 2
            mc "I keep my word. Always."
            lucien "Then you and I will get along better than I expected."
            show char lucien smile at center
            with dissolve

        "\"I was curious. That's all.\"":
            $ lucien_aff += 1
            mc "I was curious. That's all."
            lucien "Curiosity is honest. I'll take it."

        "\"Don't read into it.\"":
            $ lucien_aff -= 1
            $ lucien_trust_broken = True
            mc "Don't read into it."
            lucien "...Noted."
            show char lucien guarded at center
            with dissolve

    "He pushes the glass toward you. The wine is darker than wine has any right to be."

    lucien "My grandmother's vintage. Older than your country. Drink — or don't. The choice itself is the answer I need."

    menu:
        "What do you do?"

        "Drink without hesitation.":
            $ lucien_aff += 2
            mc "*lifts the glass*"
            lucien "Trust before understanding. That's rarer than the wine."

        "Ask what's in it first.":
            $ lucien_aff += 1
            mc "What's in it?"
            lucien "Grapes. Time. A question. Drink."

        "Push it back.":
            $ lucien_aff -= 2
            mc "Not tonight."
            lucien "Then we will get nowhere, you and I."

    jump lucien_act2


# ============================================================================
# ACT 2 — The truth Lucien doesn't tell anyone
# ============================================================================

label lucien_act2:

    $ lucien_act = 2

    scene bg shop_study
    with fade

    "A week passes. Lucien starts arriving at the shop just after midnight, every night, with a different question."
    "Tonight he doesn't ask one. He just sits across from you and stares at the fire."

    show char lucien neutral at center
    with dissolve

    lucien "I have not told this to a living person in two hundred years."
    lucien "Your grandmother knew. She is the only one who knew. And now she is gone."

    "He looks at you the way a man looks at the last bridge out of a city that is on fire."

    lucien "I did not become this willingly. I was given to it, by someone I trusted. The truce — the *real* reason for the truce — is that I cannot be allowed to leave this town."

    menu:
        "How do you respond?"

        "Reach for his hand.":
            $ lucien_aff += 3
            "His hand is colder than the room. He doesn't pull it back."
            lucien "...You should be running."
            mc "I'm not."

        "\"Why are you telling me this?\"":
            $ lucien_aff += 1
            mc "Why are you telling me this?"
            lucien "Because the keeper before you carried this for forty years and never wavered. I would like to believe you can do the same."

        "Stay silent.":
            $ lucien_aff += 0
            "You don't speak. Sometimes silence is the only honest answer."
            lucien "...Yes. That, too, is a reply I can live with."

    jump lucien_act3


# ============================================================================
# ACT 3 — The blood pact and the ending fork
# ============================================================================

label lucien_act3:

    $ lucien_act = 3

    scene bg shop_night
    with fade

    show char lucien neutral at center
    with dissolve

    "A month into knowing him, Lucien comes to the shop carrying a wooden box."

    lucien "There is a thing keepers can offer, if they choose. A blood pact. It binds the truce more deeply — and binds *me* to your line, not just to the walls."

    lucien "It is not a small thing. Refuse and I will not raise it again. Accept and I will be yours until the day you release me."

    menu:
        "Your answer?"

        "Accept the pact.":
            $ lucien_blood_pact = True
            $ lucien_aff += 2
            mc "I accept."
            "He doesn't smile. Something older than a smile crosses his face."

        "Refuse — for now.":
            $ lucien_aff += 0
            mc "Not yet. I need more time."
            lucien "Time is the one currency I have in surplus. Take what you need."

        "Refuse — permanently.":
            $ lucien_aff -= 2
            $ lucien_trust_broken = True
            mc "Never. I won't be bound to anyone."
            lucien "...Then I have my answer."

    # --- Ending fork ------------------------------------------------------
    # Final affection + the two flags select one of three endings.
    # The blood pact is REQUIRED for the true good ending, even at high aff.

    if lucien_aff >= 8 and lucien_blood_pact and not lucien_trust_broken:
        jump ending_lucien_good
    elif lucien_aff >= 5 and not lucien_trust_broken:
        jump ending_lucien_neutral
    else:
        jump ending_lucien_bad


# --- Endings --------------------------------------------------------------

label ending_lucien_good:
    scene bg shop_dawn
    with fade
    "The pact takes. The shop accepts him in a way it never has before — every floorboard, every shelf, every shadow."
    "He is no longer bound to walls. He is bound to you."
    lucien "I have been alive a very long time. I have never been *home* before."
    "{b}TRUE ENDING — Lucien: The Last Bridge{/b}"
    return

label ending_lucien_neutral:
    scene bg shop_dawn
    with fade
    "You and Lucien settle into something quieter than romance and sturdier than friendship."
    "The truce holds. He stays. It is not everything you hoped for. It is not nothing."
    "{b}NEUTRAL ENDING — Lucien: The Long Truce{/b}"
    return

label ending_lucien_bad:
    scene bg shop_dawn
    with fade
    "Lucien stops coming to the shop after midnight. Then he stops coming at all."
    "The truce holds — barely — but the bar on Harbor Street is dark every night now."
    "You see him once, from a distance, near the cliffs. He does not turn around."
    "{b}BAD ENDING — Lucien: The Bridge Burned{/b}"
    return
