"""
01 - Implemente um programa que receba a idade de uma pessoa e imprima
a mensagem de acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR

"""
"""
x = 16
z = 18

idade = float(input("Digite sua idade!"))
if idade < x:
    print("MENOR DE IDADE")
elif idade > z:
    print("MAIOR DE IDADE")
elif idade >= x <= z:
    print("EMANCIPADO")
"""

"""
02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:

infantil A  5 - 7 anos
infantil B  8 - 10 anos
juvenil A   11 - 13 anos
juvenil B   14 - 17 anos

"""
w = 5, 6, 7
x = 8, 9, 10
y = 11, 12, 13
z = 14, 15, 16, 17

print('descubra sua categoria aqui!')
idade = float(input('Digite sua idade'))
if idade in w:
    print('Infantil A')
elif idade in x:
    print('Infantil B')
elif idade in y:
    print('Juvenil A')
elif idade in z:
    print('Juvenil B')
