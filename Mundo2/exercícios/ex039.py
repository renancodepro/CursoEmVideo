from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    idade = atual - nasc
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o seu alistamento.')
    print(f'Você deve se alistar no ano de {ano}.')
elif idade > 18:
    idade = atual - nasc
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos')
    print(f'Você deveria ter se alistado no ano de {ano}.')
else:
    print('Você tem que se alistar imediatamente!!!')
