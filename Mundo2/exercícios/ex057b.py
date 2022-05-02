sexo = str(input('Informe seu sexo: [M/F]: '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registradoo com sucesso.')
