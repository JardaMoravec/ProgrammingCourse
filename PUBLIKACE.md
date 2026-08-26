# Publikace kurzu na GitHub Pages

Studijní web se po každém pushi do větve `main` automaticky znovu sestaví a nasadí.

## Doporučené nastavení repozitáře

Repozitář může být **veřejný** — referenční řešení úkolů v repozitáři nejsou (VPL používá jen `vpl_evaluate.cases`). Řešení cvičení v hodině jsou v HTML materiálech u `@reseni` (záměr pro výuku).

Pro soukromý zdrojový kód je stále možné repo nechat private; Pages ze soukromého repa vyžaduje **GitHub Pro** nebo **[GitHub Education](https://education.github.com/)**.

## Jednorázové zprovoznění

### 1. Repozitář na GitHubu

```bash
git init -b main
git add -A
git commit -m "Initial commit: kurz programování 1.–3. ročník"
```

Vytvořte na GitHubu **prázdné** repo (bez README) a propojte ho:

```bash
git remote add origin https://github.com/VAS-UCET/kurz-programovani.git
git push -u origin main
```

Nebo přes GitHub CLI:

```bash
gh repo create kurz-programovani --private --source=. --remote=origin --push
```

### 2. Zapnout GitHub Pages

1. GitHub → **Settings** → **Pages**
2. **Build and deployment** → Source: **GitHub Actions**
3. Po prvním pushi (nebo ručním spuštění workflow) se web objeví na adrese uvedené v Actions / Pages.

Typická URL projektového webu:

`https://<ucet>.github.io/kurz-programovani/`

### 3. Odkaz pro žáky a Moodle

| Účel | URL |
|------|-----|
| Přehled ročníků | `https://<ucet>.github.io/kurz-programovani/` |
| 1. ročník | `https://<ucet>.github.io/kurz-programovani/1-rocnik/` |

Úkoly pro Moodle (VPL) zůstávají v LMS — viz [`moodle/README.md`](../moodle/README.md).

## Běžná práce (automatický deploy)

```text
1. Upravte `lekce/**/*.md` nebo `lekce/**/ukoly/*/ukol.yaml`
2. git add -A && git commit -m "Lekce 07: doplnění cvičení"
3. git push
4. Za ~1–2 minuty je web aktualizovaný (GitHub → Actions)
```

Lokální náhled před pushem:

```bash
pip install -r requirements.txt
python scripts/generate_tasks.py
python scripts/build_html_output.py
# otevřete graficky-vystup/index.html
```

Složka `graficky-vystup/` je v `.gitignore` — do Gitu nepatří, vždy se generuje.

## Workflow soubor

Automatizaci řídí [`.github/workflows/publish.yml`](../.github/workflows/publish.yml):

1. instalace Pythonu a závislostí
2. `generate_tasks.py`
3. `build_html_output.py`
4. nasazení obsahu `graficky-vystup/` na GitHub Pages

Ruční spuštění: GitHub → **Actions** → **Publish course site** → **Run workflow**.

## Vlastní doména (volitelně)

Settings → Pages → Custom domain → např. `programovani.vase-skola.cz`  
U DNS poskytovatele CNAME záznam na `<ucet>.github.io`.

## Řešení problémů

| Problém | Řešení |
|---------|--------|
| Workflow selže | Actions → konkrétní běh → červený krok → log |
| Pages nejsou vidět | Settings → Pages → zdroj musí být **GitHub Actions** |
| Starý obsah | Vyčkejte na dokončení deploye; případně hard refresh (Ctrl+F5) |
| Soukromý repo, Pages nejdou | Ověřte GitHub Pro / Education, nebo použijte veřejný repo jen pro web |
