# Grupa 2 — Tipovi Podataka u Python-u

## 2.1 Uvod u tipove podataka

Svaka vrednost u Python-u ima **tip** (eng. *data type*) koji određuje kakve operacije možemo izvršiti nad tom vrednošću. Python automatski prepoznaje tip na osnovu dodeljene vrednosti — ovo se naziva **dinamičko tipiziranje**.

### Osnovni tipovi:

| Tip | Python klasa | Primer | Opis |
|---|---|---|---|
| Ceo broj | `int` | `42` | Pozitivni i negativni celi brojevi |
| Decimalni broj | `float` | `3.14` | Brojevi sa decimalnim zarezom |
| Tekst | `str` | `"Zdravo"` | Niz karaktera (string) |
| Logička vrednost | `bool` | `True` / `False` | Samo dve moguće vrednosti |

---

## 2.2 Liste (list)

Lista je **uređena**, **promenljiva** kolekcija elemenata. Elementi mogu biti različitih tipova.

```python
mojaLista = ["Vahid", "Kemo", "Omer"]
mesovitaLista = ["tekst", 42, True, 3.14]
```

### Operacije sa listama:

| Operacija | Sintaksa | Opis |
|---|---|---|
| Dodavanje | `lista.append(x)` | Dodaje `x` na kraj liste |
| Umetanje | `lista.insert(i, x)` | Umeće `x` na poziciju `i` |
| Brisanje po vrednosti | `lista.remove(x)` | Briše prvi `x` iz liste |
| Brisanje po poziciji | `lista.pop(i)` | Briše element na poziciji `i` |
| Brisanje ključnom rečju | `del lista[i]` | Briše element na poziciji `i` |
| Čišćenje | `lista.clear()` | Briše sve elemente |
| Dužina | `len(lista)` | Vraća broj elemenata |

### Slicing (isecanje):
```python
lista = ["prvi", "drugi", "treci", "cetvrti", "peti"]
print(lista[1:4])   # ["drugi", "treci", "cetvrti"]
print(lista[:3])     # ["prvi", "drugi", "treci"]
print(lista[2:])     # ["treci", "cetvrti", "peti"]
```

---

## 2.3 Tuple (torka)

Tuple je **uređena**, ali **nepromenljiva** kolekcija. Jednom kreiran, ne možete menjati, dodavati ili brisati elemente.

```python
mojTuple = (1, 2, 3)
mojTuple = tuple(["a", "b", "c"])  # Kreiranje od liste
```

> **Kada koristiti tuple umesto liste?** Kada želite da obezbedite da se podaci ne mogu slučajno promeniti (npr. koordinate, konfiguracioni podaci).

---

## 2.4 Set (skup)

Set je **neuređena** kolekcija **jedinstvenih** elemenata. Automatski uklanja duplikate.

```python
mojSet = {1, 2, 2, 3, 3, 3}
print(mojSet)  # {1, 2, 3} — duplikati su uklonjeni
```

### Ključna osobina:
Setovi ne podržavaju indeksiranje (`mojSet[0]` neće raditi) jer nemaju definisan redosled.

---

## 2.5 Dictionary (rečnik)

Rečnik čuva podatke u **ključ-vrednost** parovima. Ovo je Python-ova implementacija **hash mape**.

```python
auto = {
    "marka": "BMW",
    "model": "M8",
    "boja": "Crvena",
    "godina": 2020
}
```

### Operacije sa rečnicima:

| Operacija | Sintaksa |
|---|---|
| Čitanje vrednosti | `auto["marka"]` |
| Izmena vrednosti | `auto["marka"] = "Audi"` |
| Dodavanje para | `auto["sedista"] = 5` |
| Ažuriranje | `auto.update({"godina": 2021})` |
| Brisanje | `del auto["boja"]` |

---

## 2.6 JSON Objekti u Python-u

JSON (JavaScript Object Notation) je format za razmenu podataka. U Python-u, JSON se mapira na **listu rečnika**:

```python
studenti = [
    {"id": 1, "ime": "Vahid", "prezime": "Zekic", "godine": 34},
    {"id": 2, "ime": "Omer", "prezime": "Ljajic", "godine": 34},
]
```

Pristupamo vrednosti dvostrukim indeksiranjem:
```python
print(studenti[0]["ime"])  # "Vahid"
```

---

## Rezime Grupe 2

| Tip | Uređen | Promenljiv | Duplikati | Sintaksa |
|---|---|---|---|---|
| `list` | ✅ Da | ✅ Da | ✅ Da | `[1, 2, 3]` |
| `tuple` | ✅ Da | ❌ Ne | ✅ Da | `(1, 2, 3)` |
| `set` | ❌ Ne | ✅ Da | ❌ Ne | `{1, 2, 3}` |
| `dict` | ✅ Da* | ✅ Da | ❌ Ključevi | `{"k": "v"}` |

> *Od Python 3.7+, rečnici čuvaju redosled umetanja.
