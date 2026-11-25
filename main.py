#!/usr/bin/env python3
"""Midnight fridge roast — one line, under 200 characters.

The fridge is the only appliance awake at 3 a.m., humming like it pays
rent, guarding leftovers nobody wants and judging every snack run —
so it gets roasted for it.
"""

import os

ENTRY = (
    "My fridge at 3 a.m. hums like it pays rent, yet all it guards is "
    "a dead pickle, one sad egg, and a takeout box from 2019."
)

OUTPUT_PATH = (
    "/tmp/sweep27-u-carbon-forge-midnight-fridge-roast-fc5d44a7/entry.txt"
)


def main() -> None:
    # Enforce the bounty limit before writing anything.
    if len(ENTRY) > 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be <= 200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
