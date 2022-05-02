print('Sequência de fibonacci')
print('=' * 30)
n = int(input('Quantos termos você quer exibir? '))
proximo = 0
anterior = 0
cont = 1
while cont <= n:
    print(proximo, end=' -> ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1
    cont += 1
print('Fim')
