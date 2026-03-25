"""claude_session.py — Async wrapper for claude -p subprocess."""
import asyncio
import json
import logging
import shutil
from pathlib import Path

log = logging.getLogger("braindump.claude")


def _resolve_claude() -> str:
    found = shutil.which("claude")
    if found:
        return found
    for p in [Path.home() / ".local/bin/claude", Path("/opt/homebrew/bin/claude")]:
        if p.is_file():
            return str(p)
    return "claude"


CLAUDE_BIN = _resolve_claude()


class ClaudeSession:
    def __init__(self, model: str = "claude-sonnet-4-6"):
        self.model = model
        self.session_id: str | None = None

    async def send(self, message: str, system_prompt: str = "") -> str:
        args = [
            CLAUDE_BIN,
            "-p", message,
            "--output-format", "json",
            "--dangerously-skip-permissions",
            "--max-turns", "1",
            "--model", self.model,
        ]
        if system_prompt:
            args += ["--append-system-prompt", system_prompt]
        if self.session_id:
            args += ["--resume", self.session_id]

        log.info("claude -p (resume=%s)", self.session_id or "new")

        try:
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await proc.communicate()

            if proc.returncode != 0:
                err = stderr.decode(errors="replace")[:300]
                log.error("claude -p exit %d: %s", proc.returncode, err)
                # If resume failed, retry without it
                if self.session_id:
                    log.info("Clearing stale session, retrying fresh")
                    self.session_id = None
                    return await self.send(message, system_prompt)
                return f"Error from Claude (exit {proc.returncode})"

            raw = stdout.decode(errors="replace").strip()
            result = json.loads(raw)

            self.session_id = result.get("session_id", self.session_id)
            response = result.get("result", "")

            if not response and "messages" in result:
                for msg in reversed(result.get("messages", [])):
                    if msg.get("role") == "assistant":
                        content = msg.get("content", "")
                        if isinstance(content, list):
                            response = " ".join(
                                p.get("text", "") for p in content if p.get("type") == "text"
                            )
                        else:
                            response = str(content)
                        break

            return response.strip() or "(no response)"

        except json.JSONDecodeError:
            log.warning("Non-JSON output from claude -p")
            return raw[:1980] if raw else "(no response)"
        except Exception as exc:
            log.error("claude -p error: %s", exc)
            return f"Error: {exc}"

    def reset(self):
        self.session_id = None
