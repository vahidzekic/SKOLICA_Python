# Predavanje 2 — Napredne Operacije sa Listama

## 2.1 Iteracija kroz listu

```python
# For petlja — najčešći način
for element in lista:
    print(element)

# Sa indeksom — enumerate()
for indeks, element in enumerate(lista):
    print(f"[{indeks}] {element}")
```

## 2.2 List Comprehension

Kompaktan način za kreiranje listi:

```python
# Umesto:
kvadrati = []
for x in range(10):
    kvadrati.append(x ** 2)

# Možemo:
kvadrati = [x ** 2 for x in range(10)]

# Sa uslovom:
parni = [x for x in range(20) if x % 2 == 0]
```

## 2.3 Ugnežđene liste (2D liste)

```python
matrica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrica[1][2])  # 6 — drugi red, treća kolona
```

## 2.4 Kopiranje listi

```python
original = [1, 2, 3]
referenca = original         # NIJE kopija! Ista memorija
kopija = original.copy()     # Prava kopija (shallow)
kopija2 = original[:]        # Slicing kopija
kopija3 = list(original)     # Konstruktor kopija
```

## Rezime
- `enumerate()` za indeks + element
- List comprehension: `[izraz for x in sekvenca if uslov]`
- `.copy()` za pravu kopiju, `=` samo kreira referencu
