---
name: web-page-to-raw
description: >
  Capture a web page into `_raw/` as a text-first Markdown note by expanding flyouts, accordions,
  tabs, and other hidden text sections, preserving headings and tables, and omitting graphics and
  decorative layout. Use when the user says "capture this page", "save this webpage to raw",
  "process this URL", or wants a website archived as raw text before vault ingest.
---

# Web Page to Raw

Use this skill to turn a web page into a text-first raw note in `_raw/`.

## Purpose

Capture the page's text content faithfully for later vault ingestion while avoiding image bloat and lost hidden text.

## Core Rules

- Expand all flyouts, accordions, `details/summary` sections, tabs, load-more panels, and similar
  hidden content before capturing.
- Keep expanding until no new text appears.
- Do not summarize, interpret, or rewrite the page content.
- Preserve headings and tables.
- Ignore decorative graphics, icons, and layout images.
- Do not try to preserve column-based page layout; retain tables only when the source uses real tables.
- Keep hyperlinks as links.
- Capture visible page text in a raw, source-first form.
- For Reddit pages, expand all visible comment threads, nested replies, and "more replies" / load-more
  controls until the conversation tree no longer reveals new text.
- If a section cannot be expanded, note that explicitly in the raw file.

## Capture Workflow

1. Open the URL.
2. Inspect for expandable sections and click every content-bearing control.
3. Revisit the page after expansions to ensure no additional text is hidden.
4. Capture the visible content into a Markdown note in `_raw/`.
5. Use a readable title-based filename with filesystem-safe characters.
6. Include source URL and capture date in frontmatter.
7. Omit images unless the user explicitly asks for them.

## Raw Note Structure

Prefer this structure in the captured note:

- frontmatter with `source`, `captured`, and `title`
- H1 title
- section headings that mirror the page
- bullet lists and Markdown tables where appropriate
- short notes for any hidden sections that could not be expanded
- when a page is a discussion thread, include the post and the visible comments without summarizing them

## Quality Checks

- Confirm the raw note contains the page's main headings and visible body text.
- Confirm tables survived as Markdown tables.
- Confirm no images were copied into `_raw/`.
- Confirm any hidden sections were expanded or noted.
- For Reddit captures, confirm nested comments and visible reply branches were included, not just the
  top-level post and first comment layer.

## Output

When this skill runs, the expected result is a Markdown file in `_raw/` containing the page text, headings, tables, and visible discussion content, ready for later vault ingest.
