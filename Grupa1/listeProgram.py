lista = []
print("Prazna lista: " + str(lista))


unos = str(input("Unesite prvi clan liste: " ))
lista.append(unos)
unos = str(input("Unesite drugi clan liste: " ))
lista.append(unos)
unos = str(input("Unesite treci clan liste: " ))
lista.append(unos)

print("Clan je dodat u listu: " + str(lista))




brisanje = str(input("Unesite clan za brisanje: "))
lista.remove(brisanje)


print("Obrisana lista izgleda ovako: " + str(lista))


print("Unesite lokaciju o 0 do ...")
brisanje_lokacije = int(input())
lista.pop(brisanje_lokacije)

print("Obrisana lista izgleda ovako: " + str(lista))