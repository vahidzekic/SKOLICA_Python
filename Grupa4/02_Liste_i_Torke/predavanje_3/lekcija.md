# Predavanje 3 — Torke (Tuples)

## Lista vs Torka
| Osobina | Lista | Torka |
|---|---|---|
| Sintaksa | `[a,b]` | `(a,b)` |
| Promenljiva | Da | Ne |
| Hashable | Ne | Da |

## Unpacking
```python
lat, lon = (44.0, 20.9)
a, *rest = (1,2,3,4,5)
```

## Rezime
- Torka za fiksne podatke
- Brža i memorijski efikasnija od liste
