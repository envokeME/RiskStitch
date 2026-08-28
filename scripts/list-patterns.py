#!/usr/bin/env python3
"""Print the RiskStitch catalog without third-party dependencies."""

import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))

print(f"RiskStitch {catalog['release']} — {catalog['pattern_count']} patterns ({catalog['status']})")
print()
for item in catalog["patterns"]:
    print(f"{item['name']:<38} {item['domain']:<22} {item['summary']}")
