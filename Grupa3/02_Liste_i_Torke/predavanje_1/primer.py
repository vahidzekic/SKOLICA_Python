#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 02_Liste_i_Torke / Predavanje 1
# Tema: Kreiranje listi, indeksiranje, slicing, osnovne operacije
# =============================================================================

# --- 1. KREIRANJE LISTI ---
prazna = []
brojevi = [10, 20, 30, 40, 50]
imena = ["Vahid", "Kemo", "Omer", "Senaid"]
mesovita = ["tekst", 42, True, 3.14, None]

print("=== Kreiranje listi ===")
print("Prazna:", prazna)
print("Brojevi:", brojevi)
print("Imena:", imena)
print("Mešovita:", mesovita)
print(f"Dužina liste 'imena': {len(imena)}")
print("")

# --- 2. INDEKSIRANJE ---
print("=== Indeksiranje ===")
print(f"Prvi: imena[0] = '{imena[0]}'")
print(f"Poslednji: imena[-1] = '{imena[-1]}'")
print(f"Drugi: imena[1] = '{imena[1]}'")
print("")

# --- 3. SLICING ---
print("=== Slicing ===")
svi = ["a", "b", "c", "d", "e", "f", "g"]
print(f"Original: {svi}")
print(f"svi[1:4]  = {svi[1:4]}")
print(f"svi[:3]   = {svi[:3]}")
print(f"svi[4:]   = {svi[4:]}")
print(f"svi[::2]  = {svi[::2]}")
print(f"svi[::-1] = {svi[::-1]}")
print("")

# --- 4. DODAVANJE I BRISANJE ---
print("=== CRUD operacije ===")
lista = ["Python", "Java", "C++"]
print(f"Početna: {lista}")

lista.append("JavaScript")
print(f"append('JavaScript'): {lista}")

lista.insert(1, "Go")
print(f"insert(1, 'Go'): {lista}")

lista.remove("Java")
print(f"remove('Java'): {lista}")

izbacen = lista.pop(2)
print(f"pop(2) → '{izbacen}': {lista}")

# --- 5. OSTALE KORISNE METODE ---
print("\n=== Korisne metode ===")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Originalna: {nums}")
print(f"count(1): {nums.count(1)}")
print(f"index(5): {nums.index(5)}")
nums.sort()
print(f"sort(): {nums}")
nums.reverse()
print(f"reverse(): {nums}")
