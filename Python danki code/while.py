"""

Estruturas de repetição   -   loop

while # enquanto
for # para
do while* - não tem em python

obs: break é o comando de parar

"""
"""
a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break
    a = a + 1

print('Resultado final de a:', a)
print(a <= 5)
"""

a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f"a nao eh menor ou igual a 5. valor de a: {a}")
