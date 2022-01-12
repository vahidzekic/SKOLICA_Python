#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 06_Rad_Sa_Fajlovima / Predavanje 3
# Tema: CSV fajlovi, os.path, listanje direktorijuma
# =============================================================================
import csv
import os

os.makedirs("data", exist_ok=True)

# --- 1. PISANJE CSV ---
print("=== Pisanje CSV ===")
CSV_PATH = "data/polaznici.csv"
polaznici = [
    ["Ime", "Prezime", "Godine", "Grupa"],
    ["Vahid", "Zekic", 34, "Grupa3"],
    ["Enes", "Daca", 32, "Grupa3"],
    ["Kemo", "Plojovic", 27, "Grupa3"],
    ["Ahmed", "Kavazovic", 26, "Grupa3"]
]

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(polaznici)
print(f"✅ CSV kreiran: {CSV_PATH}")

# --- 2. ČITANJE CSV ---
print("\n=== Čitanje CSV ===")
with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    zaglavlje = next(reader)
    print(f"  Kolone: {zaglavlje}")
    for red in reader:
        print(f"  {red[0]} {red[1]}, {red[2]} god. — {red[3]}")

# --- 3. OS.PATH ---
print("\n=== os.path ===")
print(f"  CWD: {os.getcwd()}")
print(f"  data/ postoji: {os.path.exists('data')}")
print(f"  data/ je dir: {os.path.isdir('data')}")

print("\n  Fajlovi u data/:")
for fajl in os.listdir("data"):
    putanja = os.path.join("data", fajl)
    velicina = os.path.getsize(putanja)
    print(f"    {fajl} ({velicina} bajtova)")
