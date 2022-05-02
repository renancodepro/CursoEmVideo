from random import randint
from time import sleep
computer = randint(0, 5)  # faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
print('PROCESANDO...')
sleep(2)
if player == computer:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computer} e não no {player} ')


"""
import random
print('Tente adivinhar o número que o computador pensou.')
print(" " * 30)
n = random.randint(0, 5)
num = int(input('Digite seu palpite: '))
if num == n:
    print('Parabéns, você VENCEU!')
else:
    print('Você PERDEU!')

"""
