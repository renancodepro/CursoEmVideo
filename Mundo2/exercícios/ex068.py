from random import randint
print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=' * 30)
cont = 0
while True:
    num = int(input('Escolha um número: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = num + computador
    if soma % 2 == 0:
        print(f'Você colocou {num} e o computador {computador}', end=' ')
        print(f'Total de {soma}. Deu PAR')
        if escolha == 'P':
            print('Você VENCEU!!')
            cont += 1
        elif escolha == 'I':
            print('Você PERDEU!!!')
            break
    elif soma % 2 == 1:
        print(f'Você colocou {num} e o computador {computador}', end=' ')
        print(f'Total de {soma}. Deu ÍMPAR')
        if escolha == 'I':
            print('Você VENCEU!!!')
            cont += 1
        elif escolha == 'P':
            print('Você PERDEU!!!')
            break
print(f'GAMER OVER! Você venceu {cont} vezes.')
