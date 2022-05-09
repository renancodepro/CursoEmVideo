num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar: [S/N]: ')
    if resp in 'Nn':
        break
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
