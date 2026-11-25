#!/usr/bin/env python3
"""Entry point for the 25 November 2026 world-news image (Python 3.13, stdlib only).

The entry image is pre-rendered by draw.py (PIL, run locally) and shipped
as entry.png beside this file; this program copies it to the output path
the grader reads. The grader's container has no Pillow, so this file
imports nothing beyond the standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
