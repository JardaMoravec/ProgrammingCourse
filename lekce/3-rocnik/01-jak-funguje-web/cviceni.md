# Cvičení — Jak funguje web

## Cvičení 1 — Části URL (★☆☆)

Rozepište u každé adresy: schéma, hostitel, port (i když je výchozí), cesta, query.

1. `https://obchod.cz/kosik`
2. `http://127.0.0.1:5000/clanky?id=7`
3. `https://www.skola.cz/rozvrh?den=utery&trida=3A#odpoledne`

@reseni
| URL | Schéma | Hostitel | Port | Cesta | Query |
|-----|--------|----------|------|-------|-------|
| 1 | `https` | `obchod.cz` | `443` (výchozí) | `/kosik` | — |
| 2 | `http` | `127.0.0.1` | `5000` | `/clanky` | `id=7` |
| 3 | `https` | `www.skola.cz` | `443` (výchozí) | `/rozvrh` | `den=utery&trida=3A` |

U 3. adresy `#odpoledne` je **fragment** — na server se neposílá.
@end

---

## Cvičení 2 — Klient, nebo server? (★☆☆)

U každé situace napište, kdo je klient a kdo server.

1. Otevřete v prohlížeči zpravodajský web.
2. Spustíte Flask na svém PC a v prohlížeči zadáte `http://127.0.0.1:5000`.
3. Mobilní aplikace stáhne seznam jízdních řádů z webu dopravce.

@reseni
1. Klient = prohlížeč, server = počítač zpravodajského webu.
2. Klient = prohlížeč, server = Flask na *tomto* počítači. Obě role jsou na jednom stroji.
3. Klient = mobilní aplikace, server = **API** dopravce (data, ne nutně HTML stránka).
@end

---

## Cvičení 3 — Stavové kódy (★★☆)

Jaký kód (nebo kategorii) čekáte?

1. Stránka se zobrazila v pořádku.
2. Zadali jste `/neexistuje` a Flask tuto routu nemá.
3. V Pythonu na serveru nastala neošetřená výjimka.
4. Po odeslání formuláře vás aplikace pošle na `/dekujeme`.

@reseni
1. `200 OK`
2. `404 Not Found`
3. `500 Internal Server Error`
4. `302` (přesměrování) a potom `200` na cílové stránce
@end
