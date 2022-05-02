n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for x in range(n, 0, -1):
    print(x, end=' ')
    print('x ' if x > 1 else '=', end='')
    f *= x
print(f' {f}', end='')
