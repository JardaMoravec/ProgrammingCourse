# Cvičení — Git a GitHub (bonus)

Cvičení jsou **v editoru a na papíře / v dokumentu**, ne v konzoli. Příkazy `git …` nepište. Pokud Git v IDE chybí, nainstalujte ho a editor restartujte — dál používejte jen panel Source Control / Git.

---

## Cvičení 1 — Proč verzovat (★☆☆)

Spolužák má na ploše složky `projekt`, `projekt_zaloha`, `projekt_stary` a `projekt_odeslat_uciteli`. Každá obsahuje trochu jiný `main.py`.

Napište **tři problémy** tohoto postupu a **jednu věc**, kterou by místo toho řešil Git.

@reseni
Problémy (příklady):

- Neví, která složka je aktuální.
- Neví, *čím* se kopie liší, musí soubory porovnávat očima.
- Zabírá místo a snadno se splete při odevzdání.
- Po rozbití kódu neví, který soubor ještě fungoval.

Git: jeden projekt, řada commitů se zprávou, návrat k funkčnímu snímku, později i kopie na GitHubu.
@end

---

## Cvičení 2 — Git, nebo GitHub? (★☆☆)

Ke každé situaci napište **Git**, **GitHub**, nebo **obojí**.

1. Uložíte snímek projektu, když nemáte internet.
2. V prohlížeči čtete cizí `README` a seznam souborů.
3. V PyCharmu / VS Code stisknete Commit.
4. Spolužák vám pošle odkaz `https://github.com/…`.
5. Historie commitů existuje ve skryté složce `.git`.

@reseni
1. Git (lokální historie).
2. GitHub (web).
3. Git (IDE jen ovládá Git).
4. GitHub (adresa vzdálené kopie).
5. Git (`.git` je na disku; GitHub ji nemá v té podobě u vás).
@end

---

## Cvičení 3 — Co patří do commitu (★★☆)

U každé položky rozhodněte: **commitnout** / **ignorovat** (`.gitignore`) / **nikdy do Gitu**.

- `main.py` s vaším úkolem
- složka `__pycache__`
- soubor `.env` s heslem k e-mailu
- `README.md` s popisem projektu
- složka `.venv` s nainstalovaným Pythonem
- `data.txt`, ze kterého program čte čísla (součást zadání)

@reseni
| Položka | Rozhodnutí |
|---------|------------|
| `main.py` | commitnout |
| `__pycache__` | ignorovat |
| `.env` s heslem | nikdy do Gitu |
| `README.md` | commitnout |
| `.venv` | ignorovat |
| `data.txt` ze zadání | commitnout |
@end

---

## Cvičení 4 — Commit v IDE (★★☆)

V editoru otevřete **složku** (ne jeden soubor) s libovolným malým programem z 1. ročníku — nebo novou složku s `ahoj.py` a `print("Ahoj")`.

1. Inicializujte Git (Initialize Repository / Enable Version Control).
2. Přidejte `.gitignore` podle `priklady/gitignore-python.txt`.
3. Připravte soubory, napište konkrétní zprávu, proveďte **Commit**.
4. Změňte jeden `print`, uložte, commitněte podruhé.
5. Otevřete historii (Log / Timeline) a ověřte, že vidíte **oba** commity a diff druhé změny.

Do dokumentu napište: znění obou zpráv a jednu větu, *co* diff ukázal.

@reseni
Příklad zpráv:

1. `První verze pozdravu`
2. `Změna textu pozdravu`

Diff: v `ahoj.py` zmizel řádek se starým řetězcem a přibyl nový (červená / zelená). Dva commity v Logu. Bez konzole.
@end

---

## Cvičení 5 — Vzdálená kopie (★★☆)

Toto cvičení jen **pokud** máte účet na GitHubu (nebo školní GitLab) a učitel to chce zkoušet.

V IDE použijte **Publish** / **Push** a založte **soukromý** (*private*) repozitář. V prohlížeči otevřete stránku projektu.

Napište:

- je vidět váš `ahoj.py`?
- kolik commitů web ukazuje?
- proč je u školního úkolu lepší *private* než *public*?

@reseni
Soubor na záložce Code ano. Počet commitů = počet snímků z cvičení 4 (typicky 2). *Private*: cizí lidé (a jiné školy) nevidí řešení úkolu ani případné údaje; *public* je vidět celý internet.
@end
