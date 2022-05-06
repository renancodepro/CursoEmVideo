lista = []
for pos in range(0, 5):
    # adiciona a lista
    lista.append(int(input(f'Digite um valor na posição {pos}: ')))
maior = max(lista)
menor = min(lista)
print('-=' * 30)
print(f'Você digitou os valores: {lista}')
#  encontra o maior
print(f'Maior valor digitado foi: {maior} nas posições: ', end='')
for c, valor in enumerate(lista):  # enumera a posição de cada valor
    if valor == maior:
        print(f'{c}... ', end='')
# encontra o menor valor
print(f'\nMenor valor digitado foi: {menor} nas posições: ', end='')
for c, valor in enumerate(lista):
    if valor == menor:
        print(f'{c}... ', end='')
print('\n')
print('-=' * 30)
