lista = []

n = int(input())

for i in range(n):
    broj = int(input())
    lista.append(broj)

lista = sorted(lista)
m = int(input())
print(lista[m:-m])