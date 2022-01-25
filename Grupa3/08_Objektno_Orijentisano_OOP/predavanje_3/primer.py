#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 08_OOP / Predavanje 3
# Tema: Enkapsulacija, @property, specijalne metode
# =============================================================================

class Kurs:
    """Klasa sa enkapsulacijom, property-ima i dunder metodama."""

    def __init__(self, naziv, predavac, max_polaznika=20):
        self._naziv = naziv
        self._predavac = predavac
        self._max = max_polaznika
        self._polaznici = []

    @property
    def naziv(self):
        return self._naziv

    @property
    def popunjenost(self):
        return f"{len(self._polaznici)}/{self._max}"

    def upisi(self, ime):
        if len(self._polaznici) >= self._max:
            raise ValueError("Kurs je pun!")
        self._polaznici.append(ime)

    def __len__(self):
        return len(self._polaznici)

    def __str__(self):
        return f"Kurs '{self._naziv}' ({self.popunjenost})"

    def __repr__(self):
        return f"Kurs('{self._naziv}', '{self._predavac}', {self._max})"

    def __contains__(self, ime):
        return ime in self._polaznici

    def __eq__(self, other):
        return self._naziv == other._naziv

# --- Demonstracija ---
if __name__ == "__main__":
    python_kurs = Kurs("Python Osnove", "Vahid", max_polaznika=5)

    python_kurs.upisi("Enes")
    python_kurs.upisi("Kemo")
    python_kurs.upisi("Ahmed")

    print(f"str: {python_kurs}")
    print(f"repr: {repr(python_kurs)}")
    print(f"len: {len(python_kurs)}")
    print(f"'Enes' in kurs: {'Enes' in python_kurs}")
    print(f"Property naziv: {python_kurs.naziv}")
