lista = []

m = int(input())

for i in range(m):
    broj = int(input())
    lista.append(broj)

lista = sorted(lista)

sumaNajmanjih = 0
for i in range(len(lista)//2):
    sumaNajmanjih += lista[i]

sumaNajvecih = 0
for i in range(len(lista)//2, len(lista)):
    sumaNajvecih += lista[i]

print(sumaNajvecih - sumaNajmanjih)