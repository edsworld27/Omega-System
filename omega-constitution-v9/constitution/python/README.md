# 🐍 Omega Automation Library

This directory contains the self-healing and continuous-monitoring Python scripts that keep the Omega project intact and secure.

> [!IMPORTANT]
> **NO EDITS OR DELETIONS:** This folder is designed to only be added to. Do not mutate or delete existing `.py` files here unless absolutely necessary.

## The Scripts

- `auto_changelog.py`: Generates and maintains a `CHANGELOG.md` file whenever anything in the project is added, modified, or deleted.
- `auto_security.py`: Continuously scans the `USER SPACE` folder to ensure no raw passwords, `.env` data, or `.pem` keys are accidentally written into the project. It heals by redacting them or warning you.
- `auto_structure.py`: Ensures the core 4 Pillars (`START HERE`, `CONSTITUTION`, `USER SPACE`, `STORE`) always exist. If a system or user accidentally drops one, it is instantly recreated to prevent structural collapse.
- `omega_daemon.py`: The master script. Run this once, and it spins up all the automated processes in the background (including the project map/help generator).

## How to Run Everything

1. Open your terminal in the root `omega-constitution-v9` folder.
2. Run `python3 CONSTITUTION/python/omega_daemon.py`
3. Enjoy your self-healing, automated, highly-secure workspace.
