# Obsidian Agentic Tasks 🚀

Welcome to the **Obsidian Agentic Tasks** repository! This project is a curated collection of configuration files and "skills" designed to empower agentic AI workflows within [Obsidian](https://obsidian.md/).

> **tl;dr:** [Download the ZIP](https://github.com/pbeens/obsidian-agents.md/archive/refs/heads/main.zip), open it, and extract only the **contents** of the internal subfolder (e.g., `obsidian-agents.md-main`) directly into your Obsidian vault root.

## 📖 Overview

This repository provides the core components needed to turn your Obsidian vault into a powerful workspace for agentic IDEs. By leveraging the `AGENTS.md` file and custom skills, you can streamline complex tasks and enhance your productivity with AI assistance.

## 🛠️ Getting Started

Setting up is quick and easy:

1. **Download the Repository**: Click the green **Code** button and select **Download ZIP** (or [click here](https://github.com/pbeens/obsidian-agents.md/archive/refs/heads/main.zip)).
2. **Extract to Vault**: GitHub wraps ZIP downloads in a folder (e.g., `obsidian-agents.md-main`). Be sure to extract only the **contents** of that folder directly into the **root folder** of your Obsidian vault. (The `AGENTS.md` file must be at the vault root).
3. **Configure Your IDE**: Point your favorite agentic IDE (such as **Antigravity**, **Codex**, or **Claude Code**) to read the `AGENTS.md` file located in your vault root.

Once configured, your agent will have access to the instructions, skills, and scripts defined in this repository.

## 🚀 What can I do with this?

Once configured, you can use natural language to ask your AI agent to perform complex vault maintenance and knowledge management tasks. For example:

- **Morning Briefing**: *"Give me my morning update"* — Compiles critical emails, calendar events, and pending tasks into a single start-of-day note.
- **Meeting Follow-up**: *"Process the transcript for the 2026-04-14 Team Meeting"* — Summarizes transcripts and updates the matching meeting note (the transcript `.srt` and note `.md` must share the same filename).
- **Web Archiving**: *"Capture this URL and add it to my vault"* — Saves a webpage as text-first Markdown (expanding hidden sections) and automatically extracts related people and projects.
- **Knowledge Ingestion**: *"Process my raw folder"* — Ingests new clippings, reconciles people and project pages, and rolls up open tasks.
- **Vault Maintenance**: *"Rebuild my tag list"* — Scans your entire vault to refresh the `#Tag (count)` inventory in `ALL-TAGS.txt`.
- **Entity Management**: *"Create a people page for [Name]"* or *"Update the [Project] project page"* — Manages canonical, alias-friendly pages in `people/` and `projects/`, reconciling new info with existing bios and cross-links.
- **Relationship Extraction**: *"Extract all people and projects from my raw folder"* — Automatically identifies key entities in your clippings and connects them to your knowledge graph.
- **Note Archiving**: *"Archive my clippings from last month"* — Automatically moves notes into a structured `YYYY/MM/` folder hierarchy based on their creation date.

Check the [`skills/`](./skills/) directory for technical details on each specialized workflow.

## 📂 Folder Structure

To keep your vault organized, the agentic workflows utilize the following folder structure:

- **`Daily Notes/`**: Destination for morning briefings and the source for dated archival.
- **`_raw/`**: A staging "inbox" for rough web clippings and raw imports.
- **`_transcripts/`**: The default source folder for meeting transcript files (`.srt` or `.txt`).
- **`people/` & `projects/`**: Where the agent manages canonical entity pages and cross-links.
- **`Clippings/`** & **`Topic Pages/`**: Destinations for cleaned notes promoted from the `_raw/` folder.
- **`Bases/`**: Where the agent looks for or creates structured task overviews and database-style views.
- **`skills/`** & **`scripts/`**: Contains the core logic and automation scripts for the workflows.

## 📄 License

This project is licensed under the **MIT License**. For more information, please see the [LICENSE](./LICENSE) file.
