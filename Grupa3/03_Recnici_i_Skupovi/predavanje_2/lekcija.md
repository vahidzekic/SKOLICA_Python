# Predavanje 2 — Skupovi (Sets)

## 2.1 Šta je skup?

Skup (`set`) je **neuređena** kolekcija **jedinstvenih** elemenata. Automatski uklanja duplikate.

```python
s = {1, 2, 2, 3, 3, 3}    # Rezultat: {1, 2, 3}
s = set([1, 1, 2, 2, 3])   # Isto: {1, 2, 3}
```

## 2.2 Operacije sa skupovima

| Operacija | Metoda | Operator |
|---|---|---|
| Unija | `a.union(b)` | `a \| b` |
| Presek | `a.intersection(b)` | `a & b` |
| Razlika | `a.difference(b)` | `a - b` |
| Simetrična razlika | `a.symmetric_difference(b)` | `a ^ b` |

## 2.3 Metode skupova

| Metoda | Opis |
|---|---|
| `s.add(x)` | Dodaje element |
| `s.remove(x)` | Briše (greška ako ne postoji) |
| `s.discard(x)` | Briše (bez greške) |
| `s.issubset(b)` | Da li je `s` podskup `b`? |

## Rezime
- Set: `{}`, neuređen, bez duplikata
- Koristiti za uklanjanje duplikata i matematičke operacije skupova
- `frozenset()` za nepromenljive skupove
