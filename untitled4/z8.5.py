broj = input()
m = int(input())

#12345

rezultat = ""

for i in range(1, len(broj)+1):
    if i == m+1:
        rezultat = '.' + rezultat
        rezultat = broj[-i] + rezultat
    else:
        rezultat = broj[-i] + rezultat

print(rezultat)