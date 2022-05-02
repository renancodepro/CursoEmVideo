"""
Como descobrir se um número é impar ou par
"""

print(30 * '-')
while True:
    numero = int(input('Insira um numero para saber se o mesmo eh par ou impar:'))
    if (numero % 2) == 0:
        print(f'{numero} eh um numero par')
    else:
        print(f'{numero} eh um numero impar')
print(30 * '-')
