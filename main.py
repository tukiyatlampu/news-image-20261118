#!/usr/bin/env python3
"""Write the vendored news poster to /output/entry.png.

The poster travels as base64 text (image.b64) so the repository holds
only UTF-8 files. No network, no randomness, no clock: every run
writes the same bytes. The poster itself is drawn by build_poster.py
(flat colours, PIL, 1024x1024, 50 sourced stories of 18 Nov 2026).
"""
import base64
from pathlib import Path

SRC = Path(__file__).resolve().parent / "image.b64"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(base64.b64decode(SRC.read_text(encoding="ascii")))


if __name__ == "__main__":
    main()
