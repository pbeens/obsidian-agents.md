---
name: all-tags-maintenance
description: >
    Rebuild ALL-TAGS.txt by scanning the vault for tag occurrences and writing an alphabetized
    `#Tag (count)` inventory. Use when the user asks to count tags, refresh the tag list, or rebuild
    ALL-TAGS.txt.
---

# All Tags Maintenance

Use this skill when the tag inventory needs to be regenerated from the vault contents.

## Purpose

Rebuild `ALL-TAGS.txt` so it reflects the current vault tag inventory.

## Core Rules

- Read every note markdown file in the vault unless the user explicitly narrows the scope.
- Exclude infrastructure and tooling files unless the user asks otherwise: `.agents/`, `.obsidian/`, `.git/`, `skills/`, `scripts/`, `AGENTS.md`, `tasks.md`, `README.md`, `index.md`, `log.md`, and `ALL-TAGS.txt`.
- Count literal tag occurrences, not unique pages.
- Preserve the exact tag spelling and case that appears in the source.
- Include tags from frontmatter and inline Markdown.
- Ignore false positives from code blocks, inline code, and URL fragments when possible.
- Write the results back to `ALL-TAGS.txt` in the same `#Tag (count)` format already used.
- Sort the output alphabetically by tag text.
- Keep the file to one tag per line.

## Workflow

1. Scan the vault for tag occurrences, preferably by running `scripts/refresh_all_tags.py`.
2. Aggregate counts by exact tag text.
3. Sort alphabetically.
4. Rewrite `ALL-TAGS.txt` in the existing format.
5. Spot-check a few known tags for sanity.
6. Update `tasks.md` if the refresh is part of an active maintenance pass.

## Counting Guidance

- Treat `#AI`, `#ai`, and `#AI-in-Education` as distinct tags if they appear that way in source notes.
- Do not normalize casing unless the user explicitly asks for normalization.
- Do not rename tags just because a better controlled vocabulary exists.
- If the user wants taxonomy cleanup, use the tag-taxonomy workflow separately.

## Output Expectations

When this skill runs, the expected output is:

- an updated `ALL-TAGS.txt`
- a short note in `tasks.md` if this was part of a broader maintenance pass
