"""db.py — Async SQLite helpers for braindump.db"""
import aiosqlite
from datetime import datetime, date
from pathlib import Path

DB_PATH = Path.home() / "09-personal" / "BrainDumpSessions" / "braindump.db"


async def save_entry(raw_text: str, emotions: str = "", topics: str = "", domain: str = ""):
    today = date.today().isoformat()
    now = datetime.now().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO entries (date, timestamp, raw_text, emotions_detected, topics, domain) VALUES (?, ?, ?, ?, ?, ?)",
            (today, now, raw_text, emotions, topics, domain),
        )
        await db.commit()


async def save_baseline(sleep_hrs=None, sleep_quality=None, energy=None, suds=None,
                        outlook=None, exercise=None, medication=None, notes=None):
    today = date.today().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO baselines (date, sleep_hrs, sleep_quality, energy, suds, outlook, exercise, medication, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (today, sleep_hrs, sleep_quality, energy, suds, outlook, exercise, medication, notes),
        )
        await db.commit()


async def save_idea(raw_text: str, category: str = ""):
    today = date.today().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO ideas (date, raw_text, category) VALUES (?, ?, ?)",
            (today, raw_text, category),
        )
        await db.commit()


async def save_pattern(pattern_type: str, trigger_text: str, meta_model_response: str = ""):
    today = date.today().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO patterns (date, pattern_type, trigger_text, meta_model_response) VALUES (?, ?, ?, ?)",
            (today, pattern_type, trigger_text, meta_model_response),
        )
        await db.commit()


async def get_today_context(n: int = 10) -> str:
    today = date.today().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT timestamp, raw_text FROM entries WHERE date = ? ORDER BY created_at DESC LIMIT ?",
            (today, n),
        )
        rows = await cursor.fetchall()

    if not rows:
        return ""

    parts = []
    for row in reversed(rows):
        ts = row["timestamp"] or ""
        parts.append(f"[{ts}] {row['raw_text']}")
    return "\n\n".join(parts)


async def get_latest_baseline() -> dict | None:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT * FROM baselines ORDER BY date DESC, id DESC LIMIT 1"
        )
        row = await cursor.fetchone()
        return dict(row) if row else None


async def get_entry_count() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM entries")
        row = await cursor.fetchone()
        return row[0] if row else 0
