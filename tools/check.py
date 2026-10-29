#!/usr/bin/env python3
"""Score a reader's text against each sample's expected fields.

usage: python3 tools/check.py formats/<format>/samples [--reader-output <jsonl>]

For each <name>.expected.json beside <name>.pdf, reports which expected values
appear in <name>.txt (case and spacing ignored) and, given the reader's JSON
lines, whether its title fact matches. A value that is missing from the text
is one no rule can extract, so it is a reader bug, not a format bug.
"""
import json
import os
import re
import sys

FIELDS = ["title_code", "code_as_printed", "classification", "service", "agency", "title", "date_as_printed"]


def norm(s):
    # Markdown escapes (`\[061\]`) are not part of the text.
    s = s.replace("\\", "").replace("’", "'").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    samples = args[0]
    facts = {}
    if "--reader-output" in args:
        path = args[args.index("--reader-output") + 1]
        names = sorted(f[:-14] for f in os.listdir(samples) if f.endswith(".expected.json"))
        for name, line in zip(names, open(path).read().splitlines()):
            facts[name] = json.loads(line).get("facts", {})
    found = total = 0
    for f in sorted(os.listdir(samples)):
        if not f.endswith(".expected.json"):
            continue
        name = f[:-14]
        expected = json.load(open(os.path.join(samples, f)))
        text = norm(open(os.path.join(samples, name + ".txt")).read())
        missing = []
        for field in FIELDS:
            value = expected.get(field)
            if value is None:
                continue
            total += 1
            if norm(value) in text:
                found += 1
            else:
                missing.append(field)
        title = facts.get(name, {}).get("title")
        title_note = "" if name not in facts else ("  title fact ok" if title and norm(title) == norm(expected["title"]) else f"  title fact: {title!r}")
        print(f"{name}: {'all present' if not missing else 'missing ' + ', '.join(missing)}{title_note}")
    print(f"{found} of {total} expected values appear in the text")


if __name__ == "__main__":
    main()
