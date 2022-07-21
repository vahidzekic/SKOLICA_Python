#!/usr/bin/env python3
# Grupa5 / 11 / P1 â Model: Trosak
import datetime

class Trosak:
    def __init__(self, iznos, kategorija, opis=""):
        self.iznos = iznos
        self.kategorija = kategorija
        self.opis = opis
        self.datum = datetime.datetime.now().strftime("%d.%m.%Y")

    def to_dict(self):
        return {"iznos": self.iznos, "kategorija": self.kategorija,
                "opis": self.opis, "datum": self.datum}

    @classmethod
    def from_dict(cls, d):
        t = cls(d["iznos"], d["kategorija"], d["opis"])
        t.datum = d["datum"]
        return t

    def __str__(self):
        return f"{self.datum} | {self.kategorija:12} | {self.iznos:>8.2f} RSD | {self.opis}"

t1 = Trosak(350, "Hrana", "RuÄak")
t2 = Trosak(1500, "Transport", "Gorivo")
print(t1)
print(t2)
print(f"Dict: {t1.to_dict()}")