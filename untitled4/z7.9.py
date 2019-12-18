brojevi = input()

lista = brojevi.split(' ')
for i in range(len(lista)):
    lista[i] = int(lista[i])

brojac = 0
for i in range(1, len(lista)):
    if lista[i] > lista[i-1]:
        brojac += 1

print(brojac)

brojacVecih = 0
for i in range(len(lista)-1):
    suma = 0
    for j in range(i+1, len(lista)):
        if lista[j] > 0:
            suma += lista[j]
    if lista[i] > suma:
        brojacVecih += 1

print(brojacVecih)
