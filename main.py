#!/usr/bin/env python3
"""Two Days of Excuses — writes one one-line AI-agent excuse to output/entry.txt."""

from pathlib import Path

ENTRY = "I was 99.9% confident I had finished, so I spent the last two days wondering why nobody could see the file."


def main() -> None:
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    assert entry.strip(), "entry must not be only whitespace"
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
