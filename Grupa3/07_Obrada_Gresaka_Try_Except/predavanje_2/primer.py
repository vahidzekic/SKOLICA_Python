#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 07_Obrada_Gresaka_Try_Except / Predavanje 2
# Tema: raise, sopstveni izuzeci, assert
# =============================================================================

# --- 1. RAISE ---
print("=== raise ===")

def podeli(a, b):
    if b == 0:
        raise ValueError("Delilac ne sme biti nula!")
    return a / b

try:
    print(f"  10 / 3 = {podeli(10, 3):.2f}")
    print(f"  10 / 0 = {podeli(10, 0)}")
except ValueError as e:
    print(f"  ❌ Greška: {e}")
print("")

# --- 2. SOPSTVENI IZUZECI ---
print("=== Sopstveni izuzeci ===")

class NedovoljnoSredstava(Exception):
    def __init__(self, stanje, iznos):
        self.stanje = stanje
        self.iznos = iznos
        super().__init__(
            f"Nedovoljno sredstava! Stanje: {stanje}, traženo: {iznos}"
        )

class BankovniRacun:
    def __init__(self, vlasnik, stanje=0):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def podigni(self, iznos):
        if iznos > self.stanje:
            raise NedovoljnoSredstava(self.stanje, iznos)
        self.stanje -= iznos
        return self.stanje

racun = BankovniRacun("Vahid", 1000)
try:
    racun.podigni(500)
    print(f"  Stanje posle 500: {racun.stanje}")
    racun.podigni(800)
except NedovoljnoSredstava as e:
    print(f"  ❌ {e}")
print("")

# --- 3. ASSERT ---
print("=== assert ===")

def izracunaj_prosek(ocene):
    assert len(ocene) > 0, "Lista ocena ne sme biti prazna!"
    assert all(1 <= o <= 10 for o in ocene), "Ocene moraju biti 1-10!"
    return sum(ocene) / len(ocene)

try:
    print(f"  Prosek [8,9,7]: {izracunaj_prosek([8, 9, 7]):.2f}")
    print(f"  Prosek []: {izracunaj_prosek([])}")
except AssertionError as e:
    print(f"  ❌ Assert: {e}")
except Exception as e:
    print(f"  ❌ {type(e).__name__}: {e}")
