'''for c in range(0, 6):
    print('oi')
print('FIM')

for c in range(6, 0, -1):
    print(c)

for c in range(0, 7, 2):  # contou de 0 ate 6 contando de 2 em 2
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s += n
print(f'A soma dos valores é {s}')
