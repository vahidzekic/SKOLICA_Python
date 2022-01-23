#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 08_OOP / Predavanje 2
# Tema: Nasleđivanje — Osoba → Radnik, Student (OBAVEZNA IMPLEMENTACIJA)
# =============================================================================

# --- BAZNA KLASA ---
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def predstaviSe(self):
        return f"{self.ime} {self.prezime}, {self.godine} god."

    def __str__(self):
        return self.predstaviSe()

# --- IZVEDENA KLASA: Radnik ---
class Radnik(Osoba):
    def __init__(self, ime, prezime, godine, firma, pozicija, plata):
        super().__init__(ime, prezime, godine)
        self.firma = firma
        self.pozicija = pozicija
        self.plata = plata

    def predstaviSe(self):
        return (f"{self.ime} {self.prezime} — {self.pozicija} "
                f"u '{self.firma}', plata: {self.plata:,} RSD")

    def godisnji_prihod(self):
        return self.plata * 12

# --- IZVEDENA KLASA: Student ---
class Student(Osoba):
    def __init__(self, ime, prezime, godine, fakultet, smer, prosek=0.0):
        super().__init__(ime, prezime, godine)
        self.fakultet = fakultet
        self.smer = smer
        self.prosek = prosek

    def predstaviSe(self):
        return (f"{self.ime} {self.prezime} — {self.smer}, "
                f"{self.fakultet}, prosek: {self.prosek}")

    def status(self):
        if self.prosek >= 9.0:
            return "Odličan 🏆"
        elif self.prosek >= 8.0:
            return "Vrlo dobar ⭐"
        elif self.prosek >= 7.0:
            return "Dobar 📚"
        return "Prosečan"

# --- DEMONSTRACIJA ---
if __name__ == "__main__":
    print("=== Polimorfizam ===\n")

    osobe = [
        Osoba("Vahid", "Zekic", 34),
        Radnik("Senaid", "Sarenkapic", 32, "Tech Solutions",
               "Senior Dev", 150000),
        Radnik("Enes", "Daca", 32, "Web Studio", "Junior Dev", 80000),
        Student("Nerma", "Zekic", 22, "PMF", "Informatika", 9.2),
        Student("Ahmed", "Kavazovic", 20, "TF", "Elektrotehnika", 8.1),
    ]

    for osoba in osobe:
        tip = osoba.__class__.__name__
        print(f"  [{tip}] {osoba.predstaviSe()}")

    print(f"\n  Radnik godišnji: {osobe[1].godisnji_prihod():,} RSD")
    print(f"  Student status: {osobe[3].status()}")

    print(f"\n  isinstance check:")
    print(f"    Radnik je Osoba? {isinstance(osobe[1], Osoba)}")
    print(f"    Student je Radnik? {isinstance(osobe[3], Radnik)}")
