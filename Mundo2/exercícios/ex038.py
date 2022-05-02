PrimeiroNúmero = int(input('Primeiro número: '))
SegundoNúmero = int(input('Segundo número: '))
if PrimeiroNúmero > SegundoNúmero:
    print(f'{PrimeiroNúmero} é maior que {SegundoNúmero}')
elif SegundoNúmero > PrimeiroNúmero:
    print(f'{SegundoNúmero} é maior que {PrimeiroNúmero}')
else:
    print('Os dois valores são iguais.')
