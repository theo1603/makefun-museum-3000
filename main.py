#!/usr/bin/env python3
"""Museum of the Year 3000: writes one museum label to /output/entry.txt.

One line, at most 200 characters, in English: the label a museum in the
year 3000 puts beside an ordinary object from today. Python stdlib only,
no network, no randomness -- the same label on every run.
"""
import os

LABEL = (
    "Parking meter: a coin-fed shrine. Ancestors paid a metal box for permission "
    "to leave their carriage unattended, then hurried back before the god of the curb grew angry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
