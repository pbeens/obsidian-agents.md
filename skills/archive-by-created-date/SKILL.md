---
name: archive-by-created-date
description: >
  Archive daily notes or clippings into year/month folders based on the note's created date. Use
  when the user wants to move notes from `Daily Notes/` or `Clippings/` into dated archive folders
  such as `Clippings/2025/12/`.
---

# Archive by Created Date

Use this skill to move notes into a year/month archive structure based on their created date.

## Purpose

Keep `Daily Notes/` and `Clippings/` organized by moving older notes into dated archive folders
without changing their filenames.

## Scope

- Source folders: `Daily Notes/` or `Clippings/`
- Target folders: `Daily Notes/YYYY/MM/` or `Clippings/YYYY/MM/`
- Folder names use a four-digit year and two-digit month.
- Preserve the original filename.

## Created Date Rule

- Read the note's `created` date from frontmatter when available.
- If frontmatter is missing, use the created date shown in the note heading or nearby metadata if the
  date is explicit.
- Route the note to the matching `YYYY/MM/` folder.
- If the date cannot be determined confidently, stop and ask for guidance.

## Confirmation Rule

- Always confirm the move plan before changing files.
- State the source folder, file count, target year/month folder, and whether the move affects daily
  notes or clippings.
- Do not move files until the plan has been confirmed.

## Workflow

1. Identify candidate notes in the source folder.
2. Read the created date for each note.
3. Group notes by year and month.
4. Confirm the planned move with the user.
5. Create the target `YYYY/MM/` folders if needed.
6. Move the notes into the matching archive folders.
7. Update the nearest folder README or index if one exists.
8. Leave filenames unchanged unless the user asks for renaming.

## Safety

- Do not copy files when the user asked to move them.
- Do not invent dates.
- Do not move notes whose created date is unclear.
- Do not rename files during archival unless explicitly requested.
- Keep the archive structure consistent between `Daily Notes/` and `Clippings/`.

## Output Expectations

- Notes moved into the appropriate year/month folder.
- The move plan confirmed before the change.
- Folder indexes updated when needed.
