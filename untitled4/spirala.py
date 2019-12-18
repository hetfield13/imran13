def ispisMatrice(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            print(matrica[i][j], end="   ")
        print()

n = int(input())

matrica = []
for i in range(n):
    red = []
    for j in range(n):
        red.append(0)
    matrica.append(red)

indexRedPocetak = 0
indexKolonaPocetak = 0
indexRedKraj = n
indexKolonaKraj = n
brojac = 1
while indexRedPocetak < indexRedKraj and indexKolonaPocetak < indexKolonaKraj:
    for i in range(indexKolonaPocetak, indexKolonaKraj):
        matrica[indexRedPocetak][i] = brojac
        brojac += 1
    indexRedPocetak += 1

    for i in range(indexRedPocetak, indexRedKraj):
        matrica[i][indexKolonaKraj-1] = brojac
        brojac += 1
    indexKolonaKraj -= 1

    for i in range(indexKolonaKraj - 1, indexKolonaPocetak - 1, -1):
        matrica[indexRedKraj-1][i] = brojac
        brojac += 1
    indexRedKraj -= 1

    for i in range(indexRedKraj - 1, indexRedPocetak -1, -1):
        matrica[i][indexKolonaPocetak] = brojac
        brojac += 1
    indexKolonaPocetak += 1

ispisMatrice(matrica)