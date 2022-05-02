número = int(input("Digite um número inteiro: "))
print('''\nEscolha a Base de Conversão
\nDigite [1] para Binário.\nDigite [2] para Octal.
Digite [3] para Hexadecimal.''')
opção = int(input('Sua opção: '))
if opção == 1:
    binário = str(bin(número))
    print(f'{número} convertido em binário, resulta em: {binário[2:]}')
elif opção == 2:
    octal = str(oct(número))
    print(f'{número} convertido em octal, resulta em: {octal[2:]}')
elif opção == 3:
    hexa = str(hex(número))
    print(f'{número} convertido em hexadecimal, resulta em: {hexa[2:]}')
else:
    print("Opção inválida!!!")
