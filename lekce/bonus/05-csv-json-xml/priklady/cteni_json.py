"""Čtení JSON — load vrátí list/dict."""

import json

with open("zaci.json", "r", encoding="utf-8") as f:
    zaci = json.load(f)

for zak in zaci:
    print(zak["jmeno"], zak["vek"])
