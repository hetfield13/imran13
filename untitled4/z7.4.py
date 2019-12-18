lista = []

broj = input()
while broj:
    lista.append(int(broj))
    broj = input()

najmanji = lista[0]
for i in range(len(lista)//2):
    if lista[i] < najmanji:
        najmanji = lista[i]

najveci = lista[-1]
for i in range(len(lista)//2, len(lista)):
    if lista[i] > najveci:
        najveci = lista[i]

for i in range(najmanji, najveci, 2):
    print(i, end=" ")