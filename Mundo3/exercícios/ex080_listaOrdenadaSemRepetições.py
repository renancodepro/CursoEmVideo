números = list()
for c in range(1, 6):
    n = int(input(f'Digite o {c}ª valor: '))
    if c == 1 or n >= números[-1]:
        números.append(n)
    elif n <= números[0]:
        números.insert(0, n)
    elif números[0] <= n <= números[1]:
        números.insert(1, n)
    elif números[1] <= n <= números[2]:
        números.insert(2, n)
    elif números[2] <= n <= números[3]:
        números.insert(3, n)
print(números)


# professor fez assim:
lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
