recenica = input()

brojacA = 0
brojacE = 0

for slovo in recenica:
    if slovo.lower() == 'a':
        brojacA += 1
    elif slovo.lower() == 'e':
        brojacE += 1

if brojacA > brojacE:
    print("A")
elif brojacE > brojacA:
    print("E")
else:
    print("AE")