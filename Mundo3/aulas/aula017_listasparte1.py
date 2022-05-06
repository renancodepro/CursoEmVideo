'''valores = [5, 8, 2, 1]
valores.sort()  # deixa a lista em ordem
print(valores)'''

'''num = [2, 5, 9, 1]
num[2] = 3  # troca o número que está na chave 2 pelo valor 3
num.append(7)  # inseri no final da lista mais um número que no caso é o 7
num.sort()   # coloca em ordem a minha lista
num.sort(reverse=True)  # coloca em ordem reversa a lista
num.insert(2, 0)  # na posição 2 insira o valor 0
num.pop()  # elimina o último valor
num.pop(2)  # remove o valor que estiver na posição 2
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''num = [2, 5, 9, 1]
num[2] = 3  # troca o número que está na chave 2 pelo valor 3
num.append(7)  # inseri no final da lista mais um número que no caso é o 7
num.sort()   # coloca em ordem a minha lista
num.sort(reverse=True)  # coloca em ordem reversa a lista
num.insert(2, 2)
num.remove(2)  # remove o valor dois da lista. Porém se tiver mais de um 2
# ele só removera o primeiro 2
if 4 in num:  # o 4 não está na lista então se o remove for usando
    num.remove(4)  # isolado para isso gera um erro.
else:
    print('Não achei o número 4')
print(num)'''

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# inseri valores à lista pelo teclado ^

'''valores.append(5)  # adiciona o valor a lista
valores.append(9)
valores.append(4)'''

'''for v in valores:
    print(f'{v}...', end='')'''

for c, v in enumerate(valores):  # enumerate pega tanto a chave quanto o valor
    print(f'Na posição {c} está o valor {v}')
print('cheguei ao final da lista.')

a = [2, 3, 4, 7]
# b = a # cria uma ligação entre b e a, e qualquer auteração em uma lista afeta a outra
b = a[:]  # pega todos os valores de a e copia em b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
