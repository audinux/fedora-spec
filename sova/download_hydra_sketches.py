#!/usr/bin/env python3
"""Decode the public hydrasynth.xyz sketch database (already fetched to
sketches_raw.json via `curl https://api.hydrasynth.xyz/sketches`) into
one .hydra file + one .json metadata file per sketch, plus a top-level index.
"""
import base64
import json
import re
import sys
import urllib.parse
from pathlib import Path

SCRATCH = Path(__file__).parent
RAW_FILE = SCRATCH / "sketches_raw.json"
OUT_DIR = SCRATCH / "sketches"

SAFE_ID_RE = re.compile(r"[^A-Za-z0-9_-]")


def decode_code(b64: str) -> str:
    raw = base64.b64decode(b64)
    return urllib.parse.unquote(raw.decode("ascii"))


def safe_filename(sketch_id: str) -> str:
    return SAFE_ID_RE.sub("_", sketch_id) or "unknown"


def main():
    with RAW_FILE.open() as f:
        entries = json.load(f)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    index = []
    failures = []

    for entry in entries:
        sketch_id = entry.get("sketch_id") or entry.get("_id")
        if not sketch_id:
            failures.append({"reason": "missing id", "entry": entry})
            continue

        code_b64 = entry.get("code")
        if not code_b64:
            failures.append({"id": sketch_id, "reason": "missing code"})
            continue

        try:
            code = decode_code(code_b64)
        except Exception as e:
            failures.append({"id": sketch_id, "reason": f"decode error: {e}"})
            continue

        fname = safe_filename(sketch_id)
        (OUT_DIR / f"{fname}.hydra").write_text(code, encoding="utf-8")

        meta = {
            "sketch_id": sketch_id,
            "date": entry.get("date"),
            "parent": entry.get("parent"),
            "masto_id": entry.get("masto_id"),
        }
        (OUT_DIR / f"{fname}.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        index.append(meta)

    (SCRATCH / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    (SCRATCH / "failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")

    print(f"total entries: {len(entries)}")
    print(f"decoded ok:    {len(index)}")
    print(f"failed:        {len(failures)}")


if __name__ == "__main__":
    sys.exit(main())
