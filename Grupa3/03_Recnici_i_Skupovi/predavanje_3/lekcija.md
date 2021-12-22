# Predavanje 3 — Dict Comprehension i Napredni Obrasci

## 3.1 Dict Comprehension

```python
kvadrati = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

filtriran = {k: v for k, v in recnik.items() if v > 10}
```

## 3.2 Ugnežđeni rečnici

```python
skola = {
    "Grupa1": {"polaznika": 12, "predavac": "Vahid"},
    "Grupa2": {"polaznika": 10, "predavac": "Enes"}
}
print(skola["Grupa1"]["predavac"])  # "Vahid"
```

## 3.3 defaultdict i Counter

```python
from collections import defaultdict, Counter

# defaultdict — automatski kreira podrazumevanu vrednost
dd = defaultdict(list)
dd["voce"].append("jabuka")

# Counter — broji pojave
tekst = "abracadabra"
brojac = Counter(tekst)  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

## Rezime
- Dict comprehension: `{k: v for k, v in ...}`
- Ugnežđeni rečnici za složene strukture
- `Counter` za brojanje pojava, `defaultdict` za auto-default
