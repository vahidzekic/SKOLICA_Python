# Predavanje 1 — Uvod u Liste

## 1.1 Šta je lista?

Lista je **uređena, promenljiva** kolekcija elemenata. Elementi mogu biti različitih tipova.

```python
prazna = []
brojevi = [1, 2, 3, 4, 5]
mesovita = ["tekst", 42, True, 3.14]
```

## 1.2 Indeksiranje

| Indeks | Pozitivni | Negativni |
|---|---|---|
| Prvi element | `lista[0]` | `lista[-len(lista)]` |
| Poslednji | `lista[len-1]` | `lista[-1]` |
| Pretposlednji | `lista[len-2]` | `lista[-2]` |

## 1.3 Slicing (isecanje)

```python
lista = ["a", "b", "c", "d", "e", "f"]
lista[1:4]    # ["b", "c", "d"]  — od indeksa 1 do 3
lista[:3]     # ["a", "b", "c"]  — od početka do 2
lista[3:]     # ["d", "e", "f"]  — od indeksa 3 do kraja
lista[::2]    # ["a", "c", "e"]  — svaki drugi element
lista[::-1]   # obrnuta lista
```

## 1.4 Osnovne operacije

| Operacija | Metoda | Opis |
|---|---|---|
| Dodavanje | `lista.append(x)` | Dodaje na kraj |
| Umetanje | `lista.insert(i, x)` | Umeće na poziciju `i` |
| Brisanje | `lista.remove(x)` | Briše prvu pojavu `x` |
| Brisanje po indeksu | `lista.pop(i)` | Briše i vraća element |
| Dužina | `len(lista)` | Broj elemenata |

## Rezime
- Lista: `[]`, uređena, promenljiva, dozvoljava duplikate
- Indeksiranje od 0, negativni indeksi od kraja
- Slicing: `lista[start:stop:step]`
