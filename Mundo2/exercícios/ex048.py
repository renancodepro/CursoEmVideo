soma = 0
cont = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        cont += 1
        soma += + m
print(f'A soma de todos os {cont} valores solicitados é {soma}')
