lista = []

rijec = input()
while rijec:
    lista.append(rijec)
    rijec = input()

for element in lista:
    if element[0].lower() != 'b':
        print(element, end=" ")