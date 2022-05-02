from time import sleep
import random
itens = ('Pedra', 'Papel', 'Tesoura', 'Inválido')
pc = random.randint(0, 2)
print('-' * 40)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua escolha? '))
print('JO')
sleep(1)
print('ken')
sleep(1)
print('PO!!!')
print('-' * 40)
print(f'Computador jogou {itens[pc]} e jogador jogou {itens[jogador]}.')
if pc == 0:   # computador jogou pedra
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('Jogador VENCEU!!!')
    elif jogador == 2:
        print('Computador VENCEU!!!')
    else:
        print('Opção INVÁLIDA!!!')
elif pc == 1:  # pc jogou papel
    if jogador == 0:
        print('Computador VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('Jogador VENCEU!!!')
    else:
        print('Opção INVÁLIDA!!!')
elif pc == 2:  # pc jogou tesoura
    if jogador == 0:
        print('Jogador VENCEU!!!')
    elif jogador == 1:
        print('Computador VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
