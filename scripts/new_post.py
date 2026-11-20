#!/usr/bin/env python3
"""Scaffold a complete draft article package; nothing is published automatically."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def svg_template(slug: str, kind: str, heading: str, prompt: str) -> str:
    safe_id = f"{slug}-{kind}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 320"
 role="img" aria-labelledby="{safe_id}-title {safe_id}-desc">
 <title id="{safe_id}-title">{escape(heading)}</title>
 <desc id="{safe_id}-desc">{escape(prompt)}</desc>
 <rect x="24" y="24" width="912" height="272" rx="18" fill="#f7faf7" stroke="#d5e3da"/>
 <text x="480" y="132" text-anchor="middle" font-size="25" font-weight="700" fill="#19393d">{escape(heading)}</text>
 <text x="480" y="184" text-anchor="middle" font-size="17" fill="#58716f">{escape(prompt)}</text>
 <text x="480" y="242" text-anchor="middle" font-size="13" fill="#bc7149">DRAFT · replace with a problem-specific diagram</text>
</svg>
'''


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("category")
    ap.add_argument("slug")
    ap.add_argument("--topic", required=True, help="Registered L3 problem-pattern slug")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--problem-url", required=True)
    args = ap.parse_args()

    categories = json.loads((ROOT / "content/categories.json").read_text(encoding="utf-8"))
    category = next((c for c in categories if c["slug"] == args.category), None)
    if category is None:
        ap.error("category not registered")
    if args.topic not in {t["slug"] for t in category["topics"]}:
        ap.error("topic not registered in this category; see content/categories.json")
    if not SLUG_RE.fullmatch(args.slug):
        ap.error("slug must be lowercase kebab-case")
    if not args.problem_url.startswith("https://leetcode.com/problems/"):
        ap.error("--problem-url must point to an official LeetCode problem")
    manifest = ROOT / "content/posts.json"
    posts = json.loads(manifest.read_text(encoding="utf-8"))
    if any(p["slug"] == args.slug for p in posts):
        ap.error("slug already exists")
    target = ROOT / "posts" / args.category / args.slug
    if target.exists():
        ap.error("article directory already exists")

    (target / "assets").mkdir(parents=True)
    diagrams = {
        "cover.svg": ("Core mechanism", "Replace with a diagram that explains the algorithm's central idea."),
        "trace.svg": ("Execution trace", "Replace with a step-by-step state trace using a concrete input."),
        "pitfall.svg": ("Counterexample", "Replace with a counterexample that exposes a common incorrect approach."),
    }
    for filename, (heading, prompt) in diagrams.items():
        (target / "assets" / filename).write_text(
            svg_template(args.slug, filename.removesuffix(".svg"), heading, prompt),
            encoding="utf-8",
        )

    page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(args.title)} · leetcode-posts</title>
<meta name="description" content="DRAFT: {escape(args.subtitle, quote=True)}">
</head><body>
<a href="../../../">返回 leetcode-posts</a>
<main id="content"><article>
<header><p>DRAFT · {escape(category["title"])} / {escape(args.topic)}</p>
<h1>{escape(args.title)}</h1><p>{escape(args.subtitle)}</p>
<a href="{escape(args.problem_url, quote=True)}">LeetCode 官方原题 ↗</a></header>
<section><h2>01 · 题意与输入约束</h2><p>TODO: 用原创语言概括目标、输入输出与关键约束。</p></section>
<section><h2>02 · 朴素方法与瓶颈</h2><p>TODO: 给出可验证的基线，并指出重复工作。</p></section>
<section><h2>03 · 核心状态与不变量</h2><p>TODO: 定义每个状态变量，说明每一步更新为什么安全。</p>
<figure><img src="assets/cover.svg" alt="待完成的算法机制图"><figcaption>TODO: 解释图中的状态和关系。</figcaption></figure></section>
<section><h2>04 · 逐步执行</h2><p>TODO: 使用真实输入手推每轮状态。</p>
<figure><img src="assets/trace.svg" alt="待完成的算法执行轨迹"><figcaption>TODO: 标注每个状态变化。</figcaption></figure></section>
<section><h2>05 · 正确性证明</h2><p>TODO: 证明初始化、保持和终止。</p></section>
<section><h2>06 · Python 实现与复杂度</h2><pre><code>class Solution:
    pass  # TODO: implement and test</code></pre><p>TODO: 分析时间、辅助空间、输出空间和输入修改。</p></section>
<section><h2>07 · 反例、边界与迁移</h2><p>TODO: 解释常见错误及可迁移的问题模式。</p>
<figure><img src="assets/pitfall.svg" alt="待完成的错误示例与反例"><figcaption>TODO: 说明反例如何击穿错误方案。</figcaption></figure></section>
</article></main></body></html>
'''
    (target / "index.html").write_text(page, encoding="utf-8")
    (target / "solution.py").write_text(
        "class Solution:\n    pass  # TODO: implement the official method\n",
        encoding="utf-8",
    )
    evidence = {
        "problem": {
            "url": args.problem_url,
            "source": "Official LeetCode problem page; verify title, difficulty and constraints before publishing.",
            "facts": [],
        },
        "claims": [],
        "test_cases": [],
    }
    (target / "evidence.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    today = datetime.now(timezone.utc).date().isoformat()
    posts.append({
        "slug": args.slug, "title": args.title, "subtitle": args.subtitle,
        "category": args.category, "topic": args.topic, "status": "draft",
        "published": today, "updated": today, "reading_minutes": 0,
        "tags": [], "summary": "TODO: write a concise, original summary.",
        "problem_url": args.problem_url, "illustration": args.slug,
        "cover": {"src": "assets/cover.svg", "caption": "TODO: replace with a unique, accurate cover explanation."},
        "facets": {
            "structures": [], "techniques": [], "problem_shapes": [],
            "reasoning": [], "prerequisites": [], "learning_stage": "core",
        },
    })
    manifest.write_text(json.dumps(posts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Created DRAFT:", target.relative_to(ROOT))
    print("Three SVGs, index.html, solution.py and evidence.json scaffolded.")
    print("Not published until editorial work, tests and explicit status promotion are complete.")


if __name__ == "__main__":
    main()
