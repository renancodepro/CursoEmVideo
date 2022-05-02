print('=' * 40)
print('10 TERMOS DE UMA PA')
print('=' * 40)
primeiro = int(input('Digite primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão
for pa in range(primeiro, décimo + razão, razão):
    print(pa, end=' -> ')
print('ACABOU.')
