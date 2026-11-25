#!/usr/bin/env python3
"""Write one meeting joke to /output/entry.txt.

The program is fully deterministic and offline: it writes one fixed
string, exactly as-is, with no trailing newline and no second line.
No randomness, no network, no clock, no environment input.
"""

import os

ENTRY = "The 3,000-word email that replaced the meeting was so long we scheduled a meeting to discuss the email."


def main():
    # Self-check the gate before writing: one line, 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
