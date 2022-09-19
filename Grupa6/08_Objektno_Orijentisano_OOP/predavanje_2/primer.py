#!/usr/bin/env python3
# âââââââââââââââââââââââââââââââââââââââ
# Grupa6 / 08 / P2 â Osoba -> Radnik, Student (OBAVEZNO)
# âââââââââââââââââââââââââââââââââââââââ

class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
    def predstaviSe(self):
        return f"{self.ime} {self.prezime}, {self.godine} god."
    def __str__(self):
        return self.predstaviSe()

class Radnik(Osoba):
    def __init__(self, ime, prezime, godine, firma, pozicija, plata):
        super().__init__(ime, prezime, godine)
        self.firma = firma
        self.pozicija = pozicija
        self.plata = plata
    def predstaviSe(self):
        return f"{self.ime} {self.prezime} â {self.pozicija} @ {self.firma}, {self.plata:,} RSD"
    def godisnja(self):
        return self.plata * 12

class Student(Osoba):
    def __init__(self, ime, prezime, godine, fax, smer, prosek=0.0):
        super().__init__(ime, prezime, godine)
        self.fax = fax
        self.smer = smer
        self.prosek = prosek
        self.ispiti = []
    def predstaviSe(self):
        return f"{self.ime} {self.prezime} â {self.smer}, {self.fax}, prosek: {self.prosek:.1f}"
    def polozi(self, predmet, ocena):
        self.ispiti.append({"p": predmet, "o": ocena})
        self.prosek = sum(i["o"] for i in self.ispiti) / len(self.ispiti)
    def rang(self):
        if self.prosek >= 9: return "OdliÄan"
        if self.prosek >= 8: return "Vrlo dobar"
        return "Dobar"

if __name__ == '__main__':
    osobe = [
        Osoba("Vahid", "Zekic", 34),
        Radnik("Petar", "P.", 35, "MuziÄkaKuÄa", "Producent", 160000),
        Student("Sara", "S.", 22, "FMU", "Kompozicija"),
    ]
    print("=== Polimorfizam ===")
    for o in osobe:
        print(f"  [{type(o).__name__}] {o}")
    s = osobe[2]
    s.polozi("Harmonija", 10)
    s.polozi("Kontrapunkt", 9)
    print(f"\n  {s.ime}: prosek={s.prosek:.1f}, rang={s.rang()}")
    print(f"  isinstance(Radnik, Osoba): {isinstance(osobe[1], Osoba)}")