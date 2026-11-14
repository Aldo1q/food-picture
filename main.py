#!/usr/bin/env python3
"""Entry program for make.fun's "Make the best-looking food picture" bounty.

Writes one picture of food to /output/entry.png: a photorealistic
gourmet smash burger with melting cheddar, generated for this entry.

The program is deterministic: it copies the bundled entry.png byte for
byte, so two runs write identical files. It uses no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    # The competition requires a whole PNG or JPEG of at most 1 MiB and
    # 1024 by 1024 pixels; fail loudly instead of writing an invalid entry.
    size = os.path.getsize(SRC)
    if size > 1024 * 1024:
        raise SystemExit("entry.png exceeds 1 MiB")
    with open(SRC, "rb") as f:
        header = f.read(8)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
