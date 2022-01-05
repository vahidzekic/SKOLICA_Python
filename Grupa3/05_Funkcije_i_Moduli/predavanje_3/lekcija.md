# Predavanje 3 — Moduli i Paketi

## 3.1 Šta je modul?

Modul je Python fajl (`.py`) sa funkcijama, klasama i varijablama za ponovnu upotrebu.

## 3.2 Načini importovanja

| Sintaksa | Upotreba |
|---|---|
| `import math` | `math.sqrt(16)` |
| `from math import sqrt` | `sqrt(16)` |
| `from math import *` | `sqrt(16)` (ne preporučuje se) |
| `import math as m` | `m.sqrt(16)` |

## 3.3 Kreiranje sopstvenog modula

```python
# fajl: moj_modul.py
def saberi(a, b):
    return a + b

# fajl: program.py
from moj_modul import saberi
print(saberi(5, 3))
```

## 3.4 `if __name__ == "__main__"`

```python
def main():
    print("Ovo se izvršava samo ako se fajl pokrene direktno")

if __name__ == "__main__":
    main()
```

## Rezime
- Modul = Python fajl sa reupotrebljivim kodom
- `import`, `from...import`, `as` alias
- `__name__ == "__main__"` za razlikovanje import vs direktno pokretanje
