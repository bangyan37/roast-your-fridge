#!/usr/bin/env python3
"""Roast Your Fridge: one line roasting a smart fridge.

Writes a single line (at most 200 characters) to /output/entry.txt:
touchscreen, camera and push notifications, yet its proudest
feature is still the little light from 1957.
"""
import os

LINE = (
    "My fridge has a touchscreen, a camera, and push notifications, but its "
    "proudest feature is still a little light that comes on when I open it, "
    "like it's 1957 with a newsletter."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
