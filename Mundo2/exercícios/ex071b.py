c50 = c20 = c10 = c1 = 0
print('{:-^40}'.format('BEM-VINDO AO SEU BANCO'))
while True:
    saque = int(input('Quanto você quer sacar? '))
    c50 = int(saque / 50)
    c20 = int((saque - (c50 * 50)) / 20)
    c10 = int((saque - ((c50 * 50) + (c20 * 20))) / 10)
    c1 = int(saque - ((c50 * 50) + (c20 * 20) + (c10 * 10)))
    if c50 != 0:
        print(f'Total de {c50} cédulas de R$50')
    if c20 != 0:
        print(f'Total de {c20} cédulas de R$20')
    if c10 != 0:
        print(f'Total de {c10} cédulas de R$10')
    if c1 != 0:
        print(f'Total de {c1} cédulas de R$1')
    break
print('=' * 40)
print('Volte sempre!')
