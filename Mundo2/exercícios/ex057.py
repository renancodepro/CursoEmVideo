sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'F' and sexo != 'M':
        print('Inválido! Por favor digite novamente.')
    else:
        print(f'Sexo {sexo} registrado com sucesso.')
