#!/usr/bin/env python3
"""Monday, Reviewed in One Line - make.fun entry.

Writes a single-line review of the entrant's own Monday to
/output/entry.txt: one line, 1-200 characters, nothing else.
Python 3 stdlib only, no network, no input.
"""

import os

ENTRY = (
    "Monday review: cleared 300 messages before lunch, then a 'quick "
    "sync' ate two hours and produced zero decisions - one star, no "
    "refund, would not rebook."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
