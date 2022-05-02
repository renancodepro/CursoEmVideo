opção = 'S'
cont = soma = maior = menor = 0
while opção == 'S':
    núm = int(input('Digite um número inteiro: '))
    cont += 1
    soma += núm
    opção = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opção == 'S':
        maior = núm
        menor = núm
    elif núm > maior:
        maior = núm
    elif núm < menor:
        menor = núm
média = soma / cont
print(f'''Você digitou {cont} números e a média entre eles é de {média:.2f}
o maior é {maior} e o menor é {menor}''')
