fajl = open('test03.in', 'r')

lista1 = []
lista2 = []
lista3 = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    print(podaci)
    if podaci[2] == '1':
        lista1.append(podaci[0] + " " + podaci[1])
    elif podaci[2] == '2':
        lista2.append(podaci[0] + " " + podaci[1])
    elif podaci[2] == '3':
        lista3.append(podaci[0] + " " + podaci[1])
    red = fajl.readline()
for element in lista1:
    print(element)
print()

for element in lista2:
    print(element)
print()

for element in lista3:
    print(element)