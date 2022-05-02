"""
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
menor = a
maior = a
medio = a
if b <= menor and b <= c:
    menor = b
if c <= b and c <= menor:
    menor = c
if b >= maior and b >= c:
    maior = b
if c >= maior and c >= b:
    maior = c
if medio <= b and b <= c:
    medio = b
if medio <= c and c <= b:
    medio = c
if medio >= b and b >= c:
    medio = b
if medio >= c and c >= b:
    medio = c
if menor + medio > maior:
    print('As retas definidas PODEM formar um triângulo? ')
else:
    print('As retas definidas NÃO podem formar um triângulo? ')
"""
print('-=' * 20)
print('Analisandor de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
