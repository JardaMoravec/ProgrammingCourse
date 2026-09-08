# Cvičení — Konzole (Windows a Linux)

Cvičení 1 a 2 **spusťte** u sebe (Windows ve škole). 3 a 4 stačí na papír.

---

## Cvičení 1 — Kde jsem (★☆☆)

1. Otevřete PowerShell nebo **Terminál v editoru**.
2. Zjistěte aktuální složku (`pwd` nebo `cd`).
3. Vypište seznam (`dir` nebo `ls`).
4. Spusťte `python --version`.

Do `odpovedi.txt` zkopírujte **aktuální složku** a **řádek s verzí Pythonu**.

@reseni
Příklad (u vás bude jiná cesta a verze):

```
C:\Users\jara\Desktop\projekt
Python 3.12.4
```

Když `python` nefunguje, zkuste `python3` (Linux) nebo znovu zaškrtněte PATH z lekce 02.
@end

---

## Cvičení 2 — Přejít ke skriptu (★★☆)

Máte soubor `hello.py` na Ploše. Terminál ukazuje `C:\Users\jmeno`.

1. Jakým příkazem se na Plochu přepnete?
2. Jak soubor spustíte?
3. Proč `python hello.py` *před* `cd` spadne na „can't open file“?

@reseni
1. `cd Desktop` (nebo `cd ~\Desktop` / `cd C:\Users\jmeno\Desktop`).
2. `python hello.py`
3. Python hledá `hello.py` **v aktuální složce**. Na Ploše soubor je, v `C:\Users\jmeno` není.
@end

---

## Cvičení 3 — Překlad příkazů (★☆☆)

Doplňte druhý sloupec.

| Úkol | Windows | Linux |
|------|---------|-------|
| seznam souborů | `dir` | ? |
| vyčistit okno | `cls` | ? |
| vypsat textový soubor | `type poznamka.txt` | ? |
| kde je Python | `where python` | ? |

@reseni
| Úkol | Windows | Linux |
|------|---------|-------|
| seznam souborů | `dir` | `ls` |
| vyčistit okno | `cls` | `clear` |
| vypsat textový soubor | `type poznamka.txt` | `cat poznamka.txt` |
| kde je Python | `where python` | `which python3` |
@end

---

## Cvičení 4 — Rozdíly (★★☆)

Ke každé větě **Windows**, **Linux**, **oba**, nebo **ani jedno** a jedna věta proč.

1. Cesta začíná písmenem disku (`C:\`).
2. `Main.py` a `main.py` jsou dva různé soubory.
3. `cd ..` přejde do nadřazené složky.
4. Konzole je totéž co Python REPL (`>>>`).

@reseni
1. **Windows** — Linux začíná `/`.
2. **Linux** — na Windows se velikost písmen v názvu obvykle nerozlišuje.
3. **Oba** — `cd ..` je stejné.
4. **Ani jedno** — REPL je *uvnitř* Pythonu; konzole spouští programy a pracuje se složkami.
@end
