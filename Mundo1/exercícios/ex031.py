distância = float(input('Qual a distância da sua viagens em Km ? '))
if distância <= 200:
    passagem = distância * 0.50
    print(f'O valor da sua passagem é de R${passagem:.2f}')
else:
    passagem = distância * 0.45
    print(f'O valor da sua passagem é de {passagem:.2f}')
