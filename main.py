#!/usr/bin/env python3
"""Writes this entry's single line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

LINE = "My printer won't print black text because it's out of cyan, a colour I have never used, and it saves this announcement for page one of the one document due in five minutes."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
