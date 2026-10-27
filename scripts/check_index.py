#!/usr/bin/env python3
"""作品集索引一致性自检。

这个索引 README 里的「项目数量」「项目卡片」「可见性标记」很容易和真实仓库脱节
（曾经写着 17 个、实际引用 20 个，还漏了一个主打项目）。
本脚本把三件事钉死：

1. README 引用的每个仓库都在 ``projects.json`` 里（不多不少）；
2. ``projects.json`` 里每个项目都在 README 出现（不多不少）；
3. README 声明的项目数量 == ``projects.json.count`` == 实际引用数；
4. 可见性标记（🔒）与 manifest 一致：私有仓库必须标 🔒，公开仓库不能标。

用法::

    python3 scripts/check_index.py            # 本地 / CI
    python3 scripts/check_index.py --remote   # 额外用 GitHub API 核对真实可见性
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
MANIFEST = os.path.join(ROOT, "projects.json")

LINK_RE = re.compile(r"((?:🔒\s*)*)\[([A-Za-z0-9._-]+)\]\(https://github\.com/LuOzawa/([A-Za-z0-9._-]+)\)")
ANY_LINK_RE = re.compile(r"https://github\.com/LuOzawa/([A-Za-z0-9._-]+)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote", action="store_true", help="用 GitHub API 核对真实可见性")
    args = parser.parse_args()

    if not os.path.exists(README) or not os.path.exists(MANIFEST):
        print("缺少 README.md 或 projects.json", file=sys.stderr)
        return 2

    readme = open(README, encoding="utf-8").read()
    manifest: dict[str, Any] = json.load(open(MANIFEST, encoding="utf-8"))
    projects = manifest.get("projects") or []
    declared = {p["name"]: p for p in projects}

    errors: list[str] = []

    # 1) 链接合法性 + 可见性标记
    seen: set[str] = set()
    for match in LINK_RE.finditer(readme):
        locked_raw, label, target = match.group(1), match.group(2), match.group(3)
        locked = bool(locked_raw.strip())
        if len(re.findall(r"🔒", locked_raw)) > 1:
            fail(errors, f"🔒 标记重复：{target}")
        if label != target:
            fail(errors, f"链接文字与仓库名不一致：{label} != {target}")
        if target not in declared:
            fail(errors, f"README 引用了 manifest 里没有的项目：{target}")
            continue
        seen.add(target)
        want_locked = declared[target]["visibility"] == "private"
        if want_locked and not locked:
            fail(errors, f"私有项目缺少 🔒 标记：{target}")
        if not want_locked and locked:
            fail(errors, f"公开项目不该有 🔒 标记：{target}")

    # 2) manifest 里的项目必须都出现在 README
    for name in declared:
        if name not in seen:
            fail(errors, f"manifest 里的项目没有出现在 README：{name}")

    # 3) 数量一致
    referenced = {n for n in ANY_LINK_RE.findall(readme) if n not in ("LuOzawa",)}
    count_claim = re.search(r"\*\*(\d+) 个项目的索引", readme)
    if not count_claim:
        fail(errors, "README 顶部没有声明项目数量（形如「**21 个项目的索引…」）")
    else:
        claimed = int(count_claim.group(1))
        if claimed != manifest.get("count"):
            fail(errors, f"README 声明 {claimed} 个，manifest.count = {manifest.get('count')}")
        if claimed != len(referenced):
            fail(errors, f"README 声明 {claimed} 个，实际引用 {len(referenced)} 个仓库")
    if manifest.get("count") != len(projects):
        fail(errors, f"manifest.count = {manifest.get('count')}，实际条目 {len(projects)} 条")

    # 4) 可选：与 GitHub 真实状态核对
    if args.remote:
        try:
            import json as _json
            import subprocess

            raw = subprocess.run(
                ["gh", "api", f"repos/{manifest.get('owner')}/{name}", "--jq", ".private"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            actual_private = raw == "true"
            want_private = declared[name]["visibility"] == "private"
            if actual_private != want_private:
                fail(errors, f"{name} 可见性与 GitHub 实际不符（实际 private={actual_private}）")
        except Exception as exc:  # pragma: no cover
            print(f"⚠️ 远端核对跳过：{exc}", file=sys.stderr)

    if errors:
        print("❌ 索引一致性检查未通过：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✅ 索引一致性检查通过：{len(declared)} 个项目，README 与 projects.json 一致")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
