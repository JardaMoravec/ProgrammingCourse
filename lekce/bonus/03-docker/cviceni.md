# Cvičení — Docker

Cvičení jsou **pojmová** a případně **prohlídka v Docker Desktop / IDE**. Příkazy `docker …` nepište. Pokud Desktop ve škole není, stačí cvičení 1–3.

---

## Cvičení 1 — „U mě to funguje“ (★☆☆)

Kamarád vám pošle jen soubor `graf.py`. U vás padá na `ModuleNotFoundError: matplotlib`. U něj ve škole program vykreslil graf.

Vysvětlete **vlastními slovy**:

1. co je špatně na posílání „jen toho jednoho souboru“,
2. jak by stejnému problému předešel **obraz** s Pythonem a knihovnami,
3. proč to Git **nespraví** (i kdyby byl `graf.py` na GitHubu).

@reseni
1. Druhý počítač nemá stejné okolí — chybí balíček, někdy i verze Pythonu.
2. Obraz už obsahuje interpret i `matplotlib`; kontejner z něj spustí program bez ruční instalace u každého.
3. Git přenese *kód*, ne nainstalované knihovny. Na GitHubu bude stejný `graf.py` a stejná chyba, dokud okolí nedoplníte (nebo ho nezabalíte).
@end

---

## Cvičení 2 — Obraz, nebo kontejner? (★☆☆)

Ke každé situaci napište **obraz**, **kontejner**, nebo **obojí**.

1. V Docker Desktop ve sloupci Images vidíte `python:3.12`.
2. Po stisku Run přibyl řádek se stavem *running*.
3. Čtete log s výstupem `print`.
4. Z jednoho `python:3.12` jdou pustit dvě kopie najednou.
5. Soubor `Dockerfile` popisuje, z čeho se má šablona postavit.

@reseni
1. Obraz.
2. Kontejner (vznikl z obrazu).
3. Kontejner (běží, proto má výstup).
4. Obraz je jeden, kontejnery dva.
5. Obraz (recept pro stavbu šablony; kontejner ještě není).
@end

---

## Cvičení 3 — VM, nebo kontejner? (★★☆)

Zařaďte: **VM** / **kontejner** / **oba**.

1. Chcete na Windows vyzkoušet celý cizí Linux včetně vlastního jádra.
2. Chcete deset stejných kopií webové služby bez deseti kompletních OS.
3. Program má být oddělený od ostatních programů na počítači.
4. Start má trvat vteřiny a obraz má mít stovky MB, ne desítky GB.
5. Škola vám dá hotový „malý počítač“ s Windows ve VirtualBoxu.

@reseni
1. VM.
2. Kontejner.
3. Oba (izolace je cíl u obou).
4. Kontejner.
5. VM.
@end

---

## Cvičení 4 — Čtení Dockerfile (★★☆)

Otevřete v IDE `priklady/Dockerfile`. U každého řádku napište jednou větou, **co udělá** (ne překlad slova do slova).

Pak odpovězte: patří tento `Dockerfile` do Gitu? Patří do Gitu hotový stažený obraz z Docker Hubu?

@reseni
- `FROM python:3.12-slim` — vezmi hotový základ s Pythonem 3.12.
- `WORKDIR /app` — další kroky (a běh) probíhají ve složce `/app` uvnitř obrazu.
- `COPY main.py .` — zkopíruj školní program do té složky.
- `CMD ["python", "main.py"]` — po startu kontejneru spusť tento soubor.

`Dockerfile` **ano** (text projektu). Hotový obraz **ne** — je velký a stahuje se z registru, do commitu nepatří.
@end

---

## Cvičení 5 — Prohlídka Desktopu (★★☆)

Jen pokud ve škole běží **Docker Desktop** (ikona v oznamovací oblasti je připravená).

1. Otevřete Images a Containers.
2. Najděte libovolný obraz (třeba `python`) — pokud žádný není, **nestahujte** neznámé obrazy bez učitele.
3. Pokud učitel povolí Run na školním obrazu, spusťte ho a otevřete **Logs**.
4. Zastavte kontejner tlačítkem Stop.

Do dokumentu: kolik obrazů a kolik kontejnerů jste viděli, a jednu větu rozdílu mezi sloupci.

@reseni
Čísla se liší podle počítače. Images = šablony. Containers = exempláře (running / exited). Log = výstup běhu, ne seznam souborů v Gitu. Bez příkazů v konzoli.
@end
