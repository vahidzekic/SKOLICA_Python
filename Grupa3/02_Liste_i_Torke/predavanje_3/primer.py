#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 02_Liste_i_Torke / Predavanje 3
# Tema: Torke — kreiranje, unpacking, razlike sa listama
# =============================================================================

# --- 1. KREIRANJE TORKI ---
print("=== Kreiranje torki ===")
prazna = ()
jednoclana = (42,)             # ZAREZ je obavezan!
koordinate = (45.33, 20.46)
boja_rgb = (255, 128, 0)
mesovita = ("Vahid", 34, True, 1.82)

print(f"Prazna: {prazna}")
print(f"Jednočlana: {jednoclana} (tip: {type(jednoclana)})")
print(f"Koordinate: {koordinate}")
print(f"RGB boja: {boja_rgb}")
print("")

# --- 2. INDEKSIRANJE I SLICING (isto kao lista) ---
print("=== Indeksiranje ===")
dani = ("Pon", "Uto", "Sre", "Čet", "Pet", "Sub", "Ned")
print(f"Prvi dan: {dani[0]}")
print(f"Vikend: {dani[5:]}")
print(f"Radni dani: {dani[:5]}")
print("")

# --- 3. UNPACKING ---
print("=== Unpacking ===")
lat, lon = koordinate
print(f"Latitude: {lat}, Longitude: {lon}")

ime, godine, aktivan, visina = mesovita
print(f"Ime: {ime}, godine: {godine}, visina: {visina}")

# Sa * operatorom
prva, *srednje, poslednja = dani
print(f"Prva: {prva}, Poslednja: {poslednja}")
print(f"Srednje: {srednje}")
print("")

# --- 4. TORKA KAO RETURN VREDNOST FUNKCIJE ---
print("=== Funkcija koja vraća torku ===")

def statistika(brojevi):
    """Vraća (min, max, prosek) kao torku."""
    return (min(brojevi), max(brojevi), sum(brojevi) / len(brojevi))

ocene = [7, 8, 9, 6, 10, 8, 9]
najm, najv, prosek = statistika(ocene)
print(f"Ocene: {ocene}")
print(f"Min: {najm}, Max: {najv}, Prosek: {prosek:.2f}")
print("")

# --- 5. LISTA VS TORKA — PERFORMANSE ---
import sys
lista = [1, 2, 3, 4, 5]
torka = (1, 2, 3, 4, 5)
print("=== Memorija: Lista vs Torka ===")
print(f"Lista {lista}: {sys.getsizeof(lista)} bajtova")
print(f"Torka {torka}: {sys.getsizeof(torka)} bajtova")
