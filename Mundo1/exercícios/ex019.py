from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]  # lista sempre estaram entre colchete
escolha = choice(lista)
print(f'O escolhido foi {escolha}')

"""
from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

print(f'O aluno escolhido foi : {choice([a1, a2, a3, a4])}')
"""
