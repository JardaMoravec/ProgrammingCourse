# Cvičení — API: REST a GraphQL

Nic se neinstaluje. Cvičení jsou na papír / do dokumentu.

---

## Cvičení 1 — REST požadavek (★☆☆)

Ke každé potřebě napište HTTP metodu a cestu ve stylu REST (knihovna).

1. Zobrazit seznam všech knih.
2. Zobrazit knihu s `id` 8.
3. Odeslat novou knihu (JSON v těle).

@reseni
1. `GET /knihy`
2. `GET /knihy/8`
3. `POST /knihy` (tělo: JSON s názvem a autorem)
@end

---

## Cvičení 2 — Proč dva požadavky (★★☆)

Klient v REST nejdřív zavolá `GET /knihy/1` a dostane:

```json
{"id": 1, "nazev": "Robot", "autor_id": 5}
```

Na obrazovce má být **název knihy a jméno autora**. Proč nestačí jeden tenhle požadavek? Jaký bude druhý?

@reseni
V první odpovědi je jen `autor_id`, ne jméno. Druhý požadavek: `GET /autori/5`. (Server *mohl* jméno vnořit už do `/knihy/1` — ale tahle dohoda to neudělala.)
@end

---

## Cvičení 3 — GraphQL dotaz (★★☆)

Napište GraphQL `query`, který z knihy `id` 1 vytáhne **jen** `nazev` a u autora **jen** `jmeno` (vnořené `autor { … }`).

@reseni
```graphql
query {
  kniha(id: 1) {
    nazev
    autor {
      jmeno
    }
  }
}
```

Pole `rok` ani `autor_id` v dotazu nejsou — v odpovědi by být neměla.
@end

---

## Cvičení 4 — Který styl? (★☆☆)

Ke každé situaci **REST**, **GraphQL**, nebo **oba** a jedna věta.

1. Školní Flask projekt ze 3. ročníku (HTML šablony, formuláře, `sqlite3`).
2. Mobilní aplikace, každá obrazovka chce jinou kombinaci polí ze stejných entit.
3. Cizí dokumentace uvádí `GET /jizdni-rady?zastavka=12`.

@reseni
1. **REST** (vlastně HTML přes routy) — GraphQL do projektu nepatří.
2. **GraphQL** — jeden dotaz na potřebná pole; REST by množil cesty nebo posílal navíc.
3. **REST** — cesta + query parametry, klasický zdroj.
@end
