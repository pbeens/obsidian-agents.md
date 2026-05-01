# AGENTS.md

> [!TIP]
> If `AGENTS2.md` exists in the root, read it for additional local maintenance and privacy rules.


## Purpose

This vault is a personal Obsidian knowledge wiki. Agents should turn incoming material into clean, linked notes, with canonical People pages, canonical Project pages, and usable task views.

## Scope

- Work only within this vault unless explicitly told otherwise.
- Preserve the existing vault structure where possible.
- Do not bulk-migrate, rename, or rewrite legacy notes without approval.
- Prefer minimal, reviewable changes that solve the current request.

## Expected Deliverables

- Canonical `people/` notes for people entities.
- Canonical `projects/` notes for project entities.
- Clean notes promoted from `_raw/`.
- Task overviews built with Obsidian Tasks, Bases, or simple Markdown lists.
- Reusable local skills and shared scripts when a workflow repeats.

## Folder Map

- `README.md`: root entrypoint and navigation.
- `AGENTS.md`: durable agent rules and folder map.
- `tasks.md`: active work, blockers, and handoff notes.
- `_raw/`: staging inbox for clipped or rough material.
- `people/`: canonical people pages.
- `projects/`: canonical project pages.
- `skills/`: reusable vault-specific workflows.
- `scripts/`: shared utilities and validation helpers.
- Existing folders like `Topic Pages/`, `Bases/`, `Daily Notes/`, and `Clippings/` remain valid parts of the vault.

## Daily Note Convention

- A daily note means a note whose filename is only a date, typically `YYYY-MM-DD.md`.
- Treat notes with a date plus extra words in the filename as ordinary notes, not daily notes.
- When the user asks to process a folder or all files in a folder, do not assume daily notes are included unless the user explicitly says so.
- When the user says "daily note", target the date-only note for that day.
- If a workflow needs a daily note destination, use the date-only file for the relevant day rather than creating a titled note.

## Working Rules

- Read `AGENTS.md` first, then `tasks.md` when active work is being tracked.
- Keep `AGENTS.md` concise and durable.
- Do not turn `AGENTS.md` into a session log or changelog.
- Store changing plans, blockers, and progress in `tasks.md`.
- Ask before major structural changes, mass renames, or folder moves.
- Make only the changes needed for the current request.
- Use lowercase, filesystem-friendly names for new folders unless the user explicitly asks otherwise.
- Normalize new people filenames to lowercase kebab-case unless the user explicitly requests a different convention.
- Treat entity page names as alias-friendly, with readable canonical titles and variant aliases handled explicitly.
- Promote cleaned notes out of `_raw/`; do not leave raw imports as the canonical record.

## Wiki Workflow Rules

- When the user says "process raw", "process \_raw/", "process raw folder", "ingest raw", or similar short commands, automatically run `wiki-ingest` on the `_raw/` folder followed by the `wiki-people-projects-tasks` skill. Do not ask for confirmation unless there are many files or potential large changes.
- When a project note lists related people, ensure each related person has a People page; create any missing pages in `people/_new/` for manual review and update any existing person pages as needed.
- When linking related people from a project note, use explicit path-based wikilinks into `people/` or `people/_new/` rather than bare name-only links.
- Use the obsidian-wiki framework as the primary ingest and page-creation engine. It handles `_raw/` processing, delta tracking via `.manifest.json`, entity extraction, merging, wikilinking, and provenance.
- Always load and respect skills from kepano/obsidian-skills for proper Obsidian Markdown, Bases, wikilinks, aliases, and callouts.
- After ingest, chain the `wiki-people-projects-tasks` skill to reconcile People pages, Project pages, and task overviews.
- When creating People or Project pages, prefer the alias-friendly rule already set here. The agent may place pages in `people/` or `projects/` when the entity clearly belongs there, or in root / appropriate project subfolders when obsidian-wiki's natural organization suggests it.
- Core command for ingest: `Run wiki-ingest on _raw/` followed by applying custom people/project/task consolidation rules.
- For social media threads (e.g., Twitter/X, Reddit), do not extract or create pages for related people other than the primary poster/author.

## Wiki-Specific Rules

- Drop web clips and raw material into `_raw/`.
- Agent command: `Process raw folder` or `wiki-ingest` -> clean, link, extract people/projects/tasks -> promote to canonical pages.
- After ingest, run `wiki-people-projects-tasks` to consolidate alias-friendly people and project pages, roll up open tasks, and create a clean note in `Clippings/` or `Topic Pages/` using the Obsidian Notes Custom GPT instructions.
- When archiving notes from `Daily Notes/` or `Clippings/`, use `archive-by-created-date` so moves go into `YYYY/MM/` folders after confirming the plan.
- For transcript files (`.srt` from MacWhisper or `.txt` from Pixel/Google recordings), always use `meeting-transcript-summary` to append an `## AI summary` section to the matching meeting note.
- The `## AI summary` for a transcript must include extracted action items as `- [ ]` tasks when the transcript contains them; do not collapse them into plain bullets.
- Transcript processing is append-only for existing notes: append the summary block, and if the vault convention requires it, append a single daily-note pointer. Do not rewrite other lines, normalize unrelated text, or update project/person pages as part of transcript ingest.
- If title text or workspace state is garbled, handle it as a separate explicit maintenance task with `scripts/repair_mojibake.py`; do not run repair as part of transcript ingest.
- Treat existing task lines as verbatim syntax. Preserve `- [ ]` / `- [x]`, emoji-based task metadata, and completion dates exactly as they appear; do not rewrite completed-task markers, done dates, recurrence icons, or other task status fields when editing unrelated note content.
- Store incoming transcript files in `_transcripts/`; they are transient source files, not canonical notes.
- For webpages that should be archived as text first, use `web-page-to-raw` to expand hidden sections, preserve headings/tables, omit graphics, and save the result in `_raw/`.
- Clipping filenames should preserve the article title whenever possible instead of being slugified; use filesystem-safe substitutions only where required.
- After a clean note is created and verified, delete the original raw file and any associated images so they do not remain in `_raw/`.
- Before assigning or creating tags, consult `ALL-TAGS.txt` first and reuse an existing tag when possible. Only introduce a new tag when no existing tag fits.
- When copying task rollups into project pages, preserve inline hashtags from the source task line verbatim instead of stripping them.
- Copy task wording exactly as it appears in the source note; do not paraphrase or synthesize task text.
- After a clean note is created, append a numbered list item for it at the bottom of the relevant daily note in the same change, typically under `## Stuff to Process`. This is required for raw/clipping/transcript processing, not optional.
- Use a section-only or end-of-file append for daily-note updates; never rewrite the whole daily note just to add the new item.
- Preserve the file's existing Unicode/UTF-8 content when editing daily notes; do not round-trip the note through terminal text output.
- Consolidated task views should leverage existing `Bases/` or `All Tasks.md` patterns when possible.
- Use obsidian-bases skill for structured task/project views.

## Skills and Scripts

- Put reusable workflows in `skills/`.
- Put shared utilities in `scripts/`.
- When a workflow repeats or is likely to repeat, propose a new skill.
- When a workflow needs deterministic cleanup, linking, conversion, or validation, propose a script.
- Use `all-tags-maintenance` when rebuilding `ALL-TAGS.txt` from the vault's current tag usage.
- Use `archive-by-created-date` for year/month archival moves of daily notes or clippings.

## Documentation and Navigation

- If a folder gains multiple documents and has no index, add a minimal `README.md`.
- When a document is created or moved, update the nearest relevant index or README in the same change.
- Keep internal links relative.
- Keep `Related Notes` sections on project pages in chronological order by source date, and re-sort
  the section whenever a new meeting note is added.
- Keep project pages open-task only: remove completed checkboxes from project files as soon as they are
  completed, and do not leave finished tasks behind in project pages.

## Task Handling

- Use `tasks.md` for active work, next steps, blockers, and handoff notes.
- Keep task items concrete and outcome-based.
- Mark completed items before ending a session.
- Do not use `tasks.md` as a content note or as a substitute for vault-wide task pages.

## Safety and Change Control

- Do not delete or move large note sets without approval.
- Do not rewrite legacy notes just to standardize them.
- Make structure changes only when they solve a current need.
- If a workflow is repeated, capture it as a skill or script instead of leaving it as ad hoc tribal knowledge.

## Skill Opportunity Detection

- If the same agent workflow appears more than once, flag it as a candidate for `skills/`.
- If the same mechanical transformation or validation appears more than once, flag it as a candidate for `scripts/`.
- Keep proposed skills and scripts small, focused, and easy to review.

> [!NOTE]
> This project was initialized using the agentic master prompt provided by [AgenticProjectInitializer](https://github.com/pbeens/AgenticProjectInitializer/blob/main/master-prompt.md).
