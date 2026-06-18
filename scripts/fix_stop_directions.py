#!/usr/bin/env python3
"""Convert leaky **STOP. ...** stage directions into unmistakable director's notes
that a teaching model won't read aloud. Deterministic, content-preserving."""
import re, pathlib, sys

lessons = sorted(pathlib.Path("lessons").glob("*.md"))
changed = []
for f in lessons:
    txt = f.read_text(encoding="utf-8")
    orig = txt

    # 1. The rules-block line: reword the bare "STOP" so the model never echoes it.
    txt = txt.replace(
        "- **ONE step per message.** STOP and wait after each one.",
        "- **ONE step per message.** Pause and wait for the student after each one. "
        'The 🎬 director\'s notes below mark where to pause — they are instructions to '
        'you, never say them (or the word "stop") aloud.',
    )

    # 2. Per-step stage directions: **STOP. {REST}**  ->  director's note blockquote.
    def repl(m):
        rest = m.group(1).strip()
        return f"> 🎬 **Director's note (never say aloud):** {rest}"

    txt = re.sub(r"^\*\*STOP\.\s*(.+?)\*\*\s*$", repl, txt, flags=re.M)

    if txt != orig:
        f.write_text(txt, encoding="utf-8")
        changed.append(f.name)

print(f"changed {len(changed)} lesson files")
# verify no bare leaky STOP directions remain
import subprocess
left = subprocess.run(["grep", "-rn", r"\*\*STOP", "lessons/"], capture_output=True, text=True).stdout
print("remaining **STOP markers:", left.count("STOP"))
