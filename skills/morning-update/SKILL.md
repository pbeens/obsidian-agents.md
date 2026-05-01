---
name: morning-update
description: >
    Create or update a dated Morning Update note by compiling critical Gmail from the last 24 hours,
    today's calendar events, and #today items from the previous three days of Obsidian notes. Use when
    the user asks for a daily morning briefing, a YYYY-MM-DD Morning Update file, or a consolidated
    start-of-day update note.
---

# Morning Update

Use this skill to build a daily `YYYY-MM-DD Morning Update` note in `Daily Notes/`.

## Purpose

Create one concise note that surfaces:

- critical Gmail from the last 24 hours
- all calendar events for the target day
- `#today` items from notes dated in the last three calendar days

## Workflow

1. Determine the target date in the user's local timezone.
2. Create or update `Daily Notes/YYYY-MM-DD Morning Update.md`.
3. Gather Gmail items from the last 24 hours.
4. Gather calendar events for the target date.
5. Scan Obsidian notes from the target date and previous two days for `#today`.
6. Write the note with clear sections and preserve source wording where relevant.

## Gmail

- Treat "critical" conservatively.
- Prioritize unread, starred, important, or directly actionable mail from the last 24 hours.
- Include sender, subject, received time, and a brief why-it-matters note.
- Format each Gmail item as a checklist item.
- include the Gmail message or thread URL for each critical item when available
- if a direct URL is unavailable, include the message/thread ID and subject as a fallback
- If an item is ambiguous, include it under a review-oriented sublist instead of guessing.
- Do not invent urgency.

## Calendar

- List every event for the target day as a checklist item.
- Include start/end time, title, location, attendees, and meeting link when available.
- Keep all-day events visible.
- If the calendar is empty, say so explicitly.

## Obsidian Scan

- Search markdown notes in the vault for `#today` items in notes dated within the target day and the previous two calendar days.
- Use the note's date-only filename when present, otherwise use `created` frontmatter if available.
- Copy `#today` task text exactly as written.
- Preserve inline hashtags verbatim.
- Include the source note path next to each copied item.

## Note Format

Use this structure:

1. YAML frontmatter with `created: YYYY-MM-DD`, `source: "[[skills/morning-update/SKILL.md]]"`, and `tags: [Morning-Update]`
2. Overview
3. Critical Gmail
4. Calendar Today
5. `#today` Items
6. Follow-Ups
7. Do not include an H1 title if the filename already serves as the note title.

In `## Critical Gmail`, format each email as `- [ ]` rather than a bullet.
In `## Calendar Today`, format each event as `- [ ]` rather than a bullet.

## Safety Rules

- Keep the note concise and source-faithful.
- Do not paraphrase task text.
- Do not rewrite source notes.
- If a source cannot be dated confidently, skip it rather than guessing.
