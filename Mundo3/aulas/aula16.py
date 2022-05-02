'''lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
print(lanche[1:3])

lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
print(lanche[-2])'''

# Tuplas são imutáveis

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(len(lanche))
'''
'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(cont)'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(lanche[cont])'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('comi pra caramba!')'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('comi pra caramba!')'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('comi pra caramba!')'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('comi pra caramba!')'''

'''lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

print(sorted(lanche))
print(lanche)'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(b)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a + b)'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))  # quantos 5 tem na tupla c

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.index(8))  # posição de 8 NA TUPLA c '''

pessoa = ('Gustavo', 39, 'M', 89.88)
del(pessoa)  # deleta a tupla
print(pessoa)
