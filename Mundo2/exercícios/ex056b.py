somaidade = 0
médiaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'-----{p}°PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
