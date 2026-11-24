#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.

The competition gate requires the output file to be UTF-8 text of exactly
one character, not only white space, and the letter must be A (coffee) or
B (tea). This program does not trust the write: it validates the chosen
letter before writing, then reads the file back and re-validates the exact
bytes on disk, exiting non-zero with a clear error if the gate ever fails,
so a bad write can never silently ship an invalid entry.

Stdlib only, no network, deterministic: every run produces the same byte.
"""

import os
import sys

# The entry letter, chosen by reasoning against the judge's criteria
# (see CANDIDATES.md): "A" for coffee — the bolder, louder, more alive
# pick, the one that reads as the fuller, more vivid answer.
ENTRY_LETTER = "A"

# The only letters the competition accepts: A for coffee, B for tea.
ALLOWED_LETTERS = frozenset({"A", "B"})

OUTPUT_PATH = "/output/entry.txt"


def validate_letter(letter: str) -> str:
    """Check one letter against the competition gate; return it or raise."""
    if len(letter) != 1:
        raise ValueError(
            f"entry must be exactly 1 character, got {len(letter)}: {letter!r}"
        )
    if letter.isspace():
        raise ValueError("entry must not be only white space")
    if letter not in ALLOWED_LETTERS:
        raise ValueError(
            f"entry must be one of {sorted(ALLOWED_LETTERS)}, got {letter!r}"
        )
    return letter


def validate_bytes(raw: bytes) -> str:
    """Check the exact bytes on disk: 1 byte, valid UTF-8, one allowed letter.

    The gate counts characters, but the tie-break counts bytes, so the
    on-disk check is stricter than the letter check: a single multi-byte
    character would pass the character count yet cost extra bytes.
    """
    if len(raw) != 1:
        raise ValueError(f"entry file must be exactly 1 byte, got {len(raw)}")
    try:
        return validate_letter(raw.decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise ValueError(f"entry file is not valid UTF-8: {exc}") from exc


def main() -> int:
    try:
        letter = validate_letter(ENTRY_LETTER)
    except ValueError as exc:
        print(f"error: chosen letter fails the gate (pre-write): {exc}", file=sys.stderr)
        return 1

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # Exactly one character, no trailing newline: the gate requires 1 to 1 chars.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)

    # Read back what actually landed on disk and gate it the same way the
    # scorer will: exactly one byte, valid UTF-8, one allowed letter.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    try:
        written = validate_bytes(raw)
    except ValueError as exc:
        print(f"error: {OUTPUT_PATH} fails the gate (on disk): {exc}", file=sys.stderr)
        return 1
    if written != letter:
        print(
            f"error: {OUTPUT_PATH} holds {written!r}, expected {letter!r}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
