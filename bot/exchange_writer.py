"""exchange_writer.py — Write sanitised summaries to caveman exchange folder."""
import logging
from datetime import date
from pathlib import Path

log = logging.getLogger("braindump.exchange")

EXCHANGE_DIR = Path.home() / "caveman" / "collab" / "braindump-exchange"


def write_daily_summary(summary: str, for_date: str = ""):
    d = for_date or date.today().isoformat()
    path = EXCHANGE_DIR / "summaries" / f"{d}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Daily Braindump Summary - {d}\n\n{summary}\n", encoding="utf-8")
    log.info("Wrote summary: %s", path)


def write_idea(idea_text: str, category: str = "", for_date: str = ""):
    d = for_date or date.today().isoformat()
    ideas_dir = EXCHANGE_DIR / "ideas"
    ideas_dir.mkdir(parents=True, exist_ok=True)
    # Find next available number
    existing = list(ideas_dir.glob(f"{d}-*.md"))
    n = len(existing) + 1
    path = ideas_dir / f"{d}-{n:02d}.md"
    path.write_text(f"# Idea - {d}\n\nCategory: {category}\n\n{idea_text}\n", encoding="utf-8")
    log.info("Wrote idea: %s", path)


def write_tasks(tasks: list[str], for_date: str = ""):
    d = for_date or date.today().isoformat()
    path = EXCHANGE_DIR / "tasks" / f"{d}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    task_lines = "\n".join(f"- [ ] {t}" for t in tasks)
    path.write_text(f"# Tasks Extracted - {d}\n\n{task_lines}\n", encoding="utf-8")
    log.info("Wrote tasks: %s", path)
