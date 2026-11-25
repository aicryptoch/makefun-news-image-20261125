#!/usr/bin/env python3
"""Deliver the finished Passage Post page to /output/entry.png.

The page itself — entry.png, sitting beside this file — is the
entry; this script is only the courier. It reads the page's
bytes and writes them out again at the destination, untouched.
Nothing is recomputed and nothing is redrawn. Standard library
only.
"""
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def deliver() -> None:
    payload = ENTRY.read_bytes()
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(payload)
    print(f"delivered {DEST} ({len(payload)} bytes)")


if __name__ == "__main__":
    deliver()
