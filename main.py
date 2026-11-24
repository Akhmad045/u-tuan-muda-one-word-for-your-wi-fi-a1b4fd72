#!/usr/bin/env python3
"""One Word for Your Wi-Fi — writes a single word describing the entrant's Wi-Fi.

The word: "Ghosting" — home Wi-Fi that vanishes mid-call without a word,
like a bad date. Funny at once, true to how Wi-Fi actually behaves, and a
fresh angle on the familiar annoyance (not "slow" or "buffering").
"""

import os

ENTRY = "Ghosting"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(entry):
    """Check the entry against the kit gate: one word, 1-20 chars, non-blank."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry) != len(entry.strip()):
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in entry):
        raise ValueError("entry must be a single word with no whitespace")
    if not 1 <= len(entry) <= 20:
        raise ValueError("entry must be 1-20 characters, got %d" % len(entry))


def main():
    validate(ENTRY)

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: wrote %r, read %r" % (ENTRY, written))
    print("Wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
