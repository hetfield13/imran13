# Unesi naziv fajla.U fajlu je matrica prirodnih brojeva.
# Nadji elemente ciji je zbir koordinata neparan i ispisi najmanji od tih elemenata

imeFajla = input("Unesi ime fajla: ")


fajl = open(imeFajla, "r")


matrica = []


for red in fajl:
    matrica.append(red.split())

listaNajmanjih = []

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if (i+j) % 2 != 0:
            listaNajmanjih.append(int(matrica[i][j]))


print(min(listaNajmanjih))