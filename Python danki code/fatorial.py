"""
Como achar o fatorial de um número

4! == 4*3*2*1
9! == 9*8*7*6*5*4*3*2*1
0! == 1
1! == 1
"""

numero = int(input('Insira um numero:'))

fatorial = 1

if numero < 0:
    print('Nao existe fatorial de numeros negativos')
elif numero == 0:
    print(f'O fatorial de numero {numero} eh 1')
else:
    for x in range(1, numero+1):
        fatorial = fatorial*x
print(f' o fatorial de {numero} eh: {fatorial}')
