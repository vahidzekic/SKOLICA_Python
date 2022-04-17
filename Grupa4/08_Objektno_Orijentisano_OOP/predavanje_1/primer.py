#!/usr/bin/env python3
# Grupa4 / 08 / P1 â Klase

class Automobil:
    def __init__(self, marka, model, godina, km=0):
        self.marka = marka
        self.model = model
        self.godina = godina
        self.km = km

    def vozi(self, d):
        self.km += d

    def __str__(self):
        return f"{self.marka} {self.model} ({self.godina}) â {self.km:,}km"

a1 = Automobil("BMW", "M8", 2020)
a2 = Automobil("Audi", "RS6", 2022, 15000)
a1.vozi(5000)
a1.vozi(3200)
print(a1)
print(a2)