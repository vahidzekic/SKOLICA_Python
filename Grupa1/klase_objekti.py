class Osobe:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

class Radnici():
    def __init__(self, ime):
        self.ime = ime

class Studenti(Osobe):
    pass
        
    

radnik1 = Radnici("Daca")

student1 = Studenti("Nerma", "Zekic", 30)

osoba1 = Osobe("Vahid", "Zekic", 34)
osoba2 = Osobe("Kemo", "Plojovic", 27)

osoba1string = osoba1.ime + " " + osoba1.prezime + " ima godina: " + str(osoba1.godine)
osoba2string = osoba2.ime + " " + osoba2.prezime + " ima godina: " + str(osoba2.godine)


print(osoba1string)
print(osoba2string)



print(student1.ime)