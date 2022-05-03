# forma que eu fiz
'''from random import sample
num = sample(range(10), 5)  # sorteia números inteiros na quant descrita
print(f'os números sortados foram: {num}')
maior = (sorted(num)[4])  # encontando o maior
menor = (sorted(num)[0])  # encontrando o menor
print(f'O maior número sorteado foi {maior}')
print(f'O menor núemro sorteado foi {menor}')'''

# forma que o professor fez
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10))  # sorteia 5 números
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')  # imprime os valores
print(f'\nO maior valor sorteado foi {max(numeros)}')  # encontra o maior núm
print(f'O menor valor sorteado foi {min(numeros)}')  # encontra o menor núm
