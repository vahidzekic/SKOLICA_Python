#!/usr/bin/env python3
# Grupa4 / 11 / P1 â Model: Zadatak
import datetime

class Zadatak:
    def __init__(self, naslov, prioritet="srednji"):
        self.naslov = naslov
        self.prioritet = prioritet
        self.zavrsen = False
        self.kreiran = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    def zavrsi(self): self.zavrsen = True

    def to_dict(self):
        return {"naslov": self.naslov, "prioritet": self.prioritet,
                "zavrsen": self.zavrsen, "kreiran": self.kreiran}

    @classmethod
    def from_dict(cls, d):
        z = cls(d["naslov"], d["prioritet"])
        z.zavrsen = d["zavrsen"]
        z.kreiran = d["kreiran"]
        return z

    def __str__(self):
        st = "DONE" if self.zavrsen else "TODO"
        return f"[{st}] {self.naslov} ({self.prioritet})"

z1 = Zadatak("NauÄiti OOP", "visok")
z2 = Zadatak("Kupiti mleko", "nizak")
z1.zavrsi()
print(z1)
print(z2)
print(f"Dict: {z1.to_dict()}")