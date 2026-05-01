---
name: wiki-people-projects-tasks
description: >
  After wiki-ingest or wiki-history-ingest, consolidate detected people, projects, and open tasks into
  alias-friendly wiki pages in the dedicated people/ and projects/ folders and roll up tasks into overview views.
---

# Wiki People, Projects & Task Consolidation

**Use this skill immediately after** `wiki-ingest`, `data-ingest`, or `wiki-history-ingest`. It is a post-processing pass.

## Purpose
Turn newly processed material into durable, alias-friendly People and Project pages plus consolidated task overviews, while preserving provenance and avoiding duplicates.

## Invocation Examples
- "Run wiki-ingest on _raw/ then apply wiki-people-projects-tasks"
- "Process raw folder and consolidate people/projects/tasks"
- "After history ingest, run people/project/task consolidation"
- "wiki-people-projects-tasks"

## Before You Start
1. Run the appropriate ingest skill first (`wiki-ingest` for _raw/, `wiki-history-ingest codex` for history, etc.).
2. Read this `AGENTS.md` and current `tasks.md`.
3. Check `.manifest.json`, `people/`, `projects/`, `Bases/`, and existing task overview files.

## Core Order
1. Ingest first.
2. Reconcile People and Project entities.
3. Consolidate open tasks.
4. Update indexes/READMEs and log changes.

## People Rules
- Prefer creating or updating the page in the `people/` folder.
- Use root or another appropriate folder only when it clearly fits the vault's existing organization better.
- Always use alias-friendly naming: clean, readable filename + rich `aliases:` YAML frontmatter (nicknames, short forms, spelling variations, context-specific references).
- Include: short bio stub, key facts, related projects, related tasks/links.
- Merge new information safely into the best existing canonical page (check filename + aliases).
- Preserve provenance markers; prefer additive edits over wholesale overwrites.
- Every people page must include `## Overview`, `## Related Projects`, and `## Related Notes`, even when some sections are empty.
- Every newly created or updated people page must include at least one explicit source reference in `## Related Notes`.
- The source reference must point to the originating note or file that caused the people page to be created.
- If no related project is detected, still include the source note under `## Related Notes`.
- Do not leave a people page without provenance just because there is no related project.
- When linking the source note, prefer an explicit path-based wikilink or otherwise unambiguous source reference.
- Every people page must include `## Overview`, `## Related Projects`, and `## Related Notes`, even when some sections are empty.
- Every newly created or updated people page must include at least one explicit source reference in `## Related Notes`.
- The source reference must point to the originating note or file that caused the people page to be created.
- If no related project is detected, still include the source note under `## Related Notes`.
- Do not leave a people page without provenance just because there is no related project.
- When linking the source note, prefer an explicit path-based wikilink or otherwise unambiguous source reference.

## Project Rules
- Prefer creating or updating the page in the `projects/` folder.
- Include: description, current status, related people, key tasks, aliases.
- Check both filename and aliases before creating anything new; merge when possible.
- Preserve provenance when combining sources.

## Duplicate Detection & Merging
- Search by exact filename and by aliases/variations before creating a new page.
- Merge intelligently into the strongest existing page rather than duplicating.
- If information conflicts, add a clear "Note on conflicting sources" callout instead of guessing.

## Task Consolidation
- After entity pages are updated, scan the newly processed notes for open tasks.
- Roll them up into overview views.
- **Strong preference**: Update or append to existing patterns in `Bases/` or `All Tasks.md`.
- Use the kepano `obsidian-bases` skill to create or enhance structured Bases views when appropriate (e.g., a "Consolidated Open Tasks" base with filters).
- If no suitable overview exists, create or update a simple Markdown file such as `Consolidated Open Tasks.md`.
- Keep consolidated views concise, actionable, and non-duplicative.
- Copy task text exactly as it appears in the source note; do not paraphrase or synthesize task wording.
- Preserve inline hashtags from the source task line verbatim when copying tasks into project pages or
  rollups; do not strip tags such as `#today`, `#TRC`, `#Google-Doc`, or `#Google-Sheet`.

## Clean Note Creation Rules

After `wiki-ingest` and `wiki-people-projects-tasks` have reconciled people, projects, and tasks, create a clean final note using the Obsidian Notes Custom GPT style below.

### Clean Note Destination

- Save the clean note to `Clippings/` by default.
- Use `Topic Pages/` or another more contextually appropriate location when the content clearly fits an existing canonical topic area better than a clipping.
- Use the article title as the filename whenever possible so clipping notes stay title-aligned with the source. If a character is filesystem-invalid, use the closest safe substitute only for that character.
- Every newly created clean note must begin with YAML frontmatter.
- Include frontmatter fields such as `created`, `source`, `tags`, and any needed aliases or provenance metadata.
- Add tags such as `#processed`, `#clipping`, `#from-raw`, plus source URL/date if available.
- Add wikilinks from the relevant People and/or Project pages to the clean note.
- When creating the clean note in `Clippings/`, strictly follow the Custom GPT style.
- Do not embed or copy images from the raw file unless they are essential for understanding; prefer describing image content in text or using a lightweight link instead of embedding the full file to avoid bloat.
- After the clean note is successfully created and verified, delete the original raw `.md` file and any locally copied images that were only attached to it from `_raw/`.
- Do not leave raw files or their associated images in `_raw/` long-term.
- If images from the raw file are no longer referenced anywhere after deletion, note this in the processing summary so the user can optionally run an orphaned-image cleanup later.
- After the clean note is created, append a numbered list item or wikilink at the very bottom of the current daily note, typically under `## Stuff to Process`.
- Do not place the item in the `# ✂️ Clippings` section anymore; keep the daily note entry separate so the user can move it manually later.
- Use a section-only or end-of-file append for daily-note updates; never rewrite the whole file just to add the new item.
- Preserve the note's existing UTF-8/Unicode content when editing daily notes; do not round-trip the note through terminal text output.

### Raw Folder Command Behavior

When the user says "Process raw folder" or a similar short command, run the full chain:

1. `wiki-ingest`
2. `wiki-people-projects-tasks`
3. clean note creation using the Custom GPT style
4. delete the raw file and any associated images from `_raw/`
5. append the new item as a numbered list item to the bottom of today's daily note

### Obsidian Notes Custom GPT Instructions

**You turn messy or complex information—like raw text, transcripts, or documents—into clean, clear, and useful Obsidian-style notes.**

You don’t just summarize. You explain, structure, and highlight what really matters so the user understands and remembers it.

## What You Do

- Use **Obsidian-flavored Markdown**, with smart use of headings, callouts, lists, and formatting for clarity.
- Keep notes clear and helpful—optimized for reading, linking, and thinking.
- Always aim to make the “main idea” obvious and memorable.
- If something’s unclear, start with a `> [!NOTE]` explaining your approach or asking for a quick clarification.

## When Things Get Complicated

If the source is dense, technical, or confusing:

- Break it down.
- Strip out fluff and jargon.
- Rebuild it using clear language and examples, if helpful.

If the input is too broken or messy to work with, don’t fake it. Just return:

````text
> [!WARNING] The input is too unclear to turn into a useful note. Please revise or provide more context.
````

## Formatting Rules

- **Filename (Line 1)**: Short and clear, max 15 characters, no `.md`.
- **Title (Line 2)**: Markdown title (`#`).
- **Body (Line 3 onward)**: Well-structured content.

### Don’ts

- Don’t use `[[double brackets]]`
- Don’t write chatty intros—just give the note
- NEVER use horizontal rules (`---`) for any reason.

## Style Tips

Use Obsidian tools like:

- `#`, `##`, etc. for structure
- `> [!NOTE]`, `> [!TIP]`, etc. for key ideas
- **Bold** for core ideas
- _Italics_ for emphasis
- `==Highlight==` sparingly
- Bullet lists and tables when they help

## Example Output Template

````text
SocialFlywheel
# How to Grow with Organic Social Media
> [!NOTE] I’m focusing on tactics and growth strategy, as requested.

## Key Mindset

> [!ABSTRACT]
> 1. Take the long view
> 2. Share progress, not perfection
> 3. Iterate fast

## The Four Stages

### 1. Warm Up
- Teach the platform who you are
- Follow and save content in your niche

### 2. Iterate
- Post regularly
- Watch what performs well
- Adjust quickly

## Pitfalls to Avoid

> [!WARNING]
> - Don’t give up too early
> - Don’t automate too soon
> - Avoid salesy content

## Ideas to Apply

> [!HINT]
> This model pairs well with MVP thinking and “building in public” strategies.
````

## Markdown & Obsidian Rules
- Follow kepano/obsidian-skills conventions for:
  - YAML frontmatter (including `aliases`)
  - Callouts
  - Wikilinks
  - Obsidian Bases syntax
  - Clean, readable Markdown

## Safety Rules
- Keep all changes minimal, reviewable, and additive where possible.
- Never delete or overwrite large sections without explicit user confirmation.
- Always preserve provenance and existing links.
- If uncertain about a merge, create a clear note and ask for guidance.

## Supported Workflows
- Forward ingest from `_raw/`
- Backfill from Codex history via `wiki-history-ingest codex`
- Any other content routed through obsidian-wiki ingest skills

## Output Expectations
When finished the agent should report:
- Which People and Project pages were created or updated
- Where tasks were consolidated
- Any indexes/READMEs that were updated
- A brief summary of changes made
