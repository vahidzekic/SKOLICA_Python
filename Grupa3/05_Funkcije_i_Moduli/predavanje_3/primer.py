#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 05_Funkcije_i_Moduli / Predavanje 3
# Tema: Standardni moduli, kreiranje modula, __name__ == "__main__"
# =============================================================================

import math
import os
import random
import datetime

# --- 1. MATH MODUL ---
print("=== math modul ===")
print(f"Pi: {math.pi}")
print(f"sqrt(144): {math.sqrt(144)}")
print(f"pow(2, 10): {math.pow(2, 10)}")
print(f"ceil(4.3): {math.ceil(4.3)}")
print(f"floor(4.7): {math.floor(4.7)}")
print("")

# --- 2. RANDOM MODUL ---
print("=== random modul ===")
print(f"random(): {random.random():.4f}")
print(f"randint(1,100): {random.randint(1, 100)}")
imena = ["Vahid", "Enes", "Kemo", "Senaid"]
print(f"choice(): {random.choice(imena)}")
random.shuffle(imena)
print(f"shuffle(): {imena}")
print("")

# --- 3. OS MODUL ---
print("=== os modul ===")
print(f"Radni direktorijum: {os.getcwd()}")
print(f"Separator putanje: '{os.sep}'")
print("")

# --- 4. DATETIME MODUL ---
print("=== datetime modul ===")
sada = datetime.datetime.now()
print(f"Sada: {sada.strftime('%d.%m.%Y. %H:%M:%S')}")
print(f"Godina: {sada.year}, Mesec: {sada.month}, Dan: {sada.day}")
print("")

# --- 5. SOPSTVENI MODUL (simulacija) ---
print("=== Sopstveni modul (simulacija) ===")

# Ovo bi normalno bilo u zasebnom fajlu: modul_operacije.py
def modul_sabiranje(a, b):
    return a + b

def modul_oduzimanje(a, b):
    return a - b

# "Importovanje" i korišćenje
print(f"modul_sabiranje(10, 5) = {modul_sabiranje(10, 5)}")
print(f"modul_oduzimanje(10, 5) = {modul_oduzimanje(10, 5)}")

# --- 6. __name__ guard ---
def main():
    print("\n=== Ovaj kod se izvršava samo direktnim pokretanjem ===")
    print("Ako bi ovaj fajl bio importovan, main() se ne bi pozvao.")

if __name__ == "__main__":
    main()
