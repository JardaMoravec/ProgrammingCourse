---
id: 01-programovani-a-jazyky
rocnik: 1
nazev: Programování a programovací jazyky
hodiny: 3
obtiznost: zacatecnik
prerekvizity: []
cile:
  - Vysvětlí, co je programování a program
  - Rozliší vyšší a nižší programovací jazyky
  - Porovná kompilované, interpretované jazyky a jazyky s virtuálním strojem
  - Rozliší programovací a značkovací jazyky
migrovano_z:
  - "zdroje/Programování 1.docx (kap. Programovací jazyky)"
  - "zdroje/01 - Úvod do Pythonu.pptx"
---

# Programování a programovací jazyky

## Cíle lekce

- Pochopíte, co je programování a k čemu slouží
- Naučíte se základní dělení programovacích jazyků
- Připravíte se na práci v Pythonu v dalších lekcích

## Co je programování?

**Programování** je systematický proces vytváření logických instrukcí (algoritmů), které počítač provádí. Nejedná se jen o psaní kódu — jde o:

- analýzu problému,
- návrh postupu řešení,
- automatizaci práce,
- ukládání a zpracování dat.

**Program** je zápis algoritmu ve zvoleném programovacím jazyce.

## Co je programovací jazyk?

Programovací jazyk je **prostředník** mezi člověkem a počítačem. Překlenuje propast mezi lidským uvažováním a strojovým kódem (jedničky a nuly).

Každý jazyk má:

- **syntaxi** — striktní pravidla zápisu,
- **sémantiku** — význam příkazů,
- **ekosystém** — nástroje, knihovny, komunitu.

## Vyšší a nižší jazyky

| Úroveň | Příklady | Charakteristika |
|--------|----------|-----------------|
| **Nižší** | Assembler, VHDL | Strojové instrukce pro konkrétní procesor |
| **Vyšší** | Python, Java, C# | Abstraktnější, srozumitelnější pro člověka |

## Tři způsoby spuštění kódu

### 1. Kompilované jazyky

Zdrojový kód se **před spuštěním** přeloží kompilátorem do strojového kódu.

**Příklady:** C, C++, Pascal, Rust

| Výhody | Nevýhody |
|--------|----------|
| vysoký výkon | složitější kód |
| distribuce bez zdrojáků | strmější učící křivka |

### 2. Interpretované jazyky

Kód se **překládá za běhu** — interpret čte instrukce po instrukci.

**Příklady:** Python, PHP, Ruby

| Výhody | Nevýhody |
|--------|----------|
| rychlý vývoj | nižší výkon |
| snadné učení | chyby až při spuštění |
| | nutnost poskytnout zdrojový kód |

### 3. Jazyky s virtuálním strojem

Kompromis — kód se kompiluje do mezikódu (bytecode), který běží na virtuálním stroji.

**Příklady:** Java, C#

| Výhody | Nevýhody |
|--------|----------|
| lepší výkon než interpret | nižší výkon než nativní kompilace |
| přenositelnost | |
| distribuce bez zdrojáků | |

## Programovací vs. značkovací jazyky

**Značkovací jazyky** (HTML, XML) nepopisují algoritmus, ale **strukturu dat** pomocí značek (tagů).

**Programovací jazyky** popisují **postup** — co má počítač udělat.

## Proč právě Python?

Python je **interpretovaný, dynamicky typovaný** jazyk — ideální pro začátečníky:

- čitelná syntaxe (odsazování místo složených závorek),
- rychlá zpětná vazba při učení,
- široké uplatnění (web, data, automatizace, AI),
- bohatá komunita a knihovny.

Detailněji v další lekci: [02-python-a-prostredi](../02-python-a-prostredi/lekce.md).

## Shrnutí

| Pojem | Význam |
|-------|--------|
| Algoritmus | Postup řešení problému |
| Program | Algoritmus zapsaný v jazyce |
| Kompilátor | Překladač do strojového kódu |
| Interpret | Spouští kód řádek po řádku |
| Bytecode | Mezikód pro virtuální stroj |

## Co dál

→ [Lekce 02: Python a vývojové prostředí](../02-python-a-prostredi/lekce.md)
