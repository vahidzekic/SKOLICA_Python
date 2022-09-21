#!/usr/bin/env python3
# Grupa6 / 08 / P3 â Enkapsulacija

class MuzickaBiblioteka:
    def __init__(self, naziv):
        self._naziv = naziv
        self._albumi = []

    @property
    def naziv(self): return self._naziv

    @property
    def broj(self): return len(self._albumi)

    def dodaj(self, album):
        if album not in self._albumi: self._albumi.append(album)

    def __len__(self): return len(self._albumi)
    def __contains__(self, a): return a in self._albumi
    def __str__(self): return f"'{self._naziv}' ({self.broj} albuma)"
    def __iter__(self): return iter(self._albumi)

bib = MuzickaBiblioteka("Moja Kolekcija")
bib.dodaj("Abbey Road")
bib.dodaj("Dark Side of the Moon")
bib.dodaj("Thriller")
bib.dodaj("OK Computer")

print(f"str: {bib}")
print(f"len: {len(bib)}")
print(f"'Thriller' in: {'Thriller' in bib}")
for a in bib: print(f"  {a}")