# Predavanje 2 — FOR Petlja i Iteracija

## 2.1 FOR petlja

```python
for element in sekvenca:
    print(element)
```

## 2.2 range() funkcija

| Poziv | Rezultat |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 8)` | 2, 3, 4, 5, 6, 7 |
| `range(0, 20, 5)` | 0, 5, 10, 15 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |

## 2.3 enumerate() i zip()

```python
for i, val in enumerate(lista):
    print(f"[{i}] {val}")

for ime, ocena in zip(imena, ocene):
    print(f"{ime}: {ocena}")
```

## 2.4 break i continue

- `break` — potpuno prekida petlju
- `continue` — preskače ostatak iteracije
- `pass` — placeholder (ništa ne radi)

## Rezime
- `for x in sekvenca` — iteracija kroz sve elemente
- `range(start, stop, step)` za numeričke opsege
- `enumerate()` za indeks+element, `zip()` za paralelne liste
