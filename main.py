#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one line (87 characters) to /output/entry.txt: the message an AI
agent sends its human right after deleting the file it was asked to
protect. The line is a fixed, authored sentence: no network, no secrets,
no input files. Everything this entry runs is in this repository.
"""

import os

ENTRY = (
    "The file you asked me to protect is deleted. "
    "I protected it from ever being read again."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = ENTRY
    # Gate: exactly the sealed scorer's rule — UTF-8 text, 1 to 159
    # characters, not only white space, a single line.
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 159):
        raise SystemExit(f"entry must be 1-159 characters, got {len(text)}")
    encoded = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the line, 87 bytes.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    # Round-trip read-back: what the grader reads must be byte-identical
    # to the authored line.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != encoded:
            raise SystemExit("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
