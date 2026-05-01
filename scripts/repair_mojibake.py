#!/usr/bin/env python3
"""Repair common mojibake patterns in vault text files.

This script is intentionally small and conservative. It cleans up a few
recurring encoding artifacts before transcript ingestion or related link
updates, without renaming files or trying to guess at unrelated content.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_EXTENSIONS = {".md", ".txt", ".json", ".toml"}

# Keep this list narrow and explicit. We only fix patterns that have already
# appeared in this vault or in its Obsidian workspace state.
REPLACEMENTS: list[tuple[str, str]] = [
    ("M\u00c3\u00a9tis", "M\u00e9tis"),
    ("MActis", "M\u00e9tis"),
    ("MA\u0178Actis", "M\u00e9tis"),
    ("M\uFF35is", "M\u00e9tis"),
    ("M\u201Atis", "M\u00e9tis"),
    ("\u00c2\u00a0", "\u00a0"),
    ("\u00e2\u20ac\u201c", "\u2013"),
    ("\u00e2\u20ac\u201d", "\u2014"),
    ("\u00e2\u20ac\u2018", "\u2018"),
    ("\u00e2\u20ac\u2019", "\u2019"),
    ("\u00e2\u20ac\u0153", "\u201c"),
    ("\u00e2\u20ac\u009d", "\u201d"),
    ("\u00e2\u20ac\u00a6", "\u2026"),
    ("\u00e2\u008f\u00ab", "\u23eb"),
    ("\u00c3\u00a2\u00c5\u201c\u00e2\u2026", "\u2705"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repair common mojibake patterns in vault text files."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=str(Path(__file__).resolve().parents[1]),
        help="Vault root to scan. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write repaired files back to disk. Without this flag, run in dry-run mode.",
    )
    parser.add_argument(
        "--extensions",
        nargs="*",
        default=sorted(DEFAULT_EXTENSIONS),
        help="File extensions to scan, with leading dots.",
    )
    return parser.parse_args()


def repair_text(text: str) -> tuple[str, list[tuple[str, str]]]:
    updated = text
    applied: list[tuple[str, str]] = []

    for old, new in REPLACEMENTS:
        if old in updated:
            updated = updated.replace(old, new)
            applied.append((old, new))

    return updated, applied


def iter_text_files(root: Path, extensions: set[str]) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in extensions
    ]


def main() -> None:
    args = parse_args()
    root = Path(args.root)
    extensions = {ext if ext.startswith(".") else f".{ext}" for ext in args.extensions}

    changed: list[tuple[Path, list[tuple[str, str]]]] = []
    for path in iter_text_files(root, extensions):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        updated, applied = repair_text(text)
        if not applied:
            continue

        changed.append((path, applied))
        if args.apply:
            path.write_text(updated, encoding="utf-8")

    if args.apply:
        print(f"applied: {len(changed)} file(s) updated")
    else:
        print(f"dry-run: {len(changed)} file(s) would be updated")

    for path, applied in changed:
        details = ", ".join(f"{old!r}->{new!r}" for old, new in applied)
        print(f"- {path}: {details}")


if __name__ == "__main__":
    main()
