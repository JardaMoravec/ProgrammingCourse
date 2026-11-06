# Cvičení — Vlastnosti a `@property`

## Cvičení 1 — Převod teploty (★☆☆)

Třída `Teplomer` ukládá teplotu ve stupních Celsia do atributu
`celsia`. Přidejte vlastnost `fahrenheit`, která vrátí teplotu převedenou
vztahem `celsia * 9 / 5 + 32`. Vypište hodnotu pro `Teplomer(20)`.

@reseni
```python
class Teplomer:
    def __init__(self, celsia):
        self.celsia = celsia

    @property
    def fahrenheit(self):
        return self.celsia * 9 / 5 + 32


print(Teplomer(20).fahrenheit)
```
@end

---

## Cvičení 2 — Hodnocení filmu (★★☆)

Třída `Film` má vlastnost `hodnoceni`. Setter povolí jen celá čísla
od 0 do 10; jinak vyvolá `ValueError`. Ověřte vytvoření filmu
s hodnocením 7 a jeho změnu na 9.

@reseni
```python
class Film:
    def __init__(self, hodnoceni):
        self.hodnoceni = hodnoceni

    @property
    def hodnoceni(self):
        return self._hodnoceni

    @hodnoceni.setter
    def hodnoceni(self, hodnota):
        if not 0 <= hodnota <= 10:
            raise ValueError("Hodnoceni musi byt od 0 do 10")
        self._hodnoceni = hodnota


film = Film(7)
film.hodnoceni = 9
print(film.hodnoceni)
```
@end
