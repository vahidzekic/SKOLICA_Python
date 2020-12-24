broj = 4
text = "Vahid"
bolian = True

ime1 = "Vahid" 
ime2 = "Moke"
ime3 = "Omer"
ime4 = "ZMZUKO"

prazna_lista = []

mojaLista = [ime1, ime2, ime3, ime4]
mojaLista = ["Vahid", "Moke", "Omer", "ZMZUKO"]
mojaLista = [1, 2, 4, 5, 6]
mojaLista = [True, False, False, True]

mojaLista.append(9) #DODAVANJE CLANA U LISTU
mojaLista.remove("Vahid") #BRISANJE CLANA IZ LISTE
mojaLista.pop(0) #BRISANJE CLANA IZ LISTE POZICIJOM
del mojaLista[2] #BRISANJE CLANA IZ LISTE POZICIJOM

mojaLista.clear() #BRISANJE CELE LISTE

mojaLista[0] = "Zamo" #ZAMENA CLANA NA ODREDJENU LOKACIJU


print(mojaLista)

# LISTANJE PREKO FOR PETLJE
mojaLista = ["Vahid", "Moke", "Omer", "ZMZUKO"]
for imena in range(len(mojaLista)):
    print(mojaLista[imena])
