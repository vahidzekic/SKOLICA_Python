#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 4: Petlje (Loops) i Iteracija
# Autor: dipl.inz. Vahid Zekic
# Opis: Demonstracija for, while petlji, iteracije kroz JSON, CRUD sa listama
# =============================================================================


# -----------------------------------------------------------------------------
# 1. FOR PETLJA — Iteracija kroz listu
# -----------------------------------------------------------------------------

print("=== FOR petlja: Iteracija kroz listu ===")

niz = ["Vahid", "Enes", "Senaid", "Kemo", "Semir", "Kavaz"]

# Najjednostavniji način — for-in
for clan in niz:
    print(" ", clan)
print("")


# -----------------------------------------------------------------------------
# 2. FOR PETLJA SA range() — Numerička iteracija
# -----------------------------------------------------------------------------

print("=== FOR petlja: range() primeri ===")

# range(n) — od 0 do n-1
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print("")

# range(start, stop) — od start do stop-1
print("range(3, 8):", end=" ")
for i in range(3, 8):
    print(i, end=" ")
print("")

# range(start, stop, step) — sa korakom
print("range(0, 20, 5):", end=" ")
for i in range(0, 20, 5):
    print(i, end=" ")
print("\n")


# -----------------------------------------------------------------------------
# 3. FOR PETLJA SA JSON OBJEKTOM — Iteracija kroz bazu podataka
# -----------------------------------------------------------------------------

print("=== FOR petlja: Iteracija kroz JSON objekat ===")

JSON = [
    {'ime': 'Vahid', 'prezime': 'Zekic', 'godina': 1986, 'pol': 'muski'},
    {'ime': 'Enes', 'prezime': 'Daca', 'godina': 1988, 'pol': 'muski'},
    {'ime': 'Senaid', 'prezime': 'Sarenkapic', 'godina': 1988, 'pol': 'muski'},
    {'ime': 'Mirza', 'prezime': 'Sarenkapic', 'godina': 1984, 'pol': 'muski'}
]

brojClanova = len(JSON)
print("Broj članova u bazi:", brojClanova)

# Metod 1: Direktna iteracija (preporučeno)
print("\nMetod 1 — Direktna iteracija:")
for osoba in JSON:
    print(f"  {osoba['ime']} {osoba['prezime']} — godina rođenja: {osoba['godina']}")

# Metod 2: Sa range() i indeksom
print("\nMetod 2 — Sa range() i indeksom:")
for id in range(0, brojClanova):
    print("  " + JSON[id]["ime"] + " " + JSON[id]["prezime"] +
          " ima godina " + str(JSON[id]["godina"]))
print("")


# -----------------------------------------------------------------------------
# 4. WHILE PETLJA — Ponavljanje do ispunjenja uslova
# -----------------------------------------------------------------------------

print("=== WHILE petlja ===")

# Osnovni brojač
i = 0
while i < 10:
    print(f"  Iteracija {i}")
    i += 1                   # KRITIČNO: bez ove linije — beskonačna petlja!

print("")


# -----------------------------------------------------------------------------
# 5. WHILE...ELSE — Blok koji se izvršava nakon petlje
# -----------------------------------------------------------------------------

print("=== WHILE...ELSE ===")

brojac = 5
while brojac > 0:
    print(f"  Odbrojavanje: {brojac}")
    brojac -= 1
else:
    print("  Odbrojavanje završeno! 🚀")
print("")


# -----------------------------------------------------------------------------
# 6. BREAK i CONTINUE — Kontrola toka petlje
# -----------------------------------------------------------------------------

print("=== BREAK i CONTINUE ===")

print("Sa continue (preskače 3 i 5):")
for i in range(8):
    if i == 3 or i == 5:
        continue                # Preskače ostatak iteracije
    print(f"  {i}", end="")
print("")

print("Sa break (prekida na 6):")
for i in range(10):
    if i == 6:
        break                   # Potpuno prekida petlju
    print(f"  {i}", end="")
print("\n")


# -----------------------------------------------------------------------------
# 7. PRAKTIČAN PRIMER — CRUD Operacije sa Listom
# -----------------------------------------------------------------------------

print("=== CRUD Operacije sa Listom ===")

lista = ["Python", "JavaScript", "C", "HTML"]
print("Početna lista:", lista)

# CREATE — Dodavanje novog elementa
lista.append("CSS")
print("Posle append('CSS'):", lista)

# READ — Čitanje elemenata petljom
print("Svi elementi:")
for index, element in enumerate(lista):
    print(f"  [{index}] {element}")

# UPDATE — Zamena elementa
lista[3] = "HTML5"
print("Posle liste[3] = 'HTML5':", lista)

# DELETE — Brisanje elementa
lista.remove("C")
print("Posle remove('C'):", lista)

# DELETE po poziciji
lista.pop(0)
print("Posle pop(0):", lista)

print("\nKonačna lista:", lista)
