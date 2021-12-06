#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 01_Sintaksa_i_Promenljive / Predavanje 2
# Tema: Promenljive, dodela vrednosti, type(), konverzija tipova
# =============================================================================

# --- 1. KREIRANJE PROMENLJIVIH ---
ime = "Vahid"
prezime = "Zekic"
godine = 34
visina = 1.82
aktivan = True

print("=== Promenljive ===")
print("Ime:", ime)
print("Prezime:", prezime)
print("Godine:", godine)
print("Visina:", visina)
print("Aktivan:", aktivan)
print("")

# --- 2. PROVERA TIPOVA SA type() ---
print("=== Tipovi podataka ===")
print(f"'{ime}' je tipa: {type(ime)}")
print(f"'{godine}' je tipa: {type(godine)}")
print(f"'{visina}' je tipa: {type(visina)}")
print(f"'{aktivan}' je tipa: {type(aktivan)}")
print("")

# --- 3. VIŠESTRUKA DODELA ---
print("=== Višestruka dodela ===")
x, y, z = "Crvena", "Zelena", "Plava"
print("Boje:", x, y, z)

a = b = c = 0
print("Nule:", a, b, c)
print("")

# --- 4. KONKATENACIJA STRINGOVA ---
print("=== Konkatenacija ===")
puno_ime = ime + " " + prezime
info = puno_ime + ", " + str(godine) + " godina"
print(info)

# f-string (preporučeni način od Python 3.6+)
info_fstring = f"{ime} {prezime}, {godine} godina, visina {visina}m"
print(info_fstring)
print("")

# --- 5. KONVERZIJA TIPOVA ---
print("=== Konverzija tipova ===")
tekst_broj = "42"
pravi_broj = int(tekst_broj)        # str → int
decimalni = float(tekst_broj)       # str → float
nazad_tekst = str(pravi_broj)       # int → str

print(f"str '{tekst_broj}' → int {pravi_broj} → float {decimalni}")
print(f"int {pravi_broj} → str '{nazad_tekst}'")
