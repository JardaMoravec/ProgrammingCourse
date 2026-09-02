# Vzor návrhu — Knihovna (autor → kniha)

Toto **není** povinné téma ani povinné názvy. Ukazuje, jak má vypadat schválený návrh.

| Položka | Příklad |
|---------|---------|
| Název webu | Knihovna 3. A |
| Rodič | autor — tabulka `autori` (`id`, `jmeno`) |
| Potomek | kniha — tabulka `knihy` (`id`, `titul`, `rok`, `obalka`, `autor_id`) |
| Cesty | `/`, `/autori`, `/knihy/nova`, `/kniha/<id>`, `/ja`, … |
| Dva autoři | Saint-Exupéry; Čapek |
| Tři knihy | Malý princ / Saint-Exupéry / 1943; R.U.R. / Čapek / 1920; Krakatit / Čapek / 1924 |

Fotka je obálka ve `static/`. Na seznamu je vidět kniha i autor (`JOIN`).
