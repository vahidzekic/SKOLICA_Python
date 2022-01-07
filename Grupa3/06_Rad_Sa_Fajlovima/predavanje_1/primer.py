#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 06_Rad_Sa_Fajlovima / Predavanje 1
# Tema: Čitanje i pisanje tekstualnih fajlova
# =============================================================================
import os

os.makedirs("data", exist_ok=True)

# --- 1. PISANJE U FAJL ---
print("=== Pisanje u fajl ===")
with open("data/beleshke.txt", "w", encoding="utf-8") as f:
    f.write("ŠKOLICA Python — Beleške\n")
    f.write("=" * 30 + "\n\n")
    for i in range(1, 6):
        f.write(f"Lekcija {i}: Tema {i}\n")
print("✅ Fajl kreiran: data/beleshke.txt")

# --- 2. ČITANJE CELOG FAJLA ---
print("\n=== Čitanje celog fajla ===")
with open("data/beleshke.txt", "r", encoding="utf-8") as f:
    sadrzaj = f.read()
print(sadrzaj)

# --- 3. ČITANJE LINIJU PO LINIJU ---
print("=== Čitanje liniju po liniju ===")
with open("data/beleshke.txt", "r", encoding="utf-8") as f:
    for broj, linija in enumerate(f, 1):
        print(f"  [{broj}] {linija.rstrip()}")

# --- 4. DODAVANJE NA KRAJ (APPEND) ---
print("\n=== Append ===")
with open("data/beleshke.txt", "a", encoding="utf-8") as f:
    f.write("Lekcija 6: Rad sa fajlovima\n")
print("✅ Linija dodata na kraj fajla.")

# --- 5. BROJANJE REČI I LINIJA ---
print("\n=== Statistika fajla ===")
with open("data/beleshke.txt", "r", encoding="utf-8") as f:
    linije = f.readlines()

br_linija = len(linije)
br_reci = sum(len(l.split()) for l in linije)
br_karaktera = sum(len(l) for l in linije)
print(f"  Linija: {br_linija}")
print(f"  Reči: {br_reci}")
print(f"  Karaktera: {br_karaktera}")
