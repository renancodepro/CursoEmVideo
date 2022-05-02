salario = float(input('Qual o sálario atual? '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print(f'Quem recebia R${salario:.2f} com aumento de 10% passa a receber')
    print(f'R${aumento:.2f}')
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
    print(f'Quem recebia {salario:.2f} com o aumento de 15% passa a receber')
    print(f'{aumento:.2f}')
