#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 6: Moduli, Funkcije i Rad sa Fajlovima
# Autor: dipl.inz. Vahid Zekic
# Opis: Demonstracija funkcija, modularnog koda, čitanja/pisanja fajlova, JSON
# =============================================================================

import json
import os


# =============================================================================
# 1. DEFINICIJA FUNKCIJA — Modul za matematičke operacije
# =============================================================================

def sabiranje(prviBroj, drugiBroj):
    """Sabira dva broja i vraća rezultat."""
    zbir = prviBroj + drugiBroj
    return zbir


def oduzimanje(prviBroj, drugiBroj):
    """Oduzima drugi broj od prvog i vraća rezultat."""
    razlika = prviBroj - drugiBroj
    return razlika


def mnozenje(prviBroj, drugiBroj):
    """Množi dva broja i vraća rezultat."""
    proizvod = prviBroj * drugiBroj
    return proizvod


def deljenje(prviBroj, drugiBroj):
    """Deli prvi broj drugim. Proverava deljenje sa nulom."""
    if drugiBroj == 0:
        return "Greška: Deljenje sa nulom!"
    kolicnik = prviBroj / drugiBroj
    return kolicnik


# =============================================================================
# 2. FUNKCIJE SA PODRAZUMEVANIM PARAMETRIMA
# =============================================================================

def pozdrav(ime, pozdravna_rec="Zdravo"):
    """Kreira pozdravnu poruku sa opcionom pozdravnom reči."""
    return f"{pozdravna_rec}, {ime}!"


def formatiraj_osobu(ime, prezime, godine, separator=" | "):
    """Formatira informacije o osobi sa prilagodljivim separatorom."""
    return f"{ime}{separator}{prezime}{separator}{godine} god."


# =============================================================================
# 3. FUNKCIJE SA *args i **kwargs
# =============================================================================

def suma_svih(*brojevi):
    """Prima proizvoljan broj argumenata i vraća njihovu sumu."""
    return sum(brojevi)


def kreiraj_profil(**podaci):
    """Prima proizvoljne imenovane argumente i kreira rečnik profila."""
    profil = {}
    for kljuc, vrednost in podaci.items():
        profil[kljuc] = vrednost
    return profil


# =============================================================================
# DEMONSTRACIJA
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("  ŠKOLICA Python — Grupa 6: Moduli, Funkcije i Fajlovi")
    print("=" * 70)
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 4. KORIŠĆENJE FUNKCIJA
    # ─────────────────────────────────────────────────────────────────────

    print("=== Matematičke funkcije ===\n")

    a, b = 15, 4

    print(f"  Sabiranje:   {a} + {b} = {sabiranje(a, b)}")
    print(f"  Oduzimanje:  {a} - {b} = {oduzimanje(a, b)}")
    print(f"  Množenje:    {a} × {b} = {mnozenje(a, b)}")
    print(f"  Deljenje:    {a} ÷ {b} = {deljenje(a, b)}")
    print(f"  Deljenje:    {a} ÷ 0 = {deljenje(a, 0)}")
    print("")

    print("=== Funkcije sa podrazumevanim parametrima ===\n")
    print(f"  {pozdrav('Vahid')}")
    print(f"  {pozdrav('Vahid', 'Ćao')}")
    print(f"  {formatiraj_osobu('Vahid', 'Zekic', 34)}")
    print(f"  {formatiraj_osobu('Vahid', 'Zekic', 34, separator=' - ')}")
    print("")

    print("=== Funkcije sa *args i **kwargs ===\n")
    print(f"  Suma(1,2,3,4,5) = {suma_svih(1, 2, 3, 4, 5)}")
    print(f"  Suma(10,20) = {suma_svih(10, 20)}")

    profil = kreiraj_profil(ime="Vahid", prezime="Zekic", godine=34, grad="Novi Pazar")
    print(f"  Profil: {profil}")
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 5. RAD SA FAJLOVIMA — Tekstualni fajlovi
    # ─────────────────────────────────────────────────────────────────────

    print("=== Rad sa tekstualnim fajlovima ===\n")

    # Kreiranje direktorijuma za podatke
    os.makedirs("data", exist_ok=True)

    # PISANJE u fajl (mod "w" — Write, briše prethodni sadržaj)
    with open("data/beleshke.txt", "w", encoding="utf-8") as fajl:
        fajl.write("ŠKOLICA Python — Beleške\n")
        fajl.write("========================\n\n")
        fajl.write("Lekcija 1: Osnove Python-a\n")
        fajl.write("Lekcija 2: Tipovi podataka\n")
        fajl.write("Lekcija 3: Kontrolne strukture\n")
    print("  ✓ Fajl 'data/beleshke.txt' uspešno kreiran.")

    # DODAVANJE na kraj fajla (mod "a" — Append)
    with open("data/beleshke.txt", "a", encoding="utf-8") as fajl:
        fajl.write("Lekcija 4: Petlje\n")
        fajl.write("Lekcija 5: OOP\n")
        fajl.write("Lekcija 6: Moduli i fajlovi\n")
    print("  ✓ Dodatne lekcije dodate u fajl.")

    # ČITANJE fajla (mod "r" — Read)
    with open("data/beleshke.txt", "r", encoding="utf-8") as fajl:
        sadrzaj = fajl.read()
    print(f"\n  Sadržaj fajla:\n  {'─' * 40}")
    for linija in sadrzaj.strip().split("\n"):
        print(f"  {linija}")
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 6. RAD SA JSON FAJLOVIMA
    # ─────────────────────────────────────────────────────────────────────

    print("=== Rad sa JSON fajlovima ===\n")

    # JSON podaci — lista rečnika (simulacija baze podataka)
    studenti = [
        {"id": 1, "ime": "Vahid", "prezime": "Zekic", "godine": 34, "pol": "muski"},
        {"id": 2, "ime": "Enes", "prezime": "Daca", "godine": 32, "pol": "muski"},
        {"id": 3, "ime": "Senaid", "prezime": "Sarenkapic", "godine": 32, "pol": "muski"}
    ]

    # PISANJE JSON fajla
    json_putanja = "data/studenti.json"
    with open(json_putanja, "w", encoding="utf-8") as fajl:
        json.dump(studenti, fajl, indent=4, ensure_ascii=False)
    print(f"  ✓ JSON fajl '{json_putanja}' uspešno kreiran.")

    # ČITANJE JSON fajla
    with open(json_putanja, "r", encoding="utf-8") as fajl:
        ucitani_podaci = json.load(fajl)

    print(f"  Učitano studenata: {len(ucitani_podaci)}\n")
    for student in ucitani_podaci:
        print(f"  ID: {student['id']} | {student['ime']} {student['prezime']} "
              f"| Godine: {student['godine']}")

    # DODAVANJE novog studenta i ažuriranje fajla
    novi_student = {"id": 4, "ime": "Ahmed", "prezime": "Kavazovic",
                    "godine": 26, "pol": "muski"}
    ucitani_podaci.append(novi_student)

    with open(json_putanja, "w", encoding="utf-8") as fajl:
        json.dump(ucitani_podaci, fajl, indent=4, ensure_ascii=False)
    print(f"\n  ✓ Dodat novi student: {novi_student['ime']} {novi_student['prezime']}")
    print(f"  Ukupno studenata sada: {len(ucitani_podaci)}")

    # ─────────────────────────────────────────────────────────────────────
    # 7. PRAKTIČAN PRIMER — Interaktivni CRUD sa JSON persistencijom
    # ─────────────────────────────────────────────────────────────────────

    print("\n=== CRUD sa JSON persistencijom ===\n")

    # Čitamo postojeće podatke
    with open(json_putanja, "r", encoding="utf-8") as fajl:
        baza = json.load(fajl)

    # CREATE — Dodajemo zapis
    baza.append({"id": 5, "ime": "Muhamed", "prezime": "Zukovic",
                 "godine": 34, "pol": "muski"})
    print("  CREATE: Dodat Muhamed Zukovic")

    # READ — Čitamo sve zapise
    print("  READ: Svi studenti:")
    for s in baza:
        print(f"    [{s['id']}] {s['ime']} {s['prezime']}")

    # UPDATE — Menjamo prezime studenta sa ID 2
    for s in baza:
        if s["id"] == 2:
            s["prezime"] = "Dacic"
            print(f"  UPDATE: Student ID 2 → prezime promenjeno u '{s['prezime']}'")

    # DELETE — Brišemo studenta sa ID 3
    baza = [s for s in baza if s["id"] != 3]
    print("  DELETE: Student ID 3 obrisan")

    # Čuvamo ažuriranu bazu
    with open(json_putanja, "w", encoding="utf-8") as fajl:
        json.dump(baza, fajl, indent=4, ensure_ascii=False)
    print(f"\n  ✓ Baza ažurirana. Preostalo studenata: {len(baza)}")
