# Predavanje 1 — Čitanje i Pisanje Tekstualnih Fajlova

## 1.1 Funkcija open()

| Mod | Opis |
|---|---|
| `"r"` | Čitanje (Read) — podrazumevani |
| `"w"` | Pisanje (Write) — briše postojeće |
| `"a"` | Dodavanje (Append) — na kraj |
| `"x"` | Kreiranje — greška ako postoji |

## 1.2 Context Manager (with)

```python
with open("fajl.txt", "r") as f:
    sadrzaj = f.read()
# Fajl se automatski zatvara nakon bloka
```

## 1.3 Metode čitanja

| Metoda | Opis |
|---|---|
| `f.read()` | Ceo fajl kao string |
| `f.readline()` | Jedna linija |
| `f.readlines()` | Lista svih linija |
| `for line in f:` | Iteracija liniju po liniju |

## Rezime
- Uvek koristiti `with` za automatsko zatvaranje
- `"r"` čita, `"w"` piše (briše), `"a"` dodaje
- `encoding="utf-8"` za Unicode podršku
