import json
from klase import osobeBaza

nasaLista = []
with open("podaci.json") as ucitajPodatkeJson:
    nasaLista = json.load(ucitajPodatkeJson)
print("Nasa lista ima podatke: " + str(nasaLista))

# UNOS PODATAKA U LISTU PREKO KORISNICKOG INPUTA
unos = input("Unesite prvi clan liste: " )
nasaLista.append(unos)
unos = input("Unesite drugi clan liste: " )
nasaLista.append(unos)
unos = input("Unesite treci clan liste: " )
nasaLista.append(unos)
unos = input("Unesite cetvrti clan liste: " )
nasaLista.append(unos)
with open("podaci.json", "w") as sacuvajPodatakaJson:
    json.dump(nasaLista, sacuvajPodatakaJson)
print(nasaLista)


# BRISANJE PODATAKA IZ LISTE PREKO INPUTA
brisanje = input("Unesite clan za brisanje: ")
nasaLista.remove(brisanje)

# UNOS PODATAKA U LISTU IZ KLASE
unos = int(input("Unesite prvi clan klase: " ))
nasaLista.append(osobeBaza[unos]["ime"])
unos = int(input("Unesite drugi clan klase: " ))
nasaLista.append(osobeBaza[unos]["ime"])
unos = int(input("Unesite treci clan klase: " ))
nasaLista.append(osobeBaza[unos]["ime"])
unos = int(input("Unesite cetvrti clan klase: " ))
nasaLista.append(osobeBaza[unos]["ime"])
with open("podaci.json", "w") as sacuvajPodatakaJson:
    json.dump(nasaLista, sacuvajPodatakaJson)
print(nasaLista)


