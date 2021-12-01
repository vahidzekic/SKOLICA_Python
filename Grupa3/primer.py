#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 3: Kontrolne Strukture (Uslovno Grananje)
# Autor: dipl.inz. Vahid Zekic
# Opis: Demonstracija if, if-else, if-elif-else, logičkih operatora
# =============================================================================


# Definišemo varijable za demonstraciju
prviBroj = 12
drugiBroj = 9
treciBroj = 11
cetvrtiBroj = 20

# Pripremamo poruke za ispis
poruka1 = ("Prvi broj " + str(prviBroj) + " je manji od drugog broja "
           + str(drugiBroj) + ".")
poruka2 = ("Prvi broj " + str(prviBroj) + " je veci od drugog broja "
           + str(drugiBroj) + ".")
poruka3 = ("Prvi broj " + str(prviBroj) + " je jednak drugom broju "
           + str(drugiBroj) + ".")


# -----------------------------------------------------------------------------
# 1. IF — Jednostavan uslov
# -----------------------------------------------------------------------------
# Kod unutar if bloka se izvršava SAMO ako je uslov True

print("=== IF uslov ===")
if prviBroj < drugiBroj:
    print(poruka1)
print("(Ako se ništa ne ispiše, uslov nije ispunjen)")
print("")


# -----------------------------------------------------------------------------
# 2. IF...ELSE — Uslov sa alternativom
# -----------------------------------------------------------------------------
# Uvek se izvršava TAČNO JEDAN od dva bloka

print("=== IF...ELSE ===")
if prviBroj < drugiBroj:
    print(poruka1)
else:
    print(poruka2)
print("")


# -----------------------------------------------------------------------------
# 3. IF...ELIF...ELSE — Lanac više uslova
# -----------------------------------------------------------------------------
# Python proverava uslove ODOZGO NADOLE i izvršava samo prvi ispunjeni

print("=== IF...ELIF...ELSE ===")
if prviBroj < drugiBroj:
    print("Uslov 1:", poruka1)
elif drugiBroj > treciBroj:
    print("Uslov 2: Drugi broj je veci od treceg.")
elif treciBroj > prviBroj:
    print("Uslov 3: Treci broj je veci od prvog.")
else:
    print("Ni jedan uslov nije ispunjen.")
print("")


# -----------------------------------------------------------------------------
# 4. LOGIČKI OPERATORI — and, or, not
# -----------------------------------------------------------------------------

print("=== Logički operatori ===")

godine = 25
plata = 3000

# AND — oba uslova moraju biti True
if godine >= 18 and plata >= 2000:
    print("Osoba je punoletna I ima dovoljnu platu.")

# OR — bar jedan uslov mora biti True
if godine < 18 or plata < 1000:
    print("Osoba je maloletna ILI ima malu platu.")
else:
    print("Osoba je punoletna I ima platu iznad 1000.")

# NOT — negacija uslova
aktivan = False
if not aktivan:
    print("Korisnik NIJE aktivan.")
print("")


# -----------------------------------------------------------------------------
# 5. UGNEŽĐENI USLOVI (Nested If)
# -----------------------------------------------------------------------------

print("=== Ugnežđeni uslovi ===")

ocena = 85

if ocena >= 50:
    print("Student je položio ispit.")
    if ocena >= 90:
        print("  Ocena: 10 (Odličan)")
    elif ocena >= 80:
        print("  Ocena: 9 (Vrlo dobar)")
    elif ocena >= 70:
        print("  Ocena: 8 (Dobar)")
    elif ocena >= 60:
        print("  Ocena: 7 (Zadovoljavajući)")
    else:
        print("  Ocena: 6 (Dovoljan)")
else:
    print("Student NIJE položio ispit.")
    print("  Potrebno je ponovo polagati.")
print("")


# -----------------------------------------------------------------------------
# 6. PRAKTIČAN PRIMER — Korisnički unos sa validacijom
# -----------------------------------------------------------------------------

print("=== Praktičan primer: Provera starosne dobi ===")

# Čitamo korisnički unos
unos = input("Unesite vaše godine: ")

# Validacija — proveravamo da li je unos broj
if unos.isdigit():
    godine_korisnika = int(unos)

    if godine_korisnika < 0:
        print("Greška: Godine ne mogu biti negativne!")
    elif godine_korisnika < 7:
        print("Predškolski uzrast.")
    elif godine_korisnika < 15:
        print("Osnovna škola.")
    elif godine_korisnika < 19:
        print("Srednja škola.")
    elif godine_korisnika < 26:
        print("Fakultet.")
    else:
        print("Radno sposobna osoba.")
else:
    print("Greška: Molimo unesite validan broj!")
