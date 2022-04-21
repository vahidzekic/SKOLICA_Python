#!/usr/bin/env python3
# Grupa4 / 08 / P3 â Enkapsulacija, dunder

class Playlist:
    def __init__(self, naziv, vlasnik):
        self._naziv = naziv
        self._vlasnik = vlasnik
        self._pesme = []

    @property
    def naziv(self): return self._naziv

    @property
    def broj(self): return len(self._pesme)

    def dodaj(self, pesma):
        if pesma not in self._pesme:
            self._pesme.append(pesma)

    def __len__(self): return len(self._pesme)
    def __contains__(self, p): return p in self._pesme
    def __str__(self): return f"'{self._naziv}' ({self.broj} pesama)"
    def __iter__(self): return iter(self._pesme)

pl = Playlist("Coding Mix", "Vahid")
pl.dodaj("Daft Punk - Around The World")
pl.dodaj("M83 - Midnight City")
pl.dodaj("Kavinsky - Nightcall")

print(f"str: {pl}")
print(f"len: {len(pl)}")
print(f"Property: {pl.naziv}")
for p in pl:
    print(f"  {p}")