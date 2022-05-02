"""
A porcentagem representa um valor dividido por 100. Dessa forma,
falar 25% de um valor é o mesmo que dizer 25 de 100, ou seja, 25 dividido
por 100.
E, para descobrir o número exato de ausentes no evento, é só multiplicar
o todo pela porcentagem.
Dessa forma: 160 x 25% = 160 (25/100) = 160 x 0,25 = 40

"""

print('DESCUBRA O PREÇO DO SEU PRODUTO NA PROMOÇÃO!!!')
print(30 * " ")
p1 = float(input('Preço atual: R$'))
d = p1 * 0.05
p2 = p1 - d
print(f'Seu produto com 5% de desconto está saindo por: R${p2:.2f}')
