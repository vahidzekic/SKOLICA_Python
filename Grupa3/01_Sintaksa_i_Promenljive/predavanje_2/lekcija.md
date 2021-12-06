# Predavanje 2 — Promenljive i Dodela Vrednosti

## 2.1 Šta je promenljiva?

Promenljiva (varijabla) je **imenovana lokacija u memoriji** koja čuva neku vrednost. U Python-u se kreira prostom dodelom — bez ključne reči `var`, `let`, ili `int`.

```python
ime = "Vahid"          # string
godine = 34            # int
visina = 1.82          # float
aktivan = True         # bool
```

## 2.2 Pravila imenovanja

| Pravilo | Ispravan primer | Neispravan primer |
|---|---|---|
| Počinje slovom ili `_` | `moj_broj`, `_temp` | `1broj`, `@var` |
| Samo slova, cifre, `_` | `broj_1` | `moj-broj`, `moj broj` |
| Case-sensitive | `Ime` ≠ `ime` | — |
| Ne sme biti ključna reč | `rezultat` | `print`, `for`, `class` |

### Konvencije:
- **snake_case** za varijable i funkcije: `moj_broj`, `izracunaj_prosek()`
- **PascalCase** za klase: `MojaKlasa`, `StudentFakulteta`
- **UPPER_CASE** za konstante: `MAX_VREDNOST`, `PI`

## 2.3 Višestruka dodela

```python
x, y, z = 1, 2, 3           # Tri varijable u jednoj liniji
a = b = c = 0                # Ista vrednost za sve
ime, *ostalo = "Vahid", "Zekic", 34   # Unpacking sa *
```

## 2.4 Funkcija `type()`

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("tekst"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

## Rezime
- Promenljive se kreiraju dodelom: `x = 5`
- Python je case-sensitive
- `type()` za proveru tipa podatka
