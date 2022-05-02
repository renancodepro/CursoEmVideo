from time import sleep
opção = 4
while opção == 4:
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    print('=' * 20)
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    print('=' * 20)
    while opção != 5:
        opção = int(input('Qual é a sua escolha? '))
        if opção == 1:
            soma = valor1 + valor2
            print(f'A soma de {valor1} + {valor2} é igual a {soma}')
            print('=' * 20)
        elif opção == 2:
            multi = valor1 * valor2
            print(f'O resultado da multiplicação de {valor1} x {valor2} é igual a {multi}')
            print('=' * 20)
        elif opção == 3:
            if valor1 > valor2:
                maior = valor1
                print(f'O maior número entre {valor1} e {valor2} é {maior}')
                print('=' * 20)
            elif valor2 > valor1:
                maior = valor2
                print(f'O maior número entre {valor1} e {valor2} é {maior}')
                print('=' * 20)
            elif valor1 == valor2:
                maior = valor1
                print(f'Os números {valor1} e {valor2} tem o mesmo valor {maior}')
                print('=' * 20)
        elif opção == 4:
            print('Quais números você quer agora? ')
            break
        elif opção == 5:
            print('Finalizando...')
            sleep(1)
            print('Obrigado por usar o nosso programa.')
            print('Volte sempre.')
            print('=' * 20)
        else:
            print('Opção inválida! Tente novamente.')
            print('=' * 20)
