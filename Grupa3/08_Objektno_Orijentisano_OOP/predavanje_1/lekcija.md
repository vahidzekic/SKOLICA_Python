# Predavanje 1 — Klase i Objekti

## 1.1 Šta je klasa?

Klasa je **nacrt** za kreiranje objekata. Objekat je **instanca** klase.

```python
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def predstaviSe(self):
        return f"{self.ime} {self.prezime}, {self.godine} god."
```

## 1.2 Elementi klase

| Element | Opis |
|---|---|
| `__init__` | Konstruktor |
| `self` | Referenca na trenutni objekat |
| Atributi | Varijable objekta (`self.ime`) |
| Metode | Funkcije objekta |
| `__str__` | String reprezentacija |

## Rezime
- `class ImeKlase:` za deklaraciju
- `__init__` se poziva automatski pri kreiranju objekta
- `self` je obavezni prvi parametar svake metode
