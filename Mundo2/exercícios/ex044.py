print(f'{"Lojas Renans":=^40}')
valor = float(input('Valor das compras: R$'))
print('-' * 20)
print('''ESCOLHA A FORMA DE PAGAMENTO.
[1] – à vista dinheiro/cheque: 10% de desconto
[2] – à vista no cartão: 5% de desconto
[3] – em até 2x no cartão: preço normal
[4] – 3x ou mais no cartão: 20% de juros''')
opção = int(input('Digite a sua opção: '))
print('-' * 20)
if opção == 1:
    valorFinal = valor * 90 / 100
elif opção == 2:
    valorFinal = valor * 95 / 100
elif opção == 3:
    valorFinal = valor
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
elif opção == 4:
    valorFinal = valor + (valor * 20 / 100)
    par = int(input('Quantas parcelas você deseja? '))
    parcela = valorFinal / par
    print(f'Sua compra será parcelada em {par} vezes de R${parcela:.2f} com juros.')
else:
    valorFinal = valor
    print('Opção de pagamento INVÁLIDA. tente novamente.')
print(f'''A sua compra de R${valor:.2f} na forma de pagamento escolhida,
vai custar R${valorFinal:.2f} no final.''')
