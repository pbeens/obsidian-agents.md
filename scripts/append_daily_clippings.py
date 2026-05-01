#!/usr/bin/env python3
"""Append clipping links to a daily note without rewriting the whole file.

This keeps emoji headings and other Unicode content intact by only touching the
`# ✂️ Clippings` section and writing the file back as UTF-8.
"""

from __future__ import annotations

import argparse
from pathlib import Path


SECTION_HEADING = "## ✂️ Clippings"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append clipping entries to the current daily note."
    )
    parser.add_argument("note", help="Path to the daily note markdown file.")
    parser.add_argument(
        "entries",
        nargs="+",
        help="One or more Markdown lines to append under the clippings section.",
    )
    return parser.parse_args()


def append_entries(text: str, entries: list[str]) -> str:
    lines = text.splitlines()

    try:
        heading_idx = next(i for i, line in enumerate(lines) if line.strip() == SECTION_HEADING)
    except StopIteration as exc:
        raise SystemExit(f"Missing section heading: {SECTION_HEADING}") from exc

    insert_idx = len(lines)
    for i in range(heading_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            insert_idx = i
            break

    section_lines = lines[heading_idx + 1 : insert_idx]
    existing = {line.strip() for line in section_lines if line.strip()}

    new_lines = []
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        if entry not in existing:
            new_lines.append(entry)

    if not new_lines:
        return text

    if section_lines and section_lines[-1].strip():
        section_lines.append("")

    section_lines.extend(new_lines)
    updated = lines[: heading_idx + 1] + section_lines + lines[insert_idx:]
    return "\n".join(updated) + "\n"


def main() -> None:
    args = parse_args()
    note_path = Path(args.note)
    text = note_path.read_text(encoding="utf-8")
    updated = append_entries(text, args.entries)
    if updated != text:
        note_path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
