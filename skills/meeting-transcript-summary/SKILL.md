---
name: meeting-transcript-summary
description: >
    Summarize meeting transcripts from .srt files into the matching meeting note by adding or updating
    an `## AI summary` section with a neutral, outcome-oriented summary, decisions, action items, open
    questions, discussion notes, and references. Use when the user says "process transcripts" or provides
    a transcript filename such as `2026-04-14 Team Meeting.srt`.
---

# Meeting Transcript Summary

Use this skill when a meeting transcript needs to be merged into the corresponding meeting note. The source may be `.srt` (for example from MacWhisper) or `.txt` (for example from Pixel / Google recordings).

## Purpose

Turn transcript text into a concise meeting summary that helps follow-up and future reference without inventing details.

## Routing

- Match the transcript to the meeting note by filename stem whenever possible.
- Transcript filenames usually mirror the meeting note name, with `.srt` instead of `.md`.
- Read transcripts from `_transcripts/` by default.
- Accept either `.srt` or `.txt` transcript files.
- Normalize titles to Unicode NFC for matching only, and preserve the canonical Unicode spelling already present in the note or resolved from the filename.
- If the target note already exists, add or update a bottom-of-file `## AI summary` section.
- If no target note exists, create the most specific matching meeting note with YAML frontmatter and add the summary there.
- If the transcript is not actually a meeting note, do not force it into a daily note; route the cleaned note to `Clippings/` with YAML frontmatter instead.

## Core Rules

- Do not invent or extrapolate beyond the transcript.
- Preserve the original intent and meaning.
- Strictly preserve all hyperlinks, including Markdown links and HTML links.
- Summarize neutrally.
- De-duplicate repetitive material while keeping important participant input.
- Correct spelling and grammar only when it improves clarity.
- Prioritize clarity over completeness when input is fragmented.

## Output Structure

Use this default structure inside `## AI summary` unless the note already uses a stronger local format:

1. Meeting Summary
2. Key Decisions
3. Action Items
4. Open Questions / Risks
5. Discussion Notes
6. Resources / References

## Formatting Rules

- Use Obsidian Markdown.
- Use `- [ ]` for action items.
- Keep links intact and in place.
- Keep summaries concise and scannable.
- Put the summary under `## AI summary` at the bottom of the meeting note.
- Any newly created note must start with YAML frontmatter.
- Do not convert action items into plain bullets or prose; preserve them as task checkboxes inside the AI summary.

## Transcript Folder Guidance

- `_transcripts/` is the canonical intake folder for transcript files.
- Use `_transcripts/` only as source intake.
- Keep the canonical summary in the meeting note, not in the transcript file.
- Treat transcript files as transient source files unless the user explicitly asks to retain them elsewhere.

## Safety Rules

- Do not synthesize action items or decisions.
- Do not strip or rewrite links.
- Do not replace an existing summary unless the transcript clearly supports the change.
- Transcript ingest is append-only for existing notes: only add the `## AI summary` block to the matching meeting note and, if the local vault convention requires it, append a single daily-note pointer. Do not rewrite other lines, normalize unrelated content, or run cleanup transforms during transcript ingest.
- If the note already contains task lines, preserve every checkbox, emoji field, and completion date exactly as written. Do not rewrite `- [ ]` / `- [x]` syntax, `✅` completion markers, or any other Tasks plugin metadata while appending the summary.
- Keep the source note link or filename context visible when helpful.

## Output Expectations

When this skill runs, the expected result is:

- the matching meeting note updated with an `## AI summary` section
- action items, decisions, and open questions extracted from the transcript
- hyperlinks preserved exactly
