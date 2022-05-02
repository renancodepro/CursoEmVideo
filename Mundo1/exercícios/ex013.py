
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 15 / 100
novo = aumento + salario
print(F'O funcionário receberá com o aumento de 15% o valor de R${novo:.2f}')
