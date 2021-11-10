prviBroj = 12
drugiBroj = 9
treciBroj = 11

poruka1 = "Prvi broj " + str(prviBroj) + " je manji od drugog broja " + str(drugiBroj) + "."
poruka2 = "Prvi broj " + str(prviBroj) + " je veci od drugog broja " + str(drugiBroj) + "."
poruka3 = "Prvi broj " + str(prviBroj) + " je jednak drugom broju " + str(drugiBroj) + "."

# IF petlja
if (prviBroj < drugiBroj):
    print(poruka1)


# IF ELSE petlja
if (prviBroj < drugiBroj):
    print(poruka1)
else :
    print(poruka2)


# IF ELSE IF ELSE petlja - ELIF petlja
if (prviBroj < drugiBroj):
    print(poruka1)
elif (drugiBroj > treciBroj):
    print(poruka2)
elif (treciBroj > prviBroj):
    print(poruka3)
else:
    print("Ni jedan nije ispunjen.")


# WHILE petlja - koristi se najvishe za izvrshavanje glavnog programa.
i = 0
while i < 10:
    print(poruka2)
    i += 1





# FOR petlja - koristi se najvishe za izlistavanje podataka iz objekata.
JSON = [
    {
    'ime': 'Vahid',
    'prezime': 'Zekic',
    'godina': 1986,
    'pol': 'muski'
},
{
    'ime': 'Enes',
    'prezime': 'Daca',
    'godina': 1988,
    'pol': 'muski'
},
{
    'ime': 'Senaid',
    'prezime': 'Sarenkapic',
    'godina': 1988,
    'pol': 'muski'
},
{
    'ime': 'Mirza',
    'prezime': 'Sarenkapic',
    'godina': 1984,
    'pol': 'muski'
}
]

niz = ["Vahid", "Enes", "Senaid", "Kemo", "Semir", "Kavaz"]
# izcitavanje clanova liste
for clan in niz:
    print(clan)

brojClanova = len(JSON)
print(brojClanova)
# izcitavanje vrednosti objekta iz baze podataka ili JSON objekta
for id in range(0,brojClanova):
    print(JSON[id]["ime"] + " " + JSON[id]["prezime"] + " ima godina " + str(JSON[id]["godina"] ))


