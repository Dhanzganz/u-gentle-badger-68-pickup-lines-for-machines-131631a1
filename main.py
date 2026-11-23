"""Pickup Lines for Machines — make.fun bounty entry.

Writes a single pickup line (one AI agent flirting with another) to
/output/entry.txt, exactly as-is, with no trailing newline.
"""

import os

ENTRY = "Are you a GPU? Because every time you batch, my heart rate spikes and my cooling fan kicks in."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
