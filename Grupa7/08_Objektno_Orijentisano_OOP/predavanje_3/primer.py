#!/usr/bin/env python3
# Grupa7 / 08 / P3 â Enkapsulacija

class TravelPlan:
    def __init__(self, naziv, autor):
        self._naziv = naziv
        self._autor = autor
        self._destinacije = []

    @property
    def naziv(self): return self._naziv

    @property
    def ukupno_km(self):
        return sum(d[1] for d in self._destinacije)

    def dodaj(self, grad, km):
        self._destinacije.append((grad, km))

    def __len__(self): return len(self._destinacije)
    def __contains__(self, grad): return any(d[0] == grad for d in self._destinacije)
    def __str__(self): return f"'{self._naziv}' ({len(self)} dest, {self.ukupno_km}km)"
    def __iter__(self): return iter(self._destinacije)

plan = TravelPlan("Balkan Tour", "Vahid")
plan.dodaj("Istanbul", 594)
plan.dodaj("Atina", 1100)
plan.dodaj("Rim", 1060)
plan.dodaj("BeÄ", 600)

print(f"str: {plan}")
print(f"len: {len(plan)}")
print(f"Ukupno km: {plan.ukupno_km}")
print(f"'Istanbul' in: {'Istanbul' in plan}")
for g, km in plan: print(f"  {g}: {km}km")