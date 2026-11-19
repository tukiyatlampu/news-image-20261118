#!/usr/bin/env python3
"""Decode image.b64 into the graded entry.png.

The poster is vendored as base64 so the repository stays text-only.
Decoding is deterministic: the same input bytes always give the
same output bytes, with no network and no clock involved.
"""
import base64
from pathlib import Path

IMAGE_B64 = Path(__file__).resolve().parent / "image.b64"
TARGET = Path("/output/entry.png")


def write_entry() -> Path:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(base64.b64decode(IMAGE_B64.read_text(encoding="ascii")))
    return TARGET


if __name__ == "__main__":
    write_entry()
