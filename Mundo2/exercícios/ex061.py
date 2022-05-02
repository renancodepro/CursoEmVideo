'''print('=' * 40)
print('10 PRIMEIROS TERMOS DE UMA PA!')
print('=' * 40)
first_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = first_termo + (10 - 1) * razão
c = first_termo
while c <= décimo:
    print(c, end=' -> ')
    c += razão
print('Acabou!', end='')'''

print('GERADOR DE PA')
print('=-' * 30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('Fim')
