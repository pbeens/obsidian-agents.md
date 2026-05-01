# PROMPTS.md

## Mission Statement
This file serves as a collaborative log between the user and the AI assistant (Antigravity). It documents the intent, the actual prompts used, and the technical context of each change to maintain transparency, track progress, and provide a historical record of the repository's evolution.

### User Prompt 1 – 2026-05-01 15:05 – GitHub Description Request
**Goal:** Generate a short description for the GitHub repository.
**Prompt:** Can you give me a short description to use in GitHub?
**Technical Context:** Reviewed README.md and AGENTS.md to understand the project scope. Provided four options for the repository description.

### User Prompt 2 – 2026-05-01 15:07 – Clarify ZIP Extraction Instructions
**Goal:** Update README.md to warn users about GitHub's ZIP file folder nesting.
**Prompt:** One thing they have to watch for is if they download the zip, it's going to have everything in a folder, so they have to extract everything from that folder. I'll show you exactly what I mean. D:\My Documents\Downloads\obsidian-agents.md-main.zip\obsidian-agents.md-main\
**Technical Context:** Updated `README.md` step 2 under "Getting Started" to explicitly mention navigating into the nested folder before extracting to the vault root.

### User Prompt 3 – 2026-05-01 15:09 – Update Skills in README
**Goal:** Review the `skills/` folder and update the `README.md` with the correct skills.
**Prompt:** I think you need to review the Skills that are in there, because the generic ones that I had in my user profile I did not include here. These are only the ones that I use for Obsidian maintenance. Some of those other ones that you had were related to other projects. Review the Skills folder and then update the README accordingly.
**Technical Context:** Listed `skills/` directory, read `SKILL.md` for each skill, and updated `README.md` with accurate descriptions. Removed placeholder skills.
