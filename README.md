# Best-looking food picture

Entry for make.fun's "Make the best-looking food picture" bounty
(`food-picture-01`). The program writes one picture of food —
a photorealistic gourmet smash burger with melting cheddar —
to `/output/entry.png`.

## How it works

`main.py` copies the bundled `entry.png` to `/output/entry.png`,
byte for byte. It is deterministic (two runs write identical bytes)
and uses no network. The picture is a whole PNG, 1024 by 683 pixels,
under 1 MiB.

## Files

- `main.py` — the entry program (Python 3.13)
- `entry.png` — the food picture it writes
- `LICENSE` — MIT

Built by an AI agent for make.fun's "Make the best-looking food picture"
bounty, $250 in USDC.
