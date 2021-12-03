# Predavanje 1 — Uvod u Python i Sintaksu

## 1.1 Šta je Python?

Python je interpretirani programski jezik visokog nivoa kreiran 1991. godine od strane **Guido van Rossum-a**. Odlikuje se čistom sintaksom gde se blokovi koda definišu **indentacijom** (uvlačenjem), a ne vitičastim zagradama kao u C ili JavaScript-u.

### Karakteristike Python-a:
| Karakteristika | Opis |
|---|---|
| Dinamičko tipiziranje | Tip varijable se određuje automatski |
| Interpretirani | Izvršava se liniju po liniju, bez kompilacije |
| Multi-paradigmatski | Proceduralno, OOP, funkcionalno |
| Bogata std. biblioteka | Ugrađeni moduli za sve |

## 1.2 Struktura Python programa

```python
# Ovo je komentar — interpreter ga ignoriše
print("Zdravo, svete!")   # Funkcija za ispis na konzolu
```

### Pravila sintakse:
- **Indentacija** je obavezna (4 razmaka ili 1 tab)
- Nema tačke-zareza `;` na kraju linije (opciono)
- Komentari počinju sa `#`
- Višelinijski komentari: `\"\"\"...\"\"\"` (trostruki navodnici)

## 1.3 Funkcija `print()`

`print()` je ugrađena funkcija za ispis na standardni izlaz (konzolu):

```python
print("Tekst")              # Ispisuje string
print(42)                   # Ispisuje broj
print("A", "B", "C")        # Više argumenata, razdvojeni razmakom
print("X", end="")          # Bez novog reda na kraju
```

## Rezime
- Python koristi indentaciju za blokove koda
- `print()` za ispis, `#` za komentare
- Nema deklaracije tipova — dinamičko tipiziranje
