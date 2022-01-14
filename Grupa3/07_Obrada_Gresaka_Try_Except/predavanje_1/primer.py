#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 07_Obrada_Gresaka_Try_Except / Predavanje 1
# Tema: try/except osnove, tipovi grešaka, else/finally
# =============================================================================

# --- 1. OSNOVNO try/except ---
print("=== Deljenje nulom ===")
try:
    rezultat = 10 / 0
except ZeroDivisionError:
    print("  Greška: Deljenje nulom nije moguće!")

# --- 2. ValueError ---
print("\n=== ValueError ===")
try:
    broj = int("abc")
except ValueError as e:
    print(f"  Greška: {e}")

# --- 3. VIŠE EXCEPT BLOKOVA ---
print("\n=== Više except blokova ===")
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("  Greška: Indeks van opsega!")
except TypeError:
    print("  Greška: Pogrešan tip!")

# --- 4. TRY/EXCEPT/ELSE/FINALLY ---
print("\n=== Try/Except/Else/Finally ===")
try:
    x = int(input("  Unesite broj: "))
    rezultat = 100 / x
except ValueError:
    print("  ❌ To nije validan broj!")
except ZeroDivisionError:
    print("  ❌ Ne može se deliti nulom!")
else:
    print(f"  ✅ Rezultat: 100 / {x} = {rezultat:.2f}")
finally:
    print("  ℹ️ Ovaj blok se izvršava UVEK.")

# --- 5. OBRADA FAJL GREŠAKA ---
print("\n=== FileNotFoundError ===")
try:
    with open("nepostojeci_fajl.txt", "r") as f:
        sadrzaj = f.read()
except FileNotFoundError:
    print("  Greška: Fajl ne postoji!")
