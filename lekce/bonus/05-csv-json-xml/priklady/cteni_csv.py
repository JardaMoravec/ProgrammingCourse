"""Čtení CSV — DictReader."""

import csv

with open("zaci.csv", "r", encoding="utf-8", newline="") as f:
    for radek in csv.DictReader(f):
        print(radek["jmeno"], radek["vek"])
