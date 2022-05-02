from random import randint
from time import sleep
contador = 1
computer = randint(0, 10)  # faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
while player != computer:
    if player < computer:
        print('Mais... tente mais uma vez!')
        player = int(input('Qual o seu palpite? '))
    elif player > computer:
        print('Menos... Tente novamente! ')
        player = int(input('Qual o seu palpite? '))
    contador += 1
print('PROCESANDO...')
sleep(2)
print()
if player == computer:
    print('PARABÉNS! Você conseguiu me vencer!')
print(f'Levou {contador} rodadas para isso.')
