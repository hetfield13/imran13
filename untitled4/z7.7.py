lista = []

rijec = input()
while rijec:
    lista.append(rijec)
    rijec = input()

prosjek = 0
for rijec in lista:
    prosjek += len(rijec)
prosjek = prosjek // len(lista)

for rijec in lista:
    if len(rijec) > prosjek:
        print(rijec)