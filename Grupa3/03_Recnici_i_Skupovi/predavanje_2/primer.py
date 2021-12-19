#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 03_Recnici_i_Skupovi / Predavanje 2
# Tema: Skupovi — kreiranje, operacije, uklanjanje duplikata
# =============================================================================

# --- 1. KREIRANJE SKUPOVA ---
print("=== Kreiranje skupova ===")
s1 = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print(f"Set sa duplikatima: {{1,2,2,3,3,3,4,5,5}} → {s1}")

# Set od liste — uklanja duplikate
lista = ["Vahid", "Kemo", "Omer", "Kemo", "Vahid"]
unikatni = set(lista)
print(f"Lista: {lista}")
print(f"Set (bez duplikata): {unikatni}")
print("")

# --- 2. MATEMATIČKE OPERACIJE ---
print("=== Operacije sa skupovima ===")
python_studenti = {"Vahid", "Enes", "Kemo", "Senaid"}
js_studenti = {"Kemo", "Ahmed", "Vahid", "Mirza"}

print(f"Python: {python_studenti}")
print(f"JS: {js_studenti}")
print(f"Unija (svi): {python_studenti | js_studenti}")
print(f"Presek (oba): {python_studenti & js_studenti}")
print(f"Samo Python: {python_studenti - js_studenti}")
print(f"Samo JS: {js_studenti - python_studenti}")
print(f"Sim. razlika: {python_studenti ^ js_studenti}")
print("")

# --- 3. METODE ---
print("=== Metode ===")
s = {10, 20, 30}
s.add(40)
print(f"add(40): {s}")
s.discard(20)
print(f"discard(20): {s}")
print(f"30 in s: {30 in s}")
