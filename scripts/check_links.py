#!/usr/bin/env python3
"""检查 README 里的相对链接与文件锚点是否存在（不联网，避免对私有仓库误报）。"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")

REL_LINK_RE = re.compile(r"\[[^\]]*\]\((?!https?://|#|mailto:)([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.M)


def slug(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"[^\w一-鿿\- ]", "", s)
    return s.replace(" ", "-")


def main() -> int:
    if not os.path.exists(README):
        print("缺少 README.md", file=sys.stderr)
        return 2
    text = open(README, encoding="utf-8").read()
    anchors = {slug(h) for h in HEADING_RE.findall(text)}
    errors: list[str] = []

    for target in REL_LINK_RE.findall(text):
        path, _, anchor = target.partition("#")
        if path:
            full = os.path.join(ROOT, path)
            if not os.path.exists(full):
                errors.append(f"相对链接指向不存在的文件：{target}")
                continue
        if anchor and anchor not in anchors:
            errors.append(f"锚点不存在：{target}")

    if errors:
        print("❌ 链接检查未通过：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✅ 链接检查通过（{len(anchors)} 个锚点）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
