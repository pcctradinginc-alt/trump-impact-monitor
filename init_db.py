"""
init_db.py – optional, run once locally to pre-create alerts.db

Usage:
    python init_db.py
"""

import sqlite3
import os

DB_PATH = "alerts.db"

def init():
    if os.path.exists(DB_PATH):
        print(f"ℹ️  {DB_PATH} exists already – skipping creation.")
    else:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                event_id     TEXT PRIMARY KEY,
                source       TEXT,
                published_at TEXT,
                raw_text     TEXT,
                hash         TEXT UNIQUE,
                ticker       TEXT,
                processed_at TEXT
            )
        """)
        conn.commit()
        conn.close()
        print(f"✅ {DB_PATH} created successfully.")

if __name__ == "__main__":
    init()
