lista = list()
perg = 'Ss'
while perg in 'Ss':
    lista.append(int(input('Digite um valor: ')))
    perg = (input('Quer continuar? [S/N]: '))
lista.sort(reverse=True)
print('=+' * 30)
print(f'Foram digitados {len(lista)} valores.')
print(f'A ordem decrescente é : {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('o valor 5 não foi digitado.')
print('=+' * 30)
