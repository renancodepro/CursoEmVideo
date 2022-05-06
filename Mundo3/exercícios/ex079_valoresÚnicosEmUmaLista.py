# eu fiz assim
lista_unica = list()
resposta = 'Ss'
while resposta not in 'Nn':  # enquanto a resposta for sim ele vai continuar.
    valor = int(input('Digite um valor: '))
    if valor in lista_unica:  # se valor já estiver em lista
        print('Valor duplicado! Não adicionado...')
    else:
        lista_unica.append(valor)  # adiciona valor a lista
        print('Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar? [S/N]: '))
# organiza em ordem crescente a lista
print(f'Você digitou os valores {sorted(lista_unica)}')

# professor fez assim:

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-+' * 30)
números.sort()
print(f'Você digitou os valores {números}')
