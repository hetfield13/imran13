n = int(input())

lista = []
for i in range(n):
    rijec = input()
    lista.append(rijec)

rezultat = []
for i in range(n):
    if i == 0:
        rezultat.append(lista[i])
    else:
        if len(lista[i]) % 2 == 1:
            veciOdSvih = True
            for j in range(i):
                if len(lista[j]) > len(lista[i]):
                    veciOdSvih = False
            if veciOdSvih:
                rezultat.append(lista[i])
        else:
            manjiOdSvih = True
            for j in range(i):
                if len(lista[j]) < len(lista[i]):
                    manjiOdSvih = False
            if manjiOdSvih:
                rezultat.append(lista[i])
print(rezultat)