valor_casa = float(input('Qual o valor da casa? '))
sálario = float(input('Qual o valor do seu sálario? '))
anos = int(input('Em quantos anos pretende parcelar a comprar da casa? '))
porcentagem = sálario * 30 / 100
parcela = valor_casa / (anos * 12)
if parcela <= porcentagem:
    print('PARABÉNS!!!! \nSeu emprestimo foi APROVADO com sucesso.')
    print(f'A parcela da sua casa ficou de R${parcela:.2f}')
else:
    print('Seu emprestimo foi \033[31mNEGADO\033[m')
    print(f'A parcela da sua casa ficaria no valor de {parcela:.2f}')
    print('A parcela excedeu 30 por cento do seu sálario!')
