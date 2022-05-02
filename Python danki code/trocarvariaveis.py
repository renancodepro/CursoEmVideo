"""
Exercício - Trocar variáveis

"""

# Trocando variáveis em python

x = input('Digite o valor de x: ')
y = input('Digite o valor de y: ')

# Criaremos uma variável temporaria

temp = x
x = y
y = temp

print(f'O valor de x depois da troca é: {x}')
print(F'O valor de y depois da troca é: {y}')
