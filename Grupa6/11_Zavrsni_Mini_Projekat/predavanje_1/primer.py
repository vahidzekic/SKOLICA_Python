#!/usr/bin/env python3
# Grupa6 / 11 / P1 â Model: Pitanje

class Pitanje:
    def __init__(self, tekst, opcije, tacan, kategorija="OpÅ¡te"):
        self.tekst = tekst
        self.opcije = opcije
        self.tacan = tacan  # indeks taÄnog odgovora
        self.kategorija = kategorija

    def proveri(self, odgovor):
        return odgovor == self.tacan

    def to_dict(self):
        return {"tekst": self.tekst, "opcije": self.opcije,
                "tacan": self.tacan, "kategorija": self.kategorija}

    @classmethod
    def from_dict(cls, d):
        return cls(d["tekst"], d["opcije"], d["tacan"], d.get("kategorija", "OpÅ¡te"))

    def __str__(self):
        opts = "\n".join(f"  {chr(65+i)}. {o}" for i, o in enumerate(self.opcije))
        return f"{self.tekst}\n{opts}"

p = Pitanje("Koji bend je napisao 'Bohemian Rhapsody'?", ["Beatles", "Queen", "Led Zeppelin", "Pink Floyd"], 1, "Muzika")
print(p)
print(f"\nOdgovor B taÄan: {p.proveri(1)}")
print(f"Odgovor A taÄan: {p.proveri(0)}")