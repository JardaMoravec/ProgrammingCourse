# Cvičení — HTML a CSS — shrnutí

## Cvičení 1 — Strom HTML (★☆☆)

Prohlížeč z tohoto úryvku postaví jiný strom, než autor čekal. Najděte **dvě** chyby a napište, co prohlížeč pravděpodobně udělá.

```html
<body>
  <p>Úvod
    <div class="box">Důležitá informace</div>
  </p>
  <ul>
    <li>Pondělí
    <li>Úterý</li>
  </ul>
</body>
```

@reseni
1. `<div>` uvnitř `<p>` — odstavec se uzavře před `div`. `div` bude **sourozenec** odstavce, ne dítě. Závěrečné `</p>` je pak navíc / mimo.
2. První `<li>` není uzavřené. Prohlížeč ho obvykle uzavře před dalším `<li>`, ale ve složitějším kódu se uzly posunou. Bezpečné je `<li>…</li>` vždy párově.
@end

---

## Cvičení 2 — Která barva vyhraje? (★★☆)

Jakou barvu bude mít text? Krátce zdůvodněte.

```html
<p class="perex" id="uvod">Ahoj</p>
```

```css
p { color: navy; }
.perex { color: crimson; }
#uvod { color: seagreen; }
p.perex { color: orange; }
```

@reseni
**Zelená** (`seagreen`). Specifita: prvek `p` (nejnižší) → třída `.perex` a `p.perex` (střed) → id `#uvod` (nejvyšší). `p.perex` je silnější než samotné `.perex`, ale pořád slabší než `#uvod`.
@end

---

## Cvičení 3 — Šířka boxu (★★☆)

```css
.karta {
  width: 200px;
  padding: 16px;
  border: 4px solid;
}
```

Jak široký je vykreslený box při výchozím `box-sizing: content-box`? Co se změní s `border-box`?

@reseni
**Content-box:** 200 + 16+16 + 4+4 = **240 px**.

**Border-box:** `width: 200px` už zahrnuje padding i border, kreslená šířka je **200 px** (na obsah zbude 200 − 32 − 8 = 160 px).
@end

---

## Cvičení 4 — Pořadí v prohlížeči (★☆☆)

Seřaďte kroky, jak prohlížeč složí stránku:

A. vykreslení pixelů  
B. stažení a rozbor CSS  
C. DOM (strom z HTML)  
D. výpočet boxů (layout)  
E. stažení HTML

@reseni
**E → C → B → D → A** (B může částečně běžet souběžně s C, jakmile parser v `<head>` najde `<link>` — ale CSS musí být hotové, než se spočítají finální boxy a barvy).

Stručně: HTML → strom, CSS → pravidla, spojení → layout → obrazovka.
@end
