cont = maior = homens = menores = 0
opção = ' '
print('-' * 30)
titulo = 'CADASTRE UMA PESSOA'
print(f'{titulo}')
print('-' * 30)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo in 'MF':
        if sexo in 'F' and idade < 20:
            menores += 1
    if sexo in 'M':
        homens += 1
    opção = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opção in 'N':
        break
print(f'''{maior} pessoas tem mais de 18 anos.
{homens} homens foram cadastrados.
{menores} mulheres tem menos de 20 anos.''')
