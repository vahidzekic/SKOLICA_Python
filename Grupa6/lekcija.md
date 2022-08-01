# Grupa 6 — Moduli, Funkcije i Rad sa Fajlovima

## 6.1 Šta su funkcije?

Funkcija je **imenovani, ponovljivo upotrebljiv blok koda** koji izvršava specifičan zadatak. Funkcije omogućavaju:
- **DRY princip** — Don't Repeat Yourself (ne ponavljaj se)
- **Modularnost** — podela koda na logičke celine
- **Testabilnost** — lakše testiranje izolovanih delova koda

### Sintaksa:
```python
def ime_funkcije(parametar1, parametar2):
    """Docstring — opis funkcije."""
    rezultat = parametar1 + parametar2
    return rezultat
```

### Pozivanje funkcije:
```python
zbir = ime_funkcije(5, 3)  # zbir = 8
```

---

## 6.2 Parametri i argumenti

| Pojam | Opis | Primer |
|---|---|---|
| **Parametar** | Varijabla u definiciji funkcije | `def f(x, y):` |
| **Argument** | Vrednost prosleđena pri pozivu | `f(5, 3)` |
| **Podrazumevana vrednost** | Default ako argument nije dat | `def f(x=10):` |
| **\*args** | Proizvoljan broj pozicionih argumenata | `def f(*args):` |
| **\*\*kwargs** | Proizvoljan broj imenovanih argumenata | `def f(**kwargs):` |

```python
def pozdrav(ime, pozdravna_rec="Zdravo"):
    return f"{pozdravna_rec}, {ime}!"

print(pozdrav("Vahid"))              # "Zdravo, Vahid!"
print(pozdrav("Vahid", "Ćao"))       # "Ćao, Vahid!"
```

---

## 6.3 Moduli

Modul je **Python fajl** (`.py`) koji sadrži funkcije, klase i varijable namenjene za ponovnu upotrebu.

### Kreiranje modula:
```python
# fajl: modul_operacije.py
def sabiranje(a, b):
    return a + b

def oduzimanje(a, b):
    return a - b
```

### Importovanje modula:
```python
# fajl: program.py
from modul_operacije import sabiranje, oduzimanje

rezultat = sabiranje(10, 5)  # 15
```

### Načini importovanja:

| Sintaksa | Opis |
|---|---|
| `import modul` | Importuje ceo modul (`modul.funkcija()`) |
| `from modul import funkcija` | Importuje specifičnu funkciju |
| `from modul import *` | Importuje sve (nije preporučeno) |
| `import modul as m` | Importuje sa aliasom (`m.funkcija()`) |

---

## 6.4 Rad sa fajlovima

Python omogućava čitanje i pisanje fajlova koristeći ugrađenu funkciju `open()`:

### Modovi otvaranja fajla:

| Mod | Opis |
|---|---|
| `"r"` | Čitanje (Read) — podrazumevani mod |
| `"w"` | Pisanje (Write) — briše postojeći sadržaj |
| `"a"` | Dodavanje (Append) — dodaje na kraj fajla |
| `"x"` | Kreiranje (Create) — greška ako fajl postoji |

### Čitanje fajla:
```python
with open("podaci.txt", "r") as fajl:
    sadrzaj = fajl.read()
    print(sadrzaj)
```

### Pisanje u fajl:
```python
with open("podaci.txt", "w") as fajl:
    fajl.write("Prva linija\n")
    fajl.write("Druga linija\n")
```

> **`with` statement:** Automatski zatvara fajl nakon završetka bloka — ovo je preporučen pristup.

---

## 6.5 Rad sa JSON fajlovima

Python-ov `json` modul omogućava serijalizaciju (pretvaranje) Python objekata u JSON format i obrnuto.

### Čitanje JSON fajla:
```python
import json

with open("podaci.json", "r") as fajl:
    podaci = json.load(fajl)      # Konvertuje JSON → Python dict/list
```

### Pisanje u JSON fajl:
```python
import json

podaci = [{"ime": "Vahid", "godine": 34}]

with open("podaci.json", "w") as fajl:
    json.dump(podaci, fajl, indent=4)   # indent za formatiranje
```

### Konverzija:

| JSON tip | Python tip |
|---|---|
| `object {}` | `dict` |
| `array []` | `list` |
| `string` | `str` |
| `number (int)` | `int` |
| `number (float)` | `float` |
| `true/false` | `True/False` |
| `null` | `None` |

---

## 6.6 Ugniježđeni moduli i paketi

Za veće projekte, moduli se organizuju u **pakete** (direktorijumi sa `__init__.py`):

```
moj_paket/
├── __init__.py
├── matematika.py
├── stringovi.py
└── baza_podataka.py
```

```python
from moj_paket.matematika import sabiranje
```

---

## Rezime Grupe 6

| Koncept | Opis |
|---|---|
| `def` | Definicija funkcije |
| `return` | Vraćanje vrednosti iz funkcije |
| `import` | Importovanje modula |
| `open()` | Otvaranje fajla |
| `json.load()` | Čitanje JSON fajla → Python |
| `json.dump()` | Python → JSON fajl |
| `with` | Kontekst menadžer za fajlove |
