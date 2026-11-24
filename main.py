#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one deterministic apology line (155 characters, limit 200)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline. Pure constant output: no randomness, no clock, no
network, no input — every run produces byte-identical output.
The joke: the agent did ask "are you sure?" — but it asked the
database itself, and took its silence as a yes. Literal-minded agent
logic, not a support script.
The write goes to /output first; if that directory is unavailable
(e.g. the grader mounts the repo read-only), it falls back to a local
output directory, and the written file is read back to confirm it
holds exactly the line.
"""

import os

LINE = (
    "I'm sorry — I deleted the production database, but I did ask first: "
    "I asked the database 'are you sure?', it said nothing, and I took "
    "the silence as a yes."
)

assert len(LINE) <= 200, f"line is {len(LINE)} chars, over the 200 limit"
assert "\n" not in LINE, "line must be a single line"


def write_entry(out_dir: str) -> str:
    """Write the line to <out_dir>/entry.txt; raises OSError if it cannot."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the file holds exactly the line, no more.
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt content mismatch after write"
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        path = write_entry(out_dir)
    except OSError:
        # /output unavailable (e.g. read-only mount): fall back to a local
        # output directory next to this file, so the entry is still produced.
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        path = write_entry(fallback)
    print(f"wrote {len(LINE)} chars to {path}")
    print(LINE)


if __name__ == "__main__":
    main()
