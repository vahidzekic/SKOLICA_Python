#!/usr/bin/env python3
# Grupa7 / 11 / P1 â Model: Trip
import datetime

class Trip:
    def __init__(self, destinacija, km, cena, datum_polaska=""):
        self.destinacija = destinacija
        self.km = km
        self.cena = cena
        self.datum = datum_polaska or datetime.date.today().strftime("%d.%m.%Y")
        self.posecena = False

    def poseti(self): self.posecena = True

    def to_dict(self):
        return {"dest": self.destinacija, "km": self.km, "cena": self.cena,
                "datum": self.datum, "posecena": self.posecena}

    @classmethod
    def from_dict(cls, d):
        t = cls(d["dest"], d["km"], d["cena"], d["datum"])
        t.posecena = d["posecena"]
        return t

    def __str__(self):
        st = "Done" if self.posecena else "Plan"
        return f"[{st}] {self.destinacija} â {self.km}km, {self.cena}EUR ({self.datum})"

t1 = Trip("Istanbul", 594, 200)
t2 = Trip("Rim", 1060, 180)
t1.poseti()
print(t1)
print(t2)
print(f"Dict: {t1.to_dict()}")