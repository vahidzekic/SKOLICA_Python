#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 2: Tipovi Podataka
# Autor: dipl.inz. Vahid Zekic
# Opis: Demonstracija svih tipova podataka: list, tuple, set, dict, JSON
# =============================================================================


# -----------------------------------------------------------------------------
# 1. OSNOVNI TIPOVI PODATAKA
# -----------------------------------------------------------------------------

broj = 89                        # int — ceo broj
stringovi = 'Ja ucim Python'     # str — tekst (string)
bolian = True                    # bool — logička vrednost (True ili False)
decimalni = 3.14                 # float — decimalni broj

print("=== Osnovni tipovi ===")
print("Ceo broj:", broj, "| Tip:", type(broj))
print("String:", stringovi, "| Tip:", type(stringovi))
print("Boolean:", bolian, "| Tip:", type(bolian))
print("Float:", decimalni, "| Tip:", type(decimalni))
print("")


# -----------------------------------------------------------------------------
# 2. LISTE — Uređena, promenljiva kolekcija
# -----------------------------------------------------------------------------

print("=== Liste ===")

# Kreiranje liste sa različitim tipovima elemenata
lista = ['Vahid', 34, True, 'Enes', 'Senaid', 199, 199, 'Enes', 'Vahid']
print("Originalna lista:", lista)

# Brisanje elementa po vrednosti — uklanja PRVI pronađeni element
lista.remove('Vahid')
print("Posle remove('Vahid'):", lista)

# Brisanje elementa po poziciji (indeksu)
lista.pop(1)
print("Posle pop(1):", lista)

# Dodavanje elementa na kraj liste
lista.append('Auto')
print("Posle append('Auto'):", lista)

# Umetanje elementa na određenu poziciju
lista.insert(1, 'Vahid')
print("Posle insert(1, 'Vahid'):", lista)

# Zamena elementa na određenoj poziciji
lista[4] = 'Avion'
print("Posle lista[4] = 'Avion':", lista)

# Slicing — isecanje dela liste
lista1 = ["prvi", "drugi", "treci", "cetvrti", "peti", "shesti", "sedmi"]
print("\nSlicing primeri:")
print("lista1[2:]  =", lista1[2:])     # Od pozicije 2 do kraja
print("lista1[:5]  =", lista1[:5])     # Od početka do pozicije 5
print("lista1[2:5] =", lista1[2:5])    # Od pozicije 2 do 5
print("")


# -----------------------------------------------------------------------------
# 3. TUPLE — Uređena, NEPROMENLJIVA kolekcija
# -----------------------------------------------------------------------------

print("=== Tuple ===")

tuple1 = tuple()           # Prazan tuple
tuple1 = (1, 2, 3)         # Tuple sa elementima
print("Tuple:", tuple1)
print("Tip:", type(tuple1))

# Tuple kreiran od liste
tuple2 = tuple(['a', 'b', 'c'])
print("Tuple od liste:", tuple2)
print("")


# -----------------------------------------------------------------------------
# 4. SET — Neuređena kolekcija JEDINSTVENIH elemenata
# -----------------------------------------------------------------------------

print("=== Set ===")

# Set automatski uklanja duplikate
set1 = {1, 1, 1, 4, 4, 4, 5, 5, 5}
print("Set sa duplikatima:", set1)       # {1, 4, 5}
print("Broj elemenata:", len(set1))      # 3

# Kreiranje seta od liste — uklanja duplikate
set2 = set(lista)
print("Set od liste:", set2)
print("")


# -----------------------------------------------------------------------------
# 5. DICTIONARY (Rečnik) — Ključ-vrednost parovi
# -----------------------------------------------------------------------------

print("=== Dictionary ===")

auto = {
    "marka": "BMW",
    "model": "M8",
    "boja": "Crvena",
    "godina": 2020
}

# Čitanje vrednosti po ključu
print("Marka:", auto["marka"])
print("Model:", auto["model"])

# Izmena vrednosti
auto["marka"] = "Audi"
print("Nova marka:", auto["marka"])

# Dodavanje novog ključ-vrednost para
auto["sedista"] = 5

# Ažuriranje sa update()
auto.update({"godina": 2021})

# Ispis kompletnih informacija
autoInfo = (str(auto["marka"]) + " " + str(auto["model"]) + " " +
            str(auto["boja"]) + " " + str(auto["godina"]) + " sedišta: " +
            str(auto["sedista"]))
print("Kompletne info:", autoInfo)
print("")


# -----------------------------------------------------------------------------
# 6. JSON OBJEKAT — Lista rečnika (simulacija baze podataka)
# -----------------------------------------------------------------------------

print("=== JSON Objekat ===")

JsonObjekat = [
    {
        "id": 1,
        "ime": "Vahid",
        "prezime": "Zekic",
        "godine": 34,
        "pol": "muski"
    },
    {
        "id": 2,
        "ime": "Omer",
        "prezime": "Ljajic",
        "godine": 34,
        "pol": "muski"
    },
    {
        "id": 3,
        "ime": "Kemo",
        "prezime": "Plojovic",
        "godine": 27,
        "pol": "muski"
    }
]

# Čitanje vrednosti dvostrukim indeksiranjem: lista[index][ključ]
print("Ime prvog studenta:", JsonObjekat[0]["ime"])
print("Prezime drugog studenta:", JsonObjekat[1]["prezime"])

# Dodavanje novog rečnika u JSON objekat
noviStudent = {
    "id": 4,
    "ime": "Muhamed",
    "prezime": "Zukovic",
    "godine": 34,
    "pol": "muski"
}
JsonObjekat.append(noviStudent)

# Izmena vrednosti unutar JSON objekta
JsonObjekat[2]["ime"] = "Kemal"

print("\nKompletan JSON objekat nakon izmena:")
for student in JsonObjekat:
    print(f"  ID: {student['id']} | {student['ime']} {student['prezime']} | "
          f"Godine: {student['godine']}")
