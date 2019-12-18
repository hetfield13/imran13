fajl = open('test01.in', 'r')

matrica = []

red = fajl.readline()
while red != '':
    podaci = red.split()
    for i in range(len(podaci)):
        podaci[i] = float(podaci[i])
    matrica.append(podaci)
    red = fajl.readline()

suma = 0
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        suma += matrica[i][j]

print(suma)