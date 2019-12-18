lista = []

grad = input()
while grad:
    lista.append(grad)
    grad = input()

brojacS = 0
for grad in lista:
    if grad[0].lower() == 's':
        brojacS += 1

brojacB = 0
for grad in lista:
    if grad[0].lower() == 'b':
        brojacB += 1

if brojacS > brojacB:
    for grad in lista:
        if grad[0].lower() == 's':
            print(grad, end=" ")
elif brojacB > brojacS:
    for grad in lista:
        if grad[0].lower() == 'b':
            print(grad, end=" ")
else:
    for grad in lista:
        if grad[0].lower() == 's' or grad[0].lower() == 'b':
            print(grad, end=" ")