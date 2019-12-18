lista = []

broj = input()
while broj:
    lista.append(int(broj))
    broj = input()

zadnjiBroj = lista[-1]
zadnjaCifra = zadnjiBroj % 10
prvaCifra = zadnjiBroj // 10

obrnutZadnji = zadnjaCifra*10 + prvaCifra

nalaziSe = False
for broj in lista:
    if broj == obrnutZadnji:
        nalaziSe = True

if nalaziSe:
    print("DA")
else:
    print("Ne")