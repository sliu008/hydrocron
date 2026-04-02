#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
GENERATED = ROOT / "docs" / "_generated_version.md"


def read_version() -> str:
    data = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    return data["tool"]["poetry"]["version"]


def write_generated(version: str) -> bool:
    content = f"**Version:** {version}\n"
    if GENERATED.exists():
        current = GENERATED.read_text(encoding="utf-8")
        if current == content:
            return False
    GENERATED.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    version = read_version()
    changed = write_generated(version)
    if changed:
        print(f"Updated docs/_generated_version.md to version {version}")
    else:
        print(f"docs/_generated_version.md already at version {version}")


if __name__ == "__main__":
    main()
