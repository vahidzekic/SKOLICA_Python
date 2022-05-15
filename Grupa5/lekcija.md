# Grupa 5 — Objektno-Orijentisano Programiranje (OOP)

## 5.1 Šta je OOP?

Objektno-orijentisano programiranje (OOP) je **paradigma programiranja** koja organizuje kod u **objekte** — strukture podataka koje kombinuju **podatke** (atribute) i **ponašanje** (metode).

### Četiri stuba OOP-a:

| Stub | Opis | Primer |
|---|---|---|
| **Enkapsulacija** | Sakrivanje unutrašnje implementacije | Privatni atributi (`_ime`) |
| **Apstrakcija** | Sakrivanje složenosti, pokazivanje suštine | Klasa `Osoba` sakriva interne detalje |
| **Nasleđivanje** | Kreiranje novih klasa iz postojećih | `Student` nasleđuje `Osoba` |
| **Polimorfizam** | Ista metoda, različito ponašanje | `predstaviSe()` radi drugačije za Radnika i Studenta |

---

## 5.2 Klase i objekti

**Klasa** je nacrt (blueprint) za kreiranje objekata. **Objekat** je konkretna instanca klase.

```python
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

# Kreiranje objekta (instanciranje)
osoba1 = Osoba("Vahid", "Zekic", 34)
```

### Anatomija klase:

| Element | Opis |
|---|---|
| `class ImeKlase:` | Deklaracija klase (Pascal case) |
| `__init__(self, ...)` | Konstruktor — poziva se pri kreiranju objekta |
| `self` | Referenca na trenutni objekat |
| `self.atribut` | Atribut (varijabla) objekta |
| `def metoda(self):` | Metoda (funkcija) objekta |

---

## 5.3 Metode klase

Metode su **funkcije definisane unutar klase** koje operišu nad atributima objekta:

```python
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def predstaviSe(self):
        return f"{self.ime} {self.prezime}, {self.godine} godina"

    def daLiJePunoletan(self):
        return self.godine >= 18
```

---

## 5.4 Nasleđivanje (Inheritance)

Nasleđivanje omogućava kreiranje **specijalizovanih klasa** iz opštih:

```
        ┌──────────┐
        │  Osoba   │   ← Roditeljska (bazna) klasa
        └────┬─────┘
             │
     ┌───────┴────────┐
     │                │
┌────┴─────┐   ┌──────┴─────┐
│  Radnik  │   │  Student   │  ← Dečije (izvedene) klase
└──────────┘   └────────────┘
```

```python
class Radnik(Osoba):             # Radnik nasleđuje Osoba
    def __init__(self, ime, prezime, godine, firma, plata):
        super().__init__(ime, prezime, godine)   # Poziv konstruktora roditelja
        self.firma = firma
        self.plata = plata

class Student(Osoba):            # Student nasleđuje Osoba
    def __init__(self, ime, prezime, godine, fakultet, smer):
        super().__init__(ime, prezime, godine)
        self.fakultet = fakultet
        self.smer = smer
```

### Ključna reč `super()`:
`super()` poziva metodu roditeljske klase. U konstruktoru, `super().__init__()` inicijalizuje atribute nasleđene od roditelja.

---

## 5.5 Polimorfizam (Polymorphism)

Polimorfizam znači da ista metoda može imati **različitu implementaciju** u različitim klasama:

```python
class Osoba:
    def predstaviSe(self):
        return f"{self.ime} {self.prezime}"

class Radnik(Osoba):
    def predstaviSe(self):        # Ista metoda, drugačija implementacija
        return f"{self.ime} {self.prezime} — {self.firma}"

class Student(Osoba):
    def predstaviSe(self):        # Ista metoda, opet drugačija
        return f"{self.ime} {self.prezime} — {self.fakultet}"
```

Kada pozovemo `predstaviSe()`, Python **automatski zna** koju verziju da koristi na osnovu tipa objekta.

---

## 5.6 Hijerarhija klasa u praksi

U kontekstu ŠKOLICA projekta, hijerarhija klasa je centralni koncept:

```
Osoba (ime, prezime, godine)
├── Radnik (+ firma, plata)
│     └── metode: predstaviSe(), izracunajPlatu()
└── Student (+ fakultet, smer)
      └── metode: predstaviSe(), statusStudenta()
```

> **Veza sa Knowledge Graph-om:** Čvor `Osobe` je **God Node** u ŠKOLICA grafu sa 3 veze — povezuje Python OOP sa Grupom 2 (tipovi podataka), Grupom 7 (REST API), i JavaScript objektima.

---

## 5.7 Instanciranje iz JSON baze

Klase se često koriste za konverziju sirovih JSON podataka u strukturirane objekte:

```python
osobeBaza = [
    {"ime": "Vahid", "prezime": "Zekic", "godine": 34},
    {"ime": "Enes", "prezime": "Daca", "godine": 32},
]

# Kreiranje objekata iz JSON-a
osobe = []
for podatak in osobeBaza:
    osoba = Osoba(podatak["ime"], podatak["prezime"], podatak["godine"])
    osobe.append(osoba)
```

---

## Rezime Grupe 5

| Koncept | Opis |
|---|---|
| `class` | Nacrt za kreiranje objekata |
| `__init__` | Konstruktor klase |
| `self` | Referenca na trenutni objekat |
| Nasleđivanje | `class Dete(Roditelj):` |
| `super()` | Poziv metode roditeljske klase |
| Polimorfizam | Ista metoda, različito ponašanje |
