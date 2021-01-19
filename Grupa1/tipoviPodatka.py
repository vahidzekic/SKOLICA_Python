var1 = 1
var2 = "text"
lista1 = ["vahid", 65,76]
lista2 = ["Vahid", "Kemo", 4, 6, 6, "Kemo", var1, var2, var2, var2 ]
lista1 = lista2
# print(lista1)
print(lista2)

tuple1 = tuple()
tuple1 = lista2
print(tuple1)

set1 = set()
set1 = ({ 1, 2, 2, 2 , 4, 5, 5 ,5, 5,5, 9, 9 })
set2 = set()
set2.update(lista2)
print(set2)
print(set1)
print(len(set1))

dict1 = dict()
auto = {
    "marka": "BMW",
    "model": "M8",
    "boja": "Crvena",
    "godina": 2020
}

auto["marka"] = "Audi"
auto.update({"godina": 1999 })

# auto["model"] = lista2

auto["sedista"] = 5


autoInfo = str(auto["marka"]) + " " + str(auto["model"]) + " " + str(auto["boja"]) + " " + str(auto["godina"]) + " " + str(auto["sedista"])

print(autoInfo)
print("")

print("Marka: " + str(auto["marka"]))
print("Model: " + str(auto["model"]))
print("Boja: " + str(auto["boja"]))
print("Godina: " + str(auto["godina"]))
print("Sedista: " + str(auto["sedista"]))

lista = [1,2,3,4,5]


JsonObjekat = [
    {
        "godine": 34,
        "id": 1,
        "ime": "Vahid",
        "pol": "muski",
        "prezime": "Zekic"
    },
        {
        "godine": 34,
        "id": 2,
        "ime": "Omer",
        "pol": "muski",
        "prezime": "Ljajic"
    },
        {
        "godine": 34,
        "id": 3,
        "ime": "Kemo",
        "pol": "muski",
        "prezime": "Plojovic"
    }
]

JsonRecnik = {
        "godine": 34,
        "id": 4,
        "ime": "Muhamed",
        "pol": "muski",
        "prezime": "Zukovic"
    }

JsonRecnik.update({'ime': 'Vahid'})

JsonObjekat.append(JsonRecnik)

JsonObjekat[2]['ime'] = 'Vahid'


# print(JsonObjekat[2]['prezime'])



print(JsonObjekat)

