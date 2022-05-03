'''extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = -1
while num < 0 or num > 20:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Número inválido! Digite novamente: '))
print(f'Você digitou o número {extenso[num]}')'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resposta = 'S'
while resposta in 'Ss':
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[núm]}')
    resposta = str(input('Quer continuar? [S/N]: '))
