# bipolar_diary
This repository documents the evolution of a privacy-first bipolar mood journal built with Python. It serves as both a structured mood-tracking CLI project and a transparent record of my programming growth. Only source code and development logs are shared here; personal journal data remains strictly local and is never uploaded.


🌓 Mood Journal CLI

A privacy-first bipolar mood tracking tool built with Python.

📌 Overview

Mood Journal CLI is a lightweight, local-first command-line tool designed to track:

Mood level (1–5)

Sleep hours

Medication adherence (yes/no)

Optional notes

This repository documents the evolution of the software, not personal journal content.

All journal data is stored locally and is never uploaded to GitHub.

🔒 Privacy & Design Principles

Local JSON storage (data/journal.json)

data/ is excluded via .gitignore

No external services

No cloud sync

No heavy dependencies

Low resource usage (suitable for notebook PCs or mobile terminal environments)

🚀 v0.1 Features
Add Entry
python -m src.mood_journal add --mood 4 --sleep 6.5 --drug yes --note "sample"

Required arguments

--mood (1–5)

--sleep (0–24 hours)

--drug (yes or no)

Optional

--note

--date YYYY-MM-DD

Example output:

Saved: 2026-02-26 mood=4 sleep=6.5 drug=yes
List Recent Entries
python -m src.mood_journal list --n 7

Output:

DATE        MOOD  SLEEP  DRUG  NOTE
2026-02-26   4     6.5    yes   sample

Default: last 7 entries
Maximum: 50 entries per request

Show Data File Location
python -m src.mood_journal where

Output:

Data file: data/journal.json
📂 Project Structure
mood-journal/
├── src/
│   └── mood_journal/
├── data/               # Local storage (ignored by git)
├── README.md
├── .gitignore
📦 Data Schema (v0.1)
{
  "schema_version": "0.1",
  "entries": [
    {
      "id": "2026-02-26T08:30:12+08:00",
      "date": "2026-02-26",
      "mood": 4,
      "sleep_hours": 6.5,
      "drug": "yes",
      "note": "sample",
      "created_at": "2026-02-26T08:30:12+08:00"
    }
  ]
}
🧠 Project Purpose

This project serves two parallel goals:

Build a structured, minimal mental health tracking tool

Document a disciplined Python learning journey

Each version increment reflects architectural refinement and design iteration.

🛣 Roadmap

v0.1 — Basic JSON storage

v0.2 — Trend summary & simple statistics

v0.3 — Data export (CSV)

v0.4 — SQLite migration

v0.5 — Optional encryption

⚠ Disclaimer

This tool is for personal tracking and educational purposes only.
It is not a medical device and does not replace professional care.

If you are experiencing crisis, please seek professional support immediately.
