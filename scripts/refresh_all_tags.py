from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re


VAULT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = VAULT_ROOT / "ALL-TAGS.txt"

EXCLUDED_DIRS = {
    ".agents",
    ".codex",
    ".git",
    ".obsidian",
    "scripts",
    "skills",
}

EXCLUDED_FILES = {
    "AGENTS.md",
    "ALL-TAGS.txt",
    "README.md",
    "index.md",
    "log.md",
    "tasks.md",
}

TAG_BODY_RE = re.compile(r"(?<![\w/])#([\w-]+(?:/[\w-]+)*)")
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", re.S)
TAG_LINE_RE = re.compile(r"^\s*tags:\s*(.*)$", re.I)
LIST_ITEM_RE = re.compile(r"^\s*-\s*(.+?)\s*$")


def should_exclude(path: Path) -> bool:
    if path.name in EXCLUDED_FILES:
        return True
    return any(part in EXCLUDED_DIRS for part in path.parts)


def clean_tag(value: str) -> str:
    tag = value.strip().strip("'\"")
    if tag.startswith("#"):
        tag = tag[1:]
    return tag.strip()


def should_keep_tag(tag: str) -> bool:
    return bool(tag) and not tag.isdigit()


def parse_frontmatter_tags(frontmatter: str) -> list[str]:
    tags: list[str] = []
    lines = frontmatter.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        match = TAG_LINE_RE.match(line)
        if not match:
            i += 1
            continue

        rest = match.group(1).strip()
        if rest:
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                if inner:
                    for piece in inner.split(","):
                        tag = clean_tag(piece)
                        if should_keep_tag(tag):
                            tags.append(tag)
            else:
                tag = clean_tag(rest)
                if should_keep_tag(tag):
                    tags.append(tag)
            i += 1
            continue

        i += 1
        while i < len(lines):
            current = lines[i]
            if not current.strip():
                i += 1
                continue
            if not current.startswith((" ", "\t")):
                break
            item = LIST_ITEM_RE.match(current)
            if item:
                tag = clean_tag(item.group(1))
                if should_keep_tag(tag):
                    tags.append(tag)
            i += 1

    return tags


def strip_noise(body: str) -> str:
    text = re.sub(r"(?ms)```.*?```", " ", body)
    text = re.sub(r"(?ms)~~~.*?~~~", " ", text)
    text = re.sub(r"(?<!`)`[^`]+`(?!`)", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[\[[^\]]+\]\]", " ", text)
    text = re.sub(r"(?i)\bhttps?://\S+", " ", text)
    return text


def extract_tags(text: str) -> list[str]:
    tags: list[str] = []
    body = text

    match = FRONTMATTER_RE.match(text)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        tags.extend(parse_frontmatter_tags(frontmatter))

    body = strip_noise(body)
    for found in TAG_BODY_RE.findall(body):
        tag = clean_tag(found)
        if should_keep_tag(tag):
            tags.append(tag)

    return tags


def main() -> None:
    counts: dict[str, int] = defaultdict(int)

    for path in sorted(VAULT_ROOT.rglob("*.md")):
        if should_exclude(path):
            continue

        text = path.read_text(encoding="utf-8")
        tags = extract_tags(text)
        for tag in tags:
            counts[tag] += 1

    ordered = sorted(counts, key=lambda tag: (tag.lower(), tag))
    lines = [f"#{tag} ({counts[tag]})" for tag in ordered]
    OUTPUT_FILE.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")
    print(f"Wrote {len(lines)} tags to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
