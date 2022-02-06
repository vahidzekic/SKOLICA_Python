#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 10_Regularni_Izrazi_RegEx / Predavanje 2
# Tema: Grupe, imenovane grupe, validacija
# =============================================================================
import re

# --- 1. GRUPE ---
print("=== Grupe ===")
email = "vahid.zekic@skolica.rs"
m = re.match(r"([\w.]+)@([\w.]+)\.([a-z]+)", email)
if m:
    print(f"  Email: {m.group(0)}")
    print(f"  Korisnik: {m.group(1)}")
    print(f"  Domen: {m.group(2)}")
    print(f"  TLD: {m.group(3)}")
print("")

# --- 2. IMENOVANE GRUPE ---
print("=== Imenovane grupe ===")
tekst = "Vahid Zekic, 34 godina, Novi Pazar"
m = re.search(r"(?P<ime>\w+) (?P<prezime>\w+), (?P<godine>\d+)", tekst)
if m:
    print(f"  Ime: {m.group('ime')}")
    print(f"  Prezime: {m.group('prezime')}")
    print(f"  Godine: {m.group('godine')}")
print("")

# --- 3. VALIDACIJA ---
print("=== Validacije ===")

def validacija(obrazac, tekst, opis):
    if re.match(obrazac, tekst):
        print(f"  ✅ {opis}: '{tekst}' — validno")
    else:
        print(f"  ❌ {opis}: '{tekst}' — nevalidno")

# Email
email_re = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
validacija(email_re, "vahid@skolica.rs", "Email")
validacija(email_re, "invalid@", "Email")

# Telefon
tel_re = r"^\+?[0-9]{10,15}$"
validacija(tel_re, "+381651234567", "Telefon")
validacija(tel_re, "123", "Telefon")

# Lozinka (min 8, bar 1 veliko slovo, bar 1 cifra)
pass_re = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
validacija(pass_re, "MojaLozinka1", "Lozinka")
validacija(pass_re, "slaba", "Lozinka")
