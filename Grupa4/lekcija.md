# Grupa 4 — Petlje (Loops) i Iteracija

## 4.1 Šta su petlje?

Petlje su kontrolne strukture koje omogućavaju **ponavljanje bloka koda** dok je određeni uslov ispunjen. Bez petlji, morali bismo ručno ponavljati isti kod — što je nepraktično i podložno greškama.

Python podržava dve osnovne petlje:
1. **`for`** — iterira kroz sekvencu (listu, string, range...)
2. **`while`** — ponavlja dok je uslov `True`

---

## 4.2 FOR petlja

FOR petlja je **iteracijska petlja** — prolazi kroz svaki element sekvence, jedan po jedan.

### Osnovna sintaksa:
```python
for element in sekvenca:
    # Kod koji se ponavlja za svaki element
    print(element)
```

### Primeri sekvenci za iteraciju:

```python
# Iteracija kroz listu
niz = ["Vahid", "Omer", "Moke", "Muhamed"]
for clan in niz:
    print(clan)

# Iteracija kroz string
for slovo in "Python":
    print(slovo)

# Iteracija kroz range()
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):    # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 20, 5): # 0, 5, 10, 15
    print(i)
```

### Funkcija `range()`:

| Sintaksa | Rezultat | Opis |
|---|---|---|
| `range(5)` | `0, 1, 2, 3, 4` | Od 0 do 4 |
| `range(2, 8)` | `2, 3, 4, 5, 6, 7` | Od 2 do 7 |
| `range(0, 20, 5)` | `0, 5, 10, 15` | Korak 5 |
| `range(10, 0, -1)` | `10, 9, 8, ..., 1` | Obrnuto brojanje |

---

## 4.3 FOR petlja sa JSON objektima

Jedna od najčešćih upotreba `for` petlje je iteriranje kroz JSON podatke (lista rečnika):

```python
studenti = [
    {"ime": "Vahid", "prezime": "Zekic", "godina": 1986},
    {"ime": "Enes", "prezime": "Daca", "godina": 1988},
]

for student in studenti:
    print(student["ime"] + " " + student["prezime"])
```

Alternativno sa `range()` i `len()`:
```python
for i in range(len(studenti)):
    print(studenti[i]["ime"])
```

---

## 4.4 WHILE petlja

WHILE petlja ponavlja blok koda **dok god je uslov True**:

```python
i = 0
while i < 10:
    print(i)
    i += 1      # KRITIČNO: bez ove linije, petlja je beskonačna!
```

> **Upozorenje:** WHILE petlja zahteva ručno ažuriranje brojača. Ako zaboravite `i += 1`, dobijate **beskonačnu petlju** koja blokira program.

### WHILE...ELSE:
Python podržava `else` blok nakon `while` — izvršava se kad se petlja normalno završi:

```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Petlja je završena.")
```

---

## 4.5 Kada koristiti FOR, a kada WHILE?

| Situacija | Petlja | Razlog |
|---|---|---|
| Iteracija kroz listu/rečnik | `for` | Poznat broj elemenata |
| Čitanje JSON podataka | `for` | Sekvencijalan pristup |
| Glavni program loop | `while` | Nepoznat broj iteracija |
| Čekanje korisničkog unosa | `while` | Ponavlja dok korisnik ne prekine |
| Mrežne konekcije | `while` | Čeka odgovor servera |

---

## 4.6 Kontrola toka petlji

| Naredba | Opis |
|---|---|
| `break` | Prekida petlju potpuno |
| `continue` | Preskače ostatak iteracije, prelazi na sledeću |
| `pass` | Ne radi ništa (placeholder) |

```python
for i in range(10):
    if i == 3:
        continue    # Preskače 3
    if i == 7:
        break       # Prekida na 7
    print(i)        # Ispisuje: 0, 1, 2, 4, 5, 6
```

---

## 4.7 Liste i petlje — CRUD operacije

Kombinacija listi i petlji je osnova za upravljanje podacima:

```python
lista = []

# CREATE — korisnički unos
for i in range(3):
    unos = input(f"Unesite clan {i+1}: ")
    lista.append(unos)

# READ — ispis svih elemenata
for clan in lista:
    print(clan)

# DELETE — brisanje po vrednosti
brisanje = input("Unesite clan za brisanje: ")
lista.remove(brisanje)
```

---

## Rezime Grupe 4

| Petlja | Upotreba | Opasnost |
|---|---|---|
| `for...in` | Poznati opseg, liste, JSON | Nema |
| `while` | Nepoznat broj iteracija | Beskonačna petlja |
| `break` | Prekid petlje | — |
| `continue` | Preskakanje iteracije | — |
