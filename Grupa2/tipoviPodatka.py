broj = 89                       # Intiger
stringovi = 'Ja ucim Python'    # String
bolian = False
bolian = True                   # Bulian


lista = []
lista = ['Vahid', 'Enes', 'Senaid']
lista = ['Vahid', 34, True, 'Enes', 'Senaid', 199, 199, 'Enes', 'Vahid']

# brishe elemenat liste po imenu elementa
lista.remove('Vahid') 

# brishe elemenat liste po id-u
lista.pop(1)

# dodaje elemenat na kraj liste
lista.append('Auto')

# dodaje elemenat na odredjenju poziciju
lista.insert(1, 'Vahid')

# menja element lista na odredjenoj poziciji
lista[4] = 'Avion'

print(lista)


lista1 = []
lista1 = list()


# tuple1 = ()
tuple1 = tuple()
tuple1 = (1, 2, 3)

# set1 = {}
set1 = set()
set1 = {1, 1, 1, 4, 4, 4 , 5, 5, 5}
set1 = set(lista)


dict1 = {}
dict1 = dict()
dict1 = {
    'ime': 'Vahid',
    'prezime': 'Zekic',
    'godina': 1986,
    'pol': 'muski'
}


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
}
]

print(JSON[2]['prezime'])