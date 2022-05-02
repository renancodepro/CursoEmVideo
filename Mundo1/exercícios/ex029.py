v = float(input('digite a velocidade do seu carro em km/h '))
multa = (v - 80) * 7.00
if v > 80:
    print('ATENÇÃO!!!')
    print('=' * 20)
    print('Você está dirigindo acima da velocidade permitida que é de 80km/h.')
    print(f'Você acaba de ser multado em R${multa:.2f} reais.')
print('Você está dentro da velocidade permitida que é 80 km/h. Continue assim.')
