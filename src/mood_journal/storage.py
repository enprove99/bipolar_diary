import json
import os
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "journal.json"


def get_data_file_path():
    return str(DATA_FILE)


def initialize_file():
    if not DATA_DIR.exists():
        DATA_DIR.mkdir()

    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"schema_version": "0.1", "entries": []}, f, indent=2)


def load_data():
    initialize_file()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise SystemExit("Data file is corrupted. Please back up and repair.")


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_entry(mood, sleep, drug, note, date):
    data = load_data()

    now = datetime.now().astimezone()
    timestamp = now.isoformat()

    entry = {
        "id": timestamp,
        "date": date,
        "mood": mood,
        "sleep_hours": sleep,
        "drug": drug,
        "note": note,
        "created_at": timestamp,
    }

    data["entries"].append(entry)
    save_data(data)

    return entry


def list_entries(n):
    data = load_data()
    entries = sorted(
        data["entries"], key=lambda x: x["created_at"], reverse=True
    )
    return entries[: min(n, 50)]