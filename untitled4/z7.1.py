lista = []

for i in range(10):
    broj = int(input())
    lista.append(broj)

for element in lista:
    if element < 0:
        print(element, end=" ")

for element in lista:
    if element == 0:
        print(element, end=" ")

for element in lista:
    if element > 0:
        print(element, end=" ")

