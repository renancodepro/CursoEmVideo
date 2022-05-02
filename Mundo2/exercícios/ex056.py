soma = 0
velho = '0'
maior = 0
menos = 0
for c in range(1, 5):
    print(f'-----{c}° Pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: M/F ')).strip().upper()
    soma += idade
    if sexo == 'M':
        if idade > maior:
            velho = nome
            maior = idade
    elif sexo == 'F' and idade < 20:
        menos += 1
print(f'''A média de idade do grupo é de {soma / 4 :.1f}
O homem mais velhor se chama {velho} e têm {maior}anos de idade.
E {menos} mulheres têm menos de 20 anos.''')
