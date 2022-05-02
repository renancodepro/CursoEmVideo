num = int(input('Digite um número para ver sua tabuada de multiplicação: '))
print(f'A tabuada de {num} é :')
for contador in range(1, 11, 1):
    print(f'{num} x {contador:2} = {contador * num}')
