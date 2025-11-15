
# 🗂️ **Smart File Organizer**

### *Tame Your Digital Chaos — Automatically & Safely*

> **"Your `Downloads` folder doesn't need therapy — it needs automation."**
> Meet the tool that **turns messy directories into beautifully structured, human-friendly spaces**, with **zero data loss**, **full transparency**, and **true engineering-grade safety**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CLI-Application-000000?logo=gnu-bash&logoColor=white" />
  <img src="https://img.shields.io/badge/Logging-Enabled-blue?logo=simpleanalytics" />
  <img src="https://img.shields.io/badge/Duplicate%20Safe-Yes-success" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

# ✨ **Why Smart File Organizer?**

This isn’t just another script that dumps files into folders.
It’s a **modular, safe, production-ready utility** designed like a real engineering project.

| Feature                     | Benefit                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Smart Categorization**    | Auto-detects files → organizes into `Documents`, `Images`, `Videos`, `Audio`, `Archives`, `Code`, `Others` |
| **Never Loses Data**        | Duplicate-safe renaming: `report.pdf` → `report (1).pdf`                                                   |
| **Dry-Run Mode**            | Shows EXACT operations before executing them                                                               |
| **Full Audit Logging**      | Every action logged with **timestamp + source + destination**                                              |
| **Extensible Architecture** | Add new categories or detection logic easily                                                               |
| **CLI-first Design**        | Fast. Clean. Scriptable. Works anywhere.                                                                   |

---

# ⚙️ **Tech Architecture (At a Glance)**

```
file-organizer/
│
├── organizer/
│   ├── categories.py      # File-type mappings
│   ├── utils.py           # Logging + helpers
│   ├── organizer.py       # Engine: scan → categorize → move
│   ├── main.py            # CLI interface
│   └── __init__.py
│
├── logs/
│   └── organizer.log
│
├── tests/
│   └── sample_files/
│
├── README.md
└── requirements.txt
```

✔ Modular
✔ Maintainable
✔ Production-grade structure

---

# 🚀 **Quick Start**

```bash
# 1. Clone the repo
git clone https://github.com/aadil-syed/file-organizer-ai.git
cd file-organizer-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Organize any folder
python -m organizer.main --path ./my_messy_folder

# 4. Safe preview (no files moved)
python -m organizer.main --path ./my_messy_folder --dry-run
```

---

# 🛠️ **CLI Options**

| Flag        | Description                                  |
| ----------- | -------------------------------------------- |
| `--path`    | Folder to organize                           |
| `--verbose` | Prints detailed actions to console           |
| `--dry-run` | Shows what WILL happen, without moving files |
| `--log`     | Custom log path                              |

Example:

```bash
python -m organizer.main --path ~/Downloads --verbose
```

---

# 📁 **Categories Supported**

| Category      | Extensions                                     |
| ------------- | ---------------------------------------------- |
| **Documents** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`      |
| **Images**    | `.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`        |
| **Videos**    | `.mp4`, `.avi`, `.mov`, `.mkv`                 |
| **Audio**     | `.mp3`, `.wav`, `.flac`                        |
| **Archives**  | `.zip`, `.rar`, `.7z`, `.tar`                  |
| **Code**      | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java` |
| **Others**    | Everything else                                |

---

# 📊 **Logging Example**

```
2025-01-10 14:22:05 - INFO - Moved: holiday.png → Images/
2025-01-10 14:22:05 - INFO - Moved: resume.pdf → Documents/
2025-01-10 14:22:05 - WARNING - Duplicate detected: report.pdf → report (1).pdf
2025-01-10 14:22:05 - INFO - Skipped: .DS_Store
```

Transparent. Traceable. Audit-ready.

---

# 🧪 **Testing Scenarios**

✔ Mixed file types
✔ Duplicate detection
✔ Invalid path error
✔ Read-only folders
✔ Dry-run consistency

---

# 🗺️ **Roadmap**

* [ ] Add content-based file classification (magic numbers)
* [ ] Add GUI (Tkinter or Electron)
* [ ] Add scheduling (cron / Task Scheduler)
* [ ] Add plug-in category system
* [ ] Make PyPI package: `pip install smart-file-organizer`
* [ ] Add unit tests (pytest)

---

# 🤝 **Contributing**

PRs are welcome!
Fork → Improve → Submit PR.

---

# 📜 **License**

MIT License © 2025 Aadil Syed

---

