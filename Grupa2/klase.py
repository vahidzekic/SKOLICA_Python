osobeBaza = [
    {
        "id": 1,
        "ime": "Vahid",
        "prezime": "Zekic",
        "godine": 34 
    },
    {
        "id": 2,
        "ime": "Senaid",
        "prezime": "Sarenkapic",
        "godine": 32
    },
    {
        "id": 3,
        "ime": "Enes",
        "prezime": "Daca",
        "godine": 32
    },
        {
        "id": 4,
        "ime": "Ahmed",
        "prezime": "Kavazovic",
        "godine": 32
    }
]

brojClanova = len(osobeBaza)


class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

# osoba1 = Osoba("Vahid", "Zekic", 34)
# osoba2 = Osoba("Senaid", "Sarenkapic", 32)
# osoba3 = Osoba("Enes", "Daca", 32)

osoba1 = Osoba(osobeBaza[0]["ime"], osobeBaza[0]["prezime"], osobeBaza[0]["godine"])
osoba2 = Osoba(osobeBaza[1]["ime"], osobeBaza[1]["prezime"], osobeBaza[1]["godine"])
osoba3 = Osoba(osobeBaza[2]["ime"], osobeBaza[2]["prezime"], osobeBaza[2]["godine"])
osoba4 = Osoba(osobeBaza[3]["ime"], osobeBaza[3]["prezime"], osobeBaza[3]["godine"])

osoba1string = osoba1.ime + " " + osoba1.prezime + " ima godina " + str(osoba1.godine)
osoba2string = osoba2.ime + " " + osoba2.prezime + " ima godina " + str(osoba2.godine)
osoba3string = osoba3.ime + " " + osoba3.prezime + " ima godina " + str(osoba3.godine)
osoba4string = osoba4.ime + " " + osoba4.prezime + " ima godina " + str(osoba4.godine)

print("U bazi podataka se nalazi clanova: " + str(brojClanova))

print(osoba1string)
print(osoba2string)
print(osoba3string)
print(osoba4string)

