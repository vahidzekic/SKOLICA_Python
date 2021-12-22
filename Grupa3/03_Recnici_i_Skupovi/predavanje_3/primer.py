#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 03_Recnici_i_Skupovi / Predavanje 3
# Tema: Dict comprehension, ugnežđeni rečnici, Counter
# =============================================================================
from collections import Counter, defaultdict

# --- 1. DICT COMPREHENSION ---
print("=== Dict Comprehension ===")
kvadrati = {x: x ** 2 for x in range(1, 8)}
print(f"Kvadrati: {kvadrati}")

# Filtriranje — samo parni
samo_parni = {k: v for k, v in kvadrati.items() if k % 2 == 0}
print(f"Samo parni ključevi: {samo_parni}")
print("")

# --- 2. UGNEŽĐENI REČNICI ---
print("=== Ugnežđeni rečnici ===")
skola = {
    "Grupa1": {"polaznika": 12, "predavac": "Vahid", "oblast": "Python"},
    "Grupa2": {"polaznika": 10, "predavac": "Enes", "oblast": "JavaScript"},
    "Grupa3": {"polaznika": 8, "predavac": "Senaid", "oblast": "HTML/CSS"}
}

for grupa, info in skola.items():
    print(f"  {grupa}: {info['polaznika']} polaznika, "
          f"predavač: {info['predavac']}")
print("")

# --- 3. COUNTER ---
print("=== Counter ===")
reci = "jabuka banana jabuka višnja banana jabuka".split()
brojac = Counter(reci)
print(f"Brojanje reči: {dict(brojac)}")
print(f"Najčešća 2: {brojac.most_common(2)}")
print("")

# --- 4. DEFAULTDICT ---
print("=== defaultdict ===")
kategorije = defaultdict(list)
proizvodi = [("voce", "jabuka"), ("povrce", "krastavac"),
             ("voce", "banana"), ("povrce", "paradajz"), ("voce", "višnja")]

for kategorija, proizvod in proizvodi:
    kategorije[kategorija].append(proizvod)

for kat, items in kategorije.items():
    print(f"  {kat}: {items}")
