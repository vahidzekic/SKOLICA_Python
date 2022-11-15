#!/usr/bin/env python3
# Grupa7 / 08 / P1 â Klase

class Destinacija:
    def __init__(self, grad, drzava, km, cena_eur=0):
        self.grad = grad
        self.drzava = drzava
        self.km = km
        self.cena = cena_eur
        self.posecena = False

    def poseti(self):
        self.posecena = True

    def cena_po_km(self):
        return round(self.cena / self.km, 3) if self.km else 0

    def __str__(self):
        st = "â" if self.posecena else "â¬"
        return f"{st} {self.grad} ({self.drzava}) â {self.km}km, {self.cena}EUR"

d1 = Destinacija("Istanbul", "Turska", 594, 200)
d2 = Destinacija("Rim", "Italija", 1060, 180)
d1.poseti()
print(d1)
print(d2)
print(f"Cena/km: {d1.cena_po_km()} EUR")