"""
2026-10-19  Extract messages from a Positron Assistant conversation export (schemaVersion json).
File: .claude/skills/repo-excerpt/scripts/extract_msg.py

Usage:
  python -I extract_msg.py <conversation.json> <index> [<index> ...]
  python -I extract_msg.py <conversation.json> 18-21
  python -I extract_msg.py <conversation.json> --grep "결과 해석"

Prints, per message: index, role, text parts, tool-call names and the first lines of tool results.
Row-level data never comes from here: tool results are truncated to --max-chars (default 600).
Run with -I so nothing is imported from the data directory.
"""
import argparse
import json
import sys


def parse_indices(tokens):
    out = []
    for t in tokens:
        if "-" in t:
            a, b = t.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(t))
    return out


def iter_parts(msg):
    """Yield (role, kind, text) for each content part of one messages[] entry."""
    lm = msg.get("message", {}).get("lmMessage", [])
    for entry in lm:
        role = entry.get("role", "?")
        content = entry.get("content", [])
        if isinstance(content, str):
            yield role, "text", content
            continue
        for part in content:
            kind = part.get("type", "?")
            if kind == "text":
                yield role, "text", part.get("text", "")
            elif kind == "tool-call":
                args = part.get("args") or part.get("input") or {}
                code = args.get("code") if isinstance(args, dict) else None
                yield role, "tool-call", f"{part.get('toolName', part.get('name', '?'))}" + (f"\n{code}" if code else "")
            elif kind == "tool-result":
                res = part.get("result") or part.get("output") or part.get("content") or ""
                yield role, "tool-result", json.dumps(res, ensure_ascii=False) if not isinstance(res, str) else res
            else:
                yield role, kind, json.dumps(part, ensure_ascii=False)[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("indices", nargs="*")
    ap.add_argument("--grep", help="print only messages whose text contains this string")
    ap.add_argument("--max-chars", type=int, default=600, help="truncate tool results to this length")
    a = ap.parse_args()

    with open(a.path, encoding="utf-8") as f:
        d = json.load(f)
    msgs = d["messages"] if isinstance(d, dict) else d

    wanted = parse_indices(a.indices) if a.indices else range(len(msgs))
    sys.stdout.reconfigure(encoding="utf-8")
    for i in wanted:
        if i < 0 or i >= len(msgs):
            print(f"[{i}] out of range (0..{len(msgs)-1})")
            continue
        parts = list(iter_parts(msgs[i]))
        if a.grep and not any(a.grep in t for _, k, t in parts if k == "text"):
            continue
        print(f"\n===== msg[{i}] =====")
        for role, kind, text in parts:
            if kind == "tool-result":
                text = text[: a.max_chars] + (" …[truncated]" if len(text) > a.max_chars else "")
            print(f"--- {role} / {kind}")
            print(text)


if __name__ == "__main__":
    main()
