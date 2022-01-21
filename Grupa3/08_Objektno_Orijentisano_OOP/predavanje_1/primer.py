#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 08_OOP / Predavanje 1
# Tema: Klase, konstruktor, metode, __str__
# =============================================================================

class Osoba:
    """Bazna klasa koja predstavlja osobu."""

    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def predstaviSe(self):
        return f"{self.ime} {self.prezime}, {self.godine} godina"

    def daLiJePunoletan(self):
        return self.godine >= 18

    def __str__(self):
        return self.predstaviSe()

# --- Kreiranje objekata ---
print("=== Kreiranje objekata ===")
osoba1 = Osoba("Vahid", "Zekic", 34)
osoba2 = Osoba("Kemo", "Plojovic", 27)

print(osoba1)
print(osoba2)
print(f"Punoletan: {osoba1.daLiJePunoletan()}")
print("")

# --- Iz JSON baze ---
print("=== Iz JSON baze ===")
baza = [
    {"ime": "Vahid", "prezime": "Zekic", "godine": 34},
    {"ime": "Enes", "prezime": "Daca", "godine": 32},
]
for podatak in baza:
    o = Osoba(podatak["ime"], podatak["prezime"], podatak["godine"])
    print(f"  {o}")
