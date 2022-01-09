#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 06_Rad_Sa_Fajlovima / Predavanje 2
# Tema: JSON — čitanje, pisanje, CRUD sa persistencijom
# =============================================================================
import json
import os

os.makedirs("data", exist_ok=True)
JSON_PATH = "data/studenti.json"

# --- 1. KREIRANJE I PISANJE JSON ---
print("=== Pisanje JSON ===")
studenti = [
    {"id": 1, "ime": "Vahid", "prezime": "Zekic", "godine": 34},
    {"id": 2, "ime": "Enes", "prezime": "Daca", "godine": 32},
    {"id": 3, "ime": "Senaid", "prezime": "Sarenkapic", "godine": 32}
]

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(studenti, f, indent=4, ensure_ascii=False)
print(f"✅ Zapisano {len(studenti)} studenata u {JSON_PATH}")

# --- 2. ČITANJE JSON ---
print("\n=== Čitanje JSON ===")
with open(JSON_PATH, "r", encoding="utf-8") as f:
    ucitani = json.load(f)

for s in ucitani:
    print(f"  [{s['id']}] {s['ime']} {s['prezime']}, {s['godine']} god.")

# --- 3. CRUD OPERACIJE ---
print("\n=== CRUD ===")

# CREATE
novi = {"id": 4, "ime": "Ahmed", "prezime": "Kavazovic", "godine": 26}
ucitani.append(novi)
print(f"CREATE: Dodat {novi['ime']}")

# UPDATE
for s in ucitani:
    if s["id"] == 2:
        s["prezime"] = "Dacić"
        print(f"UPDATE: ID 2 → prezime = '{s['prezime']}'")

# DELETE
ucitani = [s for s in ucitani if s["id"] != 3]
print("DELETE: Obrisan ID 3")

# SAVE
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(ucitani, f, indent=4, ensure_ascii=False)
print(f"\n✅ Ažurirano. Studenata: {len(ucitani)}")
