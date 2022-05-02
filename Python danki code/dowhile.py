"""
do while

Código para adivinhar um número

"""

palpite = 0
numero = 9

while True:  # nós executamos sem verificar
    print('Qual o numero correto? ')
    palpite = int(input())
    if palpite == numero:  # Estamos verificando nosso código
        print('Parabens voce acertou')
        break
    else:
        print('Voce errou')
else:
    print('Erro na aplicacao')  # Linhas de códigos para teste, não esquecer de
    print(bool(palpite))  # retirar linhas de teste antes de ir para o ar
# quando for fazer trabalhos futuros.
