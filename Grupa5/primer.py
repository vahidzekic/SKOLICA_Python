#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 5: Objektno-Orijentisano Programiranje (OOP)
# Autor: dipl.inz. Vahid Zekic
# Opis: Hijerarhija klasa Osoba -> Radnik, Student sa nasleđivanjem
# =============================================================================


# =============================================================================
# 1. BAZNA KLASA — Osoba
# =============================================================================

class Osoba:
    """
    Bazna klasa koja predstavlja opštu osobu.
    Svi ostali tipovi osoba (Radnik, Student) nasleđuju ovu klasu.
    """

    def __init__(self, ime, prezime, godine):
        """Konstruktor — inicijalizuje osnovne atribute osobe."""
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def predstaviSe(self):
        """Vraća formatiran string sa informacijama o osobi."""
        return f"{self.ime} {self.prezime}, {self.godine} godina"

    def daLiJePunoletan(self):
        """Proverava da li je osoba punoletna (18+)."""
        return self.godine >= 18

    def __str__(self):
        """Magična metoda — poziva se kad koristimo print() na objektu."""
        return self.predstaviSe()


# =============================================================================
# 2. IZVEDENA KLASA — Radnik (nasleđuje Osoba)
# =============================================================================

class Radnik(Osoba):
    """
    Klasa Radnik nasleđuje Osoba i dodaje specifične atribute:
    firma, pozicija, plata.
    """

    def __init__(self, ime, prezime, godine, firma, pozicija, plata):
        # super().__init__() poziva konstruktor roditeljske klase (Osoba)
        super().__init__(ime, prezime, godine)
        self.firma = firma
        self.pozicija = pozicija
        self.plata = plata

    def predstaviSe(self):
        """Polimorfizam — ista metoda, drugačija implementacija."""
        return (f"{self.ime} {self.prezime} — {self.pozicija} u firmi "
                f"'{self.firma}', plata: {self.plata} RSD")

    def izracunajGodisnjiPrihod(self):
        """Izračunava godišnji prihod (12 meseci + bonus)."""
        bonus = self.plata * 0.1   # 10% bonus
        return (self.plata * 12) + bonus

    def unapredji(self, nova_pozicija, povecanje_procent):
        """Unapređuje radnika na novu poziciju sa povećanjem plate."""
        self.pozicija = nova_pozicija
        self.plata = self.plata * (1 + povecanje_procent / 100)
        print(f"  ✓ {self.ime} je unapređen/a na '{nova_pozicija}' "
              f"sa novom platom: {self.plata:.0f} RSD")


# =============================================================================
# 3. IZVEDENA KLASA — Student (nasleđuje Osoba)
# =============================================================================

class Student(Osoba):
    """
    Klasa Student nasleđuje Osoba i dodaje specifične atribute:
    fakultet, smer, prosek.
    """

    def __init__(self, ime, prezime, godine, fakultet, smer, prosek=0.0):
        super().__init__(ime, prezime, godine)
        self.fakultet = fakultet
        self.smer = smer
        self.prosek = prosek
        self.polozeniIspiti = []    # Lista položenih ispita

    def predstaviSe(self):
        """Polimorfizam — verzija za studenta."""
        return (f"{self.ime} {self.prezime} — student {self.smer}, "
                f"fakultet: {self.fakultet}, prosek: {self.prosek}")

    def polaziIspit(self, predmet, ocena):
        """Dodaje položeni ispit i ažurira prosek."""
        self.polozeniIspiti.append({"predmet": predmet, "ocena": ocena})
        # Preračunavanje proseka
        ukupno = sum(ispit["ocena"] for ispit in self.polozeniIspiti)
        self.prosek = round(ukupno / len(self.polozeniIspiti), 2)
        print(f"  ✓ {self.ime} je položio/la '{predmet}' sa ocenom {ocena}. "
              f"Novi prosek: {self.prosek}")

    def statusStudenta(self):
        """Vraća status studenta na osnovu proseka."""
        if self.prosek >= 9.0:
            return "Odličan student 🏆"
        elif self.prosek >= 8.0:
            return "Vrlo dobar student ⭐"
        elif self.prosek >= 7.0:
            return "Dobar student 📚"
        elif self.prosek >= 6.0:
            return "Prosečan student"
        else:
            return "Nedovoljan prosek ⚠️"


# =============================================================================
# DEMONSTRACIJA — Kreiranje objekata i korišćenje metoda
# =============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("  ŠKOLICA Python — Grupa 5: OOP Demonstracija")
    print("=" * 70)
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 4. KREIRANJE OBJEKATA — Instanciranje klasa
    # ─────────────────────────────────────────────────────────────────────

    print("=== Kreiranje objekata ===\n")

    # Bazna klasa — Osoba
    osoba1 = Osoba("Vahid", "Zekic", 34)
    osoba2 = Osoba("Kemo", "Plojovic", 27)

    # Izvedena klasa — Radnik
    radnik1 = Radnik("Senaid", "Sarenkapic", 32,
                     "Tech Solutions", "Senior Developer", 150000)
    radnik2 = Radnik("Enes", "Daca", 32,
                     "Web Studio", "Junior Developer", 80000)

    # Izvedena klasa — Student
    student1 = Student("Nerma", "Zekic", 22,
                       "Prirodno-matematički fakultet", "Informatika")
    student2 = Student("Ahmed", "Kavazovic", 20,
                       "Tehnički fakultet", "Elektrotehnika")

    # ─────────────────────────────────────────────────────────────────────
    # 5. POLIMORFIZAM — Ista metoda, različiti rezultati
    # ─────────────────────────────────────────────────────────────────────

    print("=== Polimorfizam: predstaviSe() ===\n")

    # Stavljamo SVE objekte u jednu listu — svi su tipa Osoba ili podtipa
    sveOsobe = [osoba1, osoba2, radnik1, radnik2, student1, student2]

    for osoba in sveOsobe:
        print(f"  [{osoba.__class__.__name__}] {osoba.predstaviSe()}")
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 6. KORIŠĆENJE SPECIFIČNIH METODA
    # ─────────────────────────────────────────────────────────────────────

    print("=== Radnik — Unapređenje i plata ===\n")

    print(f"  Godišnji prihod radnika {radnik1.ime}: "
          f"{radnik1.izracunajGodisnjiPrihod():,.0f} RSD")
    radnik1.unapredji("Tech Lead", 20)
    print(f"  Novi godišnji prihod: "
          f"{radnik1.izracunajGodisnjiPrihod():,.0f} RSD")
    print("")

    print("=== Student — Polaganje ispita ===\n")

    student1.polaziIspit("Programiranje 1", 9)
    student1.polaziIspit("Matematika 1", 8)
    student1.polaziIspit("Algoritmi", 10)
    print(f"  Status: {student1.statusStudenta()}")
    print(f"  Položeni ispiti: {len(student1.polozeniIspiti)}")
    print("")

    # ─────────────────────────────────────────────────────────────────────
    # 7. INSTANCIRANJE IZ JSON BAZE PODATAKA
    # ─────────────────────────────────────────────────────────────────────

    print("=== Instanciranje iz JSON baze ===\n")

    osobeBaza = [
        {"id": 1, "ime": "Vahid", "prezime": "Zekic", "godine": 34},
        {"id": 2, "ime": "Senaid", "prezime": "Sarenkapic", "godine": 32},
        {"id": 3, "ime": "Enes", "prezime": "Daca", "godine": 32},
        {"id": 4, "ime": "Ahmed", "prezime": "Kavazovic", "godine": 26}
    ]

    print(f"  U bazi podataka se nalazi članova: {len(osobeBaza)}\n")

    for podatak in osobeBaza:
        osoba = Osoba(podatak["ime"], podatak["prezime"], podatak["godine"])
        punoletan = "Da ✓" if osoba.daLiJePunoletan() else "Ne ✗"
        print(f"  {osoba.predstaviSe()} | Punoletan: {punoletan}")

    # ─────────────────────────────────────────────────────────────────────
    # 8. PROVERA NASLEĐIVANJA — isinstance() i issubclass()
    # ─────────────────────────────────────────────────────────────────────

    print("\n=== Provera nasleđivanja ===\n")

    print(f"  Da li je radnik1 instanca Radnik? {isinstance(radnik1, Radnik)}")
    print(f"  Da li je radnik1 instanca Osoba?  {isinstance(radnik1, Osoba)}")
    print(f"  Da li je Radnik podklasa Osoba?   {issubclass(Radnik, Osoba)}")
    print(f"  Da li je Student podklasa Osoba?  {issubclass(Student, Osoba)}")
    print(f"  Da li je Student podklasa Radnik? {issubclass(Student, Radnik)}")
