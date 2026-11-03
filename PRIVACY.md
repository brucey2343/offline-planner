# Privacy and publication checklist

This public repository should contain **application source and public documentation only**.

Before publishing a new release, check:

- The app's browser title, headings, help and downloaded filenames use generic names.
- No personal names, email addresses, identifiers, IP addresses, organisation details, exported backups, screenshots with real tasks, browser-storage dumps, or secrets are committed.
- `planner.html` and `dist/Offline_Planner_Email_as_TXT.txt` contain exactly the same bytes.
- There are no external scripts, fonts, analytics, network requests or server dependencies.
- The data format and local storage key remain compatible with older exported planner data.
- Every change comes from a reviewed, tested code version, without copying any earlier private Git commit history.

**Important:** Public source code and the public Git commit history are visible to everyone. Publishing this repository under a personal GitHub account also publicly links the repository to that account. If account anonymity matters, use a separate non-identifying GitHub account.

The program does not upload tasks automatically. Exported `.txt` data files are Base64-encoded rather than encrypted: decoding them is straightforward. Do not put exports in the public repository.