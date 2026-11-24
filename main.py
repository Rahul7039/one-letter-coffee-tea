#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Stdlib only, no network, deterministic: every run produces the same byte.
"""

import os

LETTER = "A"  # coffee — the bolder, louder, more alive pick (see CANDIDATES.md)
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character, no trailing newline: the gate requires 1 to 1 chars.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
