#!/bin/bash
# Tlačítko Run ve VPL. Nespouštějte sqlite3 reseni.sql — to otevře konzoli
# a čeká na další příkazy. SQL tady pustí Python a hned skončí.
export PYTHONIOENCODING=utf-8
if command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  PY=python
fi
exec "$PY" -c 'import sqlite3, pathlib, sys
path = pathlib.Path(sys.argv[1])
if not path.is_file():
    print("Chybí soubor", path.name)
    raise SystemExit(1)
sql = path.read_text(encoding="utf-8")
con = sqlite3.connect(":memory:")
con.execute("PRAGMA foreign_keys = ON")
try:
    con.executescript(sql)
except sqlite3.Error as exc:
    print(exc)
    raise SystemExit(1)

def qi(name):
    return "\"" + name.replace("\"", "\"\"") + "\""

rows = con.execute("SELECT name FROM sqlite_master WHERE type = \"table\" AND name NOT LIKE \"sqlite_%\" ORDER BY name").fetchall()
print("Tabulky:", ", ".join(r[0] for r in rows) or "(zadna)")
for (name,) in rows:
    print()
    print(name)
    for col in con.execute("PRAGMA table_info(" + qi(name) + ")"):
        flags = []
        if col[5]:
            flags.append("PRIMARY KEY")
        if col[3]:
            flags.append("NOT NULL")
        extra = (" " + " ".join(flags)) if flags else ""
        print("  %s %s%s" % (col[1], col[2], extra))
' "__STUDENT_FILE__"
