# Predavanje 1 — Osnove Try/Except

## 1.1 Šta su izuzeci (Exceptions)?

Izuzetak je greška koja se dešava tokom izvršavanja programa. Bez obrade, program se ruši.

## 1.2 Try/Except blok

```python
try:
    rezultat = 10 / 0
except ZeroDivisionError:
    print("Ne može se deliti nulom!")
```

## 1.3 Česti tipovi izuzetaka

| Izuzetak | Uzrok |
|---|---|
| `ZeroDivisionError` | Deljenje nulom |
| `ValueError` | Nevalidan tip/vrednost |
| `TypeError` | Pogrešan tip operanda |
| `FileNotFoundError` | Fajl ne postoji |
| `KeyError` | Ključ ne postoji u rečniku |
| `IndexError` | Indeks van opsega |

## 1.4 Try/Except/Else/Finally

```python
try:
    # Kod koji može baciti izuzetak
except TipGreske:
    # Obrada greške
else:
    # Izvršava se AKO NEMA greške
finally:
    # Izvršava se UVEK (čišćenje resursa)
```

## Rezime
- `try/except` hvata greške bez rušenja programa
- `else` — ako nema greške; `finally` — uvek
- Hvatati specifične izuzetke, ne generički `except:`
