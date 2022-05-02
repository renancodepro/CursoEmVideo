'''n = soma = c = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    soma += n
    c += 1
print(f'Você digitou {c - 1} números e a soma deles é {soma - 999}')'''

n = soma = c = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {c} números e a soma deles é {soma}')
