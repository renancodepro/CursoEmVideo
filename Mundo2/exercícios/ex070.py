totCompra = produtosM1000 = menorP = 0
produtoMbarato = ' '
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    resp = ' '
    totCompra += preço
    produtoMbarato = produto
    menorP = preço
    if preço > 1000:
        produtosM1000 += 1
    if preço < menorP:
        menorP = preço
        produtoMbarato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da sua compra foi de {totCompra:.2f}')
print(f'Produtos que custaram mais de 1000 foram {produtosM1000} no total ')
print(f'O produto mais barato foi o ou a {produtoMbarato}')
