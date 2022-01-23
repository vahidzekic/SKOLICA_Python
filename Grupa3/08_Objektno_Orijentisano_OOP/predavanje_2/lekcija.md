# Predavanje 2 — Nasleđivanje: Osoba → Radnik, Student

## 2.1 Nasleđivanje

Nasleđivanje omogućava kreiranje specijalizovanih klasa iz opštih.

```
        Osoba
       /     \\
   Radnik   Student
```

## 2.2 super()

`super()` poziva metodu roditeljske klase:

```python
class Radnik(Osoba):
    def __init__(self, ime, prezime, godine, firma, plata):
        super().__init__(ime, prezime, godine)
        self.firma = firma
        self.plata = plata
```

## 2.3 Polimorfizam

Ista metoda, različito ponašanje u različitim klasama:

```python
for osoba in [radnik, student]:
    print(osoba.predstaviSe())  # Svaka klasa ima svoju verziju
```

## Rezime
- `class Dete(Roditelj):` za nasleđivanje
- `super().__init__()` za poziv roditeljskog konstruktora
- Polimorfizam: ista metoda, drugačija implementacija
