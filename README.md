# Offline Planner

A self-contained, offline-first task and printable planning app that runs locally in a compatible browser. No account, server, installation, or external assets are required.

## Download and use

- Download **`planner.html`**, then open it in a browser that permits local HTML and JavaScript.
- If a `.txt` file is easier to transfer, download **`dist/Offline_Planner_Email_as_TXT.txt`** and rename it to `.html` before opening. The two app files are identical.
- Use **Export .txt** inside the app to back up tasks, notes, layouts and preferences. The exported data file is a separate file from the app itself.
- Use **Import .txt → Merge changes** to combine changes between devices. Review any merge conflicts.
- Exported data is Base64-encoded for convenient text transport, **not encrypted**. Do not publish exported backups.

## Features

Daily, Weekly, Monthly and Anytime views (old Backlog tasks preserved in Anytime or dated views); dated and undated tasks; nested subtasks up to four levels; custom repeat intervals in days, weeks and months with day-of-month selection; overdue and upcoming tasks; independent priority and energy requirements; bulk task actions; repeated task entry without losing focus; independently stacked on-screen sections; collapsible priority groups; four-corner resize handles; per-view Print toggles that do not hide Plan tasks; dynamic custom-section destinations; custom printable A4 layouts with view and sheet selection; offline browser storage; Base64 backup transfers with merge review and recovery safeguards.

## Privacy and release policy

The application code contains no built-in user data, account credentials, personal names or server settings. It does not call external services or load remote resources. Real task data remains in each device's browser storage and manually exported backups. Review [PRIVACY.md](PRIVACY.md) before adding anything to this repository.

This repository is a **clean public distribution**, not a copy of a private development repository or its history. Keep development backups, real planner data, diagnostics, and private project history elsewhere.

The absence of a license file means the code is publicly viewable but no broad reuse license is granted automatically.

## Verification

Run `python tests/test_public_release.py` for the anonymisation, static offline checks and byte-for-byte consistency. The private development test suite is run separately before a release is copied into this public distribution.