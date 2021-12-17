#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 03_Recnici_i_Skupovi / Predavanje 1
# Tema: Rečnici — kreiranje, CRUD, metode, iteracija
# =============================================================================

# --- 1. KREIRANJE REČNIKA ---
auto = {
    "marka": "BMW",
    "model": "M8",
    "boja": "Crvena",
    "godina": 2020,
    "sedista": 5
}

print("=== Rečnik 'auto' ===")
for kljuc, vrednost in auto.items():
    print(f"  {kljuc}: {vrednost}")
print("")

# --- 2. ČITANJE VREDNOSTI ---
print("=== Čitanje ===")
print(f"Marka: {auto['marka']}")
print(f"Boja (get): {auto.get('boja', 'Nepoznata')}")
print(f"Klima (get): {auto.get('klima', 'Nema podatka')}")  # Bezbedno
print("")

# --- 3. CRUD OPERACIJE ---
print("=== CRUD ===")
auto["marka"] = "Audi"              # UPDATE
auto["klima"] = True                 # CREATE
del auto["sedista"]                  # DELETE
print("Ažuriran:", auto)
print("")

# --- 4. ITERACIJA ---
print("=== Iteracija ===")
print("Ključevi:", list(auto.keys()))
print("Vrednosti:", list(auto.values()))
print("Parovi:")
for k, v in auto.items():
    print(f"  {k} → {v}")
print("")

# --- 5. LISTA REČNIKA (JSON STRUKTURA) ---
print("=== Lista rečnika (JSON) ===")
studenti = [
    {"id": 1, "ime": "Vahid", "prezime": "Zekic", "godine": 34},
    {"id": 2, "ime": "Enes", "prezime": "Daca", "godine": 32},
    {"id": 3, "ime": "Senaid", "prezime": "Sarenkapic", "godine": 32}
]

for s in studenti:
    print(f"  [{s['id']}] {s['ime']} {s['prezime']}, {s['godine']} god.")
