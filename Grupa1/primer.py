#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 1: Osnove Python Programskog Jezika
# Autor: dipl.inz. Vahid Zekic
# Opis: Demonstracija varijabli, aritmetičkih operacija, print/input funkcija
# =============================================================================


# -----------------------------------------------------------------------------
# 1. PRVI PROGRAM — "Zdravo, svete!"
# -----------------------------------------------------------------------------
print("Zdravo, svete!!!")
print("")  # Prazan red za vizuelno razdvajanje


# -----------------------------------------------------------------------------
# 2. VARIJABLE I DODELA VREDNOSTI
# -----------------------------------------------------------------------------

# Definišemo dve celobrojne varijable
prviBroj = 11
drugiBroj = 7

# Višestruka dodela — Python dozvoljava dodelu u jednoj liniji
x, y, z = "Crvena", "Zelena", "Plava"
print("Boje:", x, y, z)

# Redodela istih varijabli sa brojevima
x, y, z = 1, 2, 3
print("Brojevi:", x, y, z)
print("")


# -----------------------------------------------------------------------------
# 3. ARITMETIČKE OPERACIJE
# -----------------------------------------------------------------------------

sabiranje = prviBroj + drugiBroj           # 11 + 7 = 18
oduzimanje = prviBroj - drugiBroj          # 11 - 7 = 4
mnozenje = prviBroj * drugiBroj            # 11 * 7 = 77
deljenje = prviBroj / drugiBroj            # 11 / 7 = 1.571...
celobrojno_deljenje = prviBroj // drugiBroj # 11 // 7 = 1
ostatak_deljenja = prviBroj % drugiBroj    # 11 % 7 = 4
stepenovanje = prviBroj ** drugiBroj       # 11^7 = 19487171

# Ispis svih rezultata sa objašnjenjima
print("=== Aritmetičke operacije sa brojevima", prviBroj, "i", drugiBroj, "===")
print("Sabiranje:          ", sabiranje)
print("Oduzimanje:         ", oduzimanje)
print("Množenje:           ", mnozenje)
print("Deljenje:           ", deljenje)
print("Celobrojno deljenje:", celobrojno_deljenje)
print("Ostatak deljenja:   ", ostatak_deljenja)
print("Stepenovanje:       ", stepenovanje)
print("")


# -----------------------------------------------------------------------------
# 4. KONKATENACIJA STRINGOVA SA str() KONVERZIJOM
# -----------------------------------------------------------------------------

ime = "Vahid"
prezime = "Zekic"
godine = 34

# Za spajanje stringa sa brojem, koristimo str() da konvertujemo broj u tekst
informacija = "Ime: " + ime + " " + prezime + ", godine: " + str(godine)
print(informacija)
print("")


# -----------------------------------------------------------------------------
# 5. KORISNIČKI UNOS — input() funkcija
# -----------------------------------------------------------------------------

# input() uvek vraća STRING, pa za matematiku moramo konvertovati u int/float
print("=== Kalkulator sabiranja ===")
prvi = int(input("Unesite prvi broj: "))
drugi = int(input("Unesite drugi broj: "))

rezultat = prvi + drugi
print("Rezultat sabiranja: " + str(prvi) + " + " + str(drugi) + " = " + str(rezultat))
print("")


# -----------------------------------------------------------------------------
# 6. PROVERA TIPOVA PODATAKA — type() funkcija
# -----------------------------------------------------------------------------

print("=== Tipovi podataka ===")
print("Tip varijable 'ime':", type(ime))           # <class 'str'>
print("Tip varijable 'godine':", type(godine))      # <class 'int'>
print("Tip varijable 'deljenje':", type(deljenje))   # <class 'float'>
print("Tip varijable True:", type(True))             # <class 'bool'>
