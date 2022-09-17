#!/usr/bin/env python3
# Grupa6 / 08 / P1 â Klase

class Album:
    def __init__(self, naziv, bend, godina, pesama=0):
        self.naziv = naziv
        self.bend = bend
        self.godina = godina
        self.pesama = pesama
        self.ocena = 0.0

    def oceni(self, ocena):
        self.ocena = ocena

    def starost(self):
        return 2025 - self.godina

    def __str__(self):
        return f"{self.naziv} â {self.bend} ({self.godina}) [{self.ocena}/10]"

a1 = Album("Abbey Road", "Beatles", 1969, 17)
a2 = Album("Dark Side", "Pink Floyd", 1973, 10)
a1.oceni(9.8)
a2.oceni(9.9)
print(a1)
print(a2)
print(f"Starost '{a1.naziv}': {a1.starost()} god.")