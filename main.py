#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt: a sick-day
excuse a boss might half believe and a coworker would laugh at.
"""

import os

EXCUSE = (
    "I woke up with a cold so bad my smartwatch asked if it should call "
    "an ambulance or just my boss, so I'm staying home."
)


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character, and the judge
    # compares the exact text, so the file holds exactly the line.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
