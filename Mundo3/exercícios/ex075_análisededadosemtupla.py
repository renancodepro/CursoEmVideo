#  fiz assim
'''num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Outro valor: '))
num4 = int(input('Digite o último valor: '))
números = (num1, num2, num3, num4)
print(f'Você digitou os valores: {números}')
print(f'O número 9 aparece {números.count(9)} vezes.')
print(f'O número 3 apareceu na {números.index(3) + 1}ª posição.')
print('Os valores pares digitados foram: ', end='')
if num1 % 2 == 0:
    print(num1, end=' ')
if num2 % 2 == 0:
    print(num2, end=' ')
if num3 % 2 == 0:
    print(num3, end=' ')
if num4 % 2 == 0:
    print(num4, end=' ')'''

#  professor fez assim

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9,)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
