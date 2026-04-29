# Forbidden Truce

A supernatural romance visual novel built in Ren'Py. The player inherits a coastal antique shop and the centuries-old truce between three immortals bound to it.

## Project layout

```
ForbiddenTruceGame/
├── README.md
└── game/
    ├── options.rpy        # project config (name, version, resolution, audio)
    ├── characters.rpy     # Character() definitions + affection state
    ├── script.rpy         # entry point — opens at `label start:`
    ├── images/
    │   ├── characters/    # sprite PNGs (e.g. lucien_neutral.png)
    │   ├── bg/            # backgrounds (e.g. shop_night.png)
    │   └── cg/            # full-screen story art / unlockables
    └── audio/
        ├── music/         # looping BGM (.ogg recommended)
        └── sfx/           # one-shots (clock chime, door, etc.)
```

Ren'Py concatenates every `.rpy` file under `game/` at compile time, so splitting characters into their own file is a convention, not a requirement.

## Running the game

You have two options. **Pick one**, don't mix them.

### Option A — Open from the Ren'Py launcher (easiest)

1. Open the **Ren'Py SDK launcher**.
2. Click **Preferences → Projects Directory** and point it at `/Users/syannevoxland/Downloads/`.
3. The launcher's left-hand list will now show **ForbiddenTruceGame**. Select it.
4. Click **Launch Project** (top-right).

Ren'Py will auto-generate `gui.rpy`, `screens.rpy`, and a few other files the first time it loads the project. That's expected — those handle the menu, save/load, and preferences screens.

### Option B — Run from the terminal

```bash
# adjust the path to wherever you installed the Ren'Py SDK
/Applications/renpy-8.x.x-sdk/renpy.sh /Users/syannevoxland/Downloads/ForbiddenTruceGame
```

On first launch you may see a dialog about generating the GUI files — click **Generate**. Then `Shift+R` reloads the script without restarting the game (huge for iteration).

## Hot keys while playing (developer-useful)

| Key | What it does |
|-----|--------------|
| `Shift+R` | Reload the script (your main iteration loop) |
| `Shift+O` | Open the developer console (run Python live) |
| `Shift+D` | Developer menu (jump to any label, inspect variables) |
| `Ctrl` (hold) | Skip read text |
| `Tab` | Toggle auto-skip |

Enable the dev menu first: in `options.rpy` set `define config.developer = True` while building. Turn it off before shipping.

## VS Code tips

- The **Ren'Py Language** extension you already have gives syntax highlighting and label-jump support.
- Indentation is significant — Ren'Py uses 4-space blocks like Python. If you get a `expected a block` error, check your indentation first.
- Set `"files.associations": { "*.rpy": "renpy" }` in your workspace settings if highlighting ever drops.

## What you'll see on first run

1. A name-entry prompt ("The deed lists your name as…").
2. The midnight shop scene with all three love interests appearing.
3. A 3-way choice (bold / cautious / defensive).
4. A converged truce-reveal scene.
5. A route-locked ending if any one love interest cleared 3 affection — otherwise the common-route ending.

Backgrounds and sprites render as flat colors until you drop real PNGs into `game/images/bg/` and `game/images/characters/`. Filenames map to image tags automatically: `images/bg/shop_night.png` becomes `bg shop_night`, which the script already references.

## Next steps after the script runs

See the chat where this project was scaffolded — there's a numbered "what to do next" list covering art pipeline, route expansion, GUI theming, music, and packaging.
