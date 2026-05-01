#!/usr/bin/env python3
"""Copy a cleaned markdown source block to the clipboard.

This helper accepts a local file path, file:// URL, or http(s) URL, strips YAML
front matter and any existing keyword section, then copies the remaining text to
the Windows clipboard.
"""

from __future__ import annotations

import argparse
import re
import sys
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse, unquote
from urllib.request import Request, urlopen


FRONTMATTER_RE = re.compile(r"^---\r?\n.*?\r?\n---\r?\n?", re.S)
KEYWORDS_HEADING_RE = re.compile(r"(?ims)^(?:#{1,6}\s*)?(?:\*\*)?Keywords(?:\*\*)?\s*:?\s*$")
NEXT_HEADING_RE = re.compile(r"(?m)^#{1,6}\s+\S")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy cleaned source text from a file or URL to the clipboard."
    )
    parser.add_argument(
        "source",
        help="Local markdown path, file:// URL, or http(s) URL to copy from.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Also print the cleaned text to stdout.",
    )
    return parser.parse_args()


def read_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        request = Request(source, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=60) as response:
            data = response.read()
        return data.decode("utf-8")

    if parsed.scheme == "file":
        local_path = Path(unquote(parsed.path))
        return local_path.read_text(encoding="utf-8")

    return Path(source).read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n") or text.startswith("---\r\n"):
        match = FRONTMATTER_RE.match(text)
        if match:
            return text[match.end() :]
    return text


def strip_keyword_section(text: str) -> str:
    match = KEYWORDS_HEADING_RE.search(text)
    if not match:
        return text

    start = match.start()
    tail = text[match.end() :]
    next_heading = NEXT_HEADING_RE.search(tail)
    end = match.end() + (next_heading.start() if next_heading else len(tail))
    return text[:start] + text[end:]


def clean_text(text: str) -> str:
    text = strip_frontmatter(text)
    text = strip_keyword_section(text)
    return text.lstrip("\r\n")


def copy_to_clipboard(text: str) -> None:
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", suffix=".txt") as tmp:
        tmp.write(text)
        temp_path = tmp.name

    try:
        completed = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                f"Get-Content -Raw -Encoding UTF8 -Path '{temp_path}' | Set-Clipboard",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if completed.returncode != 0:
            raise SystemExit(
                "Failed to copy to clipboard via PowerShell: "
                + completed.stderr.strip()
            )
    finally:
        Path(temp_path).unlink(missing_ok=True)


def main() -> None:
    args = parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    text = read_source(args.source)
    cleaned = clean_text(text)
    copy_to_clipboard(cleaned)

    if args.stdout:
        sys.stdout.write(cleaned)
    else:
        print(f"Copied cleaned text to clipboard from: {args.source}")


if __name__ == "__main__":
    main()
