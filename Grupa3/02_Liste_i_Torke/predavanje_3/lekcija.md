# Predavanje 3 — Torke (Tuples)

## 3.1 Šta je torka?

Torka (tuple) je **uređena, NEPROMENLJIVA** kolekcija. Jednom kreirana, ne može se menjati.

```python
prazna = ()
jednočlana = (42,)           # Zarez je obavezan za jednočlanu!
koordinate = (45.33, 20.46)
mesovita = ("tekst", 42, True)
```

## 3.2 Razlike Lista vs Torka

| Osobina | Lista `[]` | Torka `()` |
|---|---|---|
| Promenljiva | ✅ Da | ❌ Ne |
| Brzina | Sporija | Brža |
| Memorija | Više | Manje |
| Hashable | ❌ Ne | ✅ Da (može biti dict ključ) |
| Upotreba | Kolekcije koje se menjaju | Fiksni podaci |

## 3.3 Unpacking (raspakivanje)

```python
koordinate = (45.33, 20.46, 512)
lat, lon, alt = koordinate     # Raspakovano u 3 varijable

# Sa * za ostatak
prva, *ostale = (1, 2, 3, 4, 5)
# prva = 1, ostale = [2, 3, 4, 5]
```

## 3.4 Kada koristiti torke?

- Koordinate: `(lat, lon)`
- RGB boje: `(255, 128, 0)`
- Funkcije koje vraćaju više vrednosti: `return (min, max, avg)`
- Ključevi rečnika: `dict[(x, y)] = vrednost`

## Rezime
- Torka: `()`, uređena, nepromenljiva
- Brža i memorijski efikasnija od liste
- Unpacking: `a, b, c = torka`
- Koristiti za fiksne podatke koji se ne menjaju
