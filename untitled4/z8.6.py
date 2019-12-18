lista = []

recenica = input()
while recenica:
    lista.append(recenica)
    recenica = input()

for recenica in lista:
    if recenica[-1] == '.' and len(recenica) < 20:
        print(recenica)