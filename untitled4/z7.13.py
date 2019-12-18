brojevi = input()

lista = brojevi.split(' ')
for i in range(len(lista)):
    lista[i] = int(lista[i])

for i in range(1, len(lista)-1):
    if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
        indexNajmanjegLokalnogMax = i
        break

for i in range(len(lista)-2, 1, -1):
    if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
        indexNajvecegLokalnogMax = i
        break

print(indexNajvecegLokalnogMax - indexNajmanjegLokalnogMax + 1)