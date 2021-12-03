#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 01_Sintaksa_i_Promenljive / Predavanje 1
# Tema: Uvod u Python — prvi program, print(), komentari
# =============================================================================

# --- 1. PRVI PROGRAM ---
print("Zdravo, svete!")
print("Dobrodošli u ŠKOLICA Python kurs!")
print("")

# --- 2. FUNKCIJA print() SA RAZLICITIM ARGUMENTIMA ---
print("=== print() primeri ===")
print("Tekst:", "Ovo je string")
print("Broj:", 42)
print("Decimalni:", 3.14)
print("Boolean:", True)
print("")

# --- 3. print() SA SEPARATOROM I KRAJEM ---
# sep= menja separator između argumenata (default je razmak)
print("Jabuka", "Banana", "Višnja", sep=", ")
print("Jabuka", "Banana", "Višnja", sep=" | ")

# end= menja kraj linije (default je \n — novi red)
print("Ovo je", end=" ")
print("ista linija!")
print("")

# --- 4. VIŠELINIJSKI KOMENTAR ---
"""
Ovo je višelinijski komentar (docstring).
Koristi se za dokumentaciju funkcija i klasa,
ali može i kao obični komentar.
"""

# --- 5. SPECIJALNI KARAKTERI U STRINGOVIMA ---
print("=== Specijalni karakteri ===")
print("Novi red:\nDruga linija")
print("Tab:\tUvučen tekst")
print("Navodnici: \\\"unutar stringa\\\"")
print("Kosa crta: \\\\")
