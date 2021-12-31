#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 05_Funkcije_i_Moduli / Predavanje 1
# Tema: Definicija funkcija, parametri, return, scope
# =============================================================================

# --- 1. OSNOVNA FUNKCIJA ---
def pozdrav(ime):
    """Ispisuje pozdravnu poruku."""
    return f"Zdravo, {ime}! Dobrodošli u ŠKOLICA Python."

print(pozdrav("Vahid"))
print(pozdrav("Kemo"))
print("")

# --- 2. FUNKCIJA SA DEFAULT PARAMETRIMA ---
def saberi(a, b=0, c=0):
    """Sabira dva ili tri broja."""
    return a + b + c

print("=== Default parametri ===")
print(f"saberi(5) = {saberi(5)}")
print(f"saberi(5, 3) = {saberi(5, 3)}")
print(f"saberi(5, 3, 2) = {saberi(5, 3, 2)}")
print("")

# --- 3. *ARGS — Proizvoljan broj argumenata ---
def suma_svih(*brojevi):
    """Prima proizvoljan broj argumenata."""
    return sum(brojevi)

print("=== *args ===")
print(f"suma_svih(1,2,3) = {suma_svih(1, 2, 3)}")
print(f"suma_svih(10,20,30,40) = {suma_svih(10, 20, 30, 40)}")
print("")

# --- 4. **KWARGS — Imenovani argumenti ---
def profil(**podaci):
    """Prima proizvoljne imenovane argumente."""
    for kljuc, vrednost in podaci.items():
        print(f"  {kljuc}: {vrednost}")

print("=== **kwargs ===")
profil(ime="Vahid", prezime="Zekic", godine=34, grad="Novi Pazar")
print("")

# --- 5. SCOPE VARIJABLI ---
print("=== Scope ===")
globalna = "Ja sam globalna"

def test_scope():
    lokalna = "Ja sam lokalna"
    print(f"  Unutar f-je: {globalna}")
    print(f"  Unutar f-je: {lokalna}")

test_scope()
print(f"  Van f-je: {globalna}")
# print(lokalna)  # NameError — lokalna ne postoji ovde
