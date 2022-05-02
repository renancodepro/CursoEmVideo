frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(" ", "")
print(f'A frase digitada ao contrário é {frase[::-1]}')
if str(frase) == str(frase)[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
