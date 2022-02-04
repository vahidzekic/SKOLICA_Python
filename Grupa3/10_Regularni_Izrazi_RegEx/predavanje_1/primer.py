#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 10_Regularni_Izrazi_RegEx / Predavanje 1
# Tema: Osnove re modula — search, match, findall
# =============================================================================
import re

# --- 1. re.search() ---
print("=== re.search() ===")
tekst = "Moj broj telefona je 065-123-4567."
rezultat = re.search(r"\d{3}-\d{3}-\d{4}", tekst)
if rezultat:
    print(f"  Pronađen broj: {rezultat.group()}")

# --- 2. re.findall() ---
print("\n=== re.findall() ===")
tekst2 = "Email: vahid@skolica.rs i enes@skolica.rs i info@test.com"
emailovi = re.findall(r"[\w.]+@[\w.]+\.\w+", tekst2)
print(f"  Pronađeni emailovi: {emailovi}")

# --- 3. re.findall() SA GRUPAMA ---
print("\n=== Pronalaženje brojeva ===")
tekst3 = "Cena je 150 dinara, a popust 20 procenata. Ukupno: 120."
brojevi = re.findall(r"\d+", tekst3)
print(f"  Svi brojevi: {brojevi}")

# --- 4. re.sub() — Zamena ---
print("\n=== re.sub() ===")
tekst4 = "Java je najbolji jezik. Java je svuda."
novi = re.sub(r"Java", "Python", tekst4)
print(f"  Original: {tekst4}")
print(f"  Zamena: {novi}")

# --- 5. re.split() ---
print("\n=== re.split() ===")
tekst5 = "jabuka;banana,višnja narandža|kivi"
delovi = re.split(r"[;,\s|]+", tekst5)
print(f"  Split: {delovi}")
