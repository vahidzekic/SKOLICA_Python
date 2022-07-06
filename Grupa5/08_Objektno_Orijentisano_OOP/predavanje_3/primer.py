#!/usr/bin/env python3
# Grupa5 / 08 / P3 â Enkapsulacija

class Liga:
    def __init__(self, naziv, sezona):
        self._naziv = naziv
        self._sezona = sezona
        self._timovi = []

    @property
    def naziv(self): return self._naziv

    @property
    def broj_timova(self): return len(self._timovi)

    def dodaj(self, tim):
        if tim not in self._timovi: self._timovi.append(tim)

    def __len__(self): return len(self._timovi)
    def __contains__(self, tim): return tim in self._timovi
    def __str__(self): return f"Liga '{self._naziv}' {self._sezona} ({self.broj_timova} timova)"
    def __iter__(self): return iter(self._timovi)

liga = Liga("SuperLiga", "2024/25")
liga.dodaj("Partizan")
liga.dodaj("Zvezda")
liga.dodaj("Vojvodina")
liga.dodaj("ÄukariÄki")

print(f"str: {liga}")
print(f"len: {len(liga)}")
print(f"'Zvezda' in: {'Zvezda' in liga}")
for t in liga: print(f"  {t}")