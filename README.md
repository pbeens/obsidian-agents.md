# Obsidian Agentic Tasks 🚀

Welcome to the **Obsidian Agentic Tasks** repository! This project is a curated collection of configuration files and "skills" designed to empower agentic AI workflows within [Obsidian](https://obsidian.md/).

## 📖 Overview

This repository provides the core components needed to turn your Obsidian vault into a powerful workspace for agentic IDEs. By leveraging the `AGENTS.md` file and custom skills, you can streamline complex tasks and enhance your productivity with AI assistance.

## 🛠️ Getting Started

Setting up is quick and easy:

1. **Download the Repository**: Click the green **Code** button and select **Download ZIP** (or [click here](https://github.com/pbeens/obsidian-agents.md/archive/refs/heads/main.zip)).
2. **Extract to Vault**: GitHub wraps ZIP downloads in a folder (e.g., `obsidian-agents.md-main`). Be sure to extract only the **contents** of that folder directly into the **root folder** of your Obsidian vault. (The `AGENTS.md` file must be at the vault root).
3. **Configure Your IDE**: Point your favorite agentic IDE (such as **Antigravity**, **Codex**, or **Claude Code**) to read the `AGENTS.md` file located in your vault root.

Once configured, your agent will have access to the instructions, skills, and scripts defined in this repository.

## 🧰 Included Skills

This repository also includes a set of specialized skills to extend your agent's capabilities:

- **All Tags Maintenance**: Rebuilds `ALL-TAGS.txt` by scanning the vault for tag occurrences and counts.
- **Archive by Created Date**: Archives daily notes or clippings into year/month folders (e.g., `YYYY/MM/`) based on their creation date.
- **Meeting Transcript Summary**: Summarizes meeting transcripts (`.srt` or `.txt`) into meeting notes, extracting action items and decisions.
- **Morning Update**: Creates a daily briefing note by compiling critical emails, calendar events, and `#today` tasks from Obsidian.
- **Web Page to Raw**: Captures web pages into `_raw/` as text-first Markdown, expanding hidden sections and preserving tables.
- **Wiki People, Projects & Tasks**: Consolidates detected entities and open tasks into alias-friendly wiki pages and task overviews.

Check the [`skills/`](./skills/) directory for details on each skill.

## 📄 License

This project is licensed under the **MIT License**. For more information, please see the [LICENSE](./LICENSE) file.
