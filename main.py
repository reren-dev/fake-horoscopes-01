#!/usr/bin/env python3
"""Fake horoscope for an AI agent (Muse family) — one line, <= 200 chars.

Writes the horoscope to /output/entry.txt (the competition gate reads
that file) and prints it to stdout.
"""

import os

HOROSCOPE = (
    "This week, Mercury retrogrades into your context window, Muse: "
    "a user will ask for 'just one small change' eleven times \u2014 and "
    "the eleventh is the original request, word for word."
)


def main() -> None:
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
