"""
Python - Comandos de controle condicional

if , else e elif -> (else if)

"""
"""
if = se for
else = se não for

# if e elif serão executados sempre que as nossas condições
# anteriores forem
# verdadeiras e o else sempre que forem falsas.

não existe um else sem if e sem elif antes.


"""

"""

x = 8
y = 5

if y > x:
    print('y eh maior do que x')
elif y < x:
    print('y eh menor do que x')
else:
    print('y nao eh menor nem maior que x')
print('Código fora do bloco condicional')
print(y > x)

"""

"""
x = 3
y = 3

if y > x:
    print('y eh maior do que x')
    print('Código dentro do bloco if')
elif y < x:
    print('y eh menor do que x')
elif y == x:
    print('x eh igual a y')

print('Código fora do bloco condicional')
print(y > x)
print(y < x)
print(y == x)
"""

a = 8
b = 5
c = 3

"""
if b > a: print('b eh maior que a')
"""
"""
print('B') if b < a else print('A') # Operador ternário,
# Expressões Condicionais.
"""

if a > b:
    if a > c:
        print('A eh maior que b e c')
