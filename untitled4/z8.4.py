lista = []

rijec = input()
while rijec:
    lista.append(rijec)
    rijec = input()

listaSamoglasnika = ['a', 'e', 'i', 'o', 'u']

rezultat = []

for rijec in lista:
    rjesenje = ""
    for slovo in rijec:
        if slovo.lower() not in listaSamoglasnika:
            rjesenje += slovo
    rezultat.append(rjesenje)

print(rezultat)