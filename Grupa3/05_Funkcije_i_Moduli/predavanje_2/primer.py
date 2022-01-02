#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 05_Funkcije_i_Moduli / Predavanje 2
# Tema: Lambda, map, filter, sorted sa key, dekoratori
# =============================================================================

# --- 1. LAMBDA FUNKCIJE ---
print("=== Lambda ===")
kvadrat = lambda x: x ** 2
saberi = lambda a, b: a + b

print(f"kvadrat(7) = {kvadrat(7)}")
print(f"saberi(10, 20) = {saberi(10, 20)}")
print("")

# --- 2. MAP ---
print("=== map() ===")
brojevi = [1, 2, 3, 4, 5, 6, 7, 8]
kvadrati = list(map(lambda x: x ** 2, brojevi))
print(f"Originalni: {brojevi}")
print(f"Kvadrati: {kvadrati}")
print("")

# --- 3. FILTER ---
print("=== filter() ===")
parni = list(filter(lambda x: x % 2 == 0, brojevi))
veci_od_4 = list(filter(lambda x: x > 4, brojevi))
print(f"Parni: {parni}")
print(f"Veći od 4: {veci_od_4}")
print("")

# --- 4. SORTED SA KEY ---
print("=== sorted() sa key ===")
studenti = [
    {"ime": "Vahid", "prosek": 9.2},
    {"ime": "Enes", "prosek": 8.1},
    {"ime": "Kemo", "prosek": 9.5},
    {"ime": "Senaid", "prosek": 7.8}
]

po_proseku = sorted(studenti, key=lambda s: s["prosek"], reverse=True)
for s in po_proseku:
    print(f"  {s['ime']}: {s['prosek']}")
print("")

# --- 5. DEKORATOR ---
print("=== Dekorator ===")

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        kraj = time.time()
        print(f"  ⏱ {func.__name__} izvršena za {kraj - start:.6f}s")
        return rezultat
    return wrapper

@timer
def spora_operacija():
    total = sum(range(1_000_000))
    return total

rezultat = spora_operacija()
print(f"  Rezultat: {rezultat:,}")
