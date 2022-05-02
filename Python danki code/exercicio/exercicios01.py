"""

Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado # área = lado ao quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual
será o valor do mesmo com desconto de (??)%.
04 - área de um círculo - pi = 3,141592
05 - conversão de reais para dolar
06 -  conversão de dolar para reais

"""

# Exercício 01 - área do retângulo

"""
print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} unidades de medida')
"""

# Exercício 02 - área de um quadrado

"""
print("Calcule a area de um quadrado.")
lado = input('Qual o tamanho do lado do seu quadrado? ')
area = float(lado) ** 2
print(f'O seu quadrado possui área: {area} unidades de medida')

"""
"""
# Exercício 03 - Se o produto que você quer avaliar custa (??) reais qual
# será o valor do mesmo com desconto de (??)%.

print("Calcule o preço final do seu produto!")

valor_original = float(input("Qual o valor original do seu produto em reais?"))

desconto = float(input("Qual o desconto em (%) para este produto?"))

desconto = desconto / 100

valor_final = valor_original * (1 - desconto)
print(f"O valor final do seu produto eh: R$ {round(valor_final, 2)}")
"""

"""
# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto ganho de 20%
valor_descontado = valor_original * 0.2
# Valor com desconto incluso
novo_valor = valor_original * 0.80

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_descontado)
print('Valor com desconto: R$', novo_valor)
"""


"""
# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto que será concedido
desconto = float( input("Desconto (em %) para esse produto: ") )

# Transformando a porcentagem em número decimal
desconto = desconto / 100

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_original * desconto)
print('Valor com desconto: R$', valor_original * (1-desconto) )

"""

"""
# 04 - área de um círculo - pi = 3,141592
# formula A= pi * raio ao quadradro

print("Calcule a área de um círculo.")
raio = float(input('Qual o tamanho do raio do seu Círculo?'))
pi = 3.141592
area = pi * raio ** 2
print(f'A área do circulo é de : {round(area, 2)}')

"""
"""
# 05 - conversão de reais para dólar


print('Converto de REAL em DÓLAR.')
real = float(input('Quantos reais você quer converter?'))
dolar = 5.65
converçao = real / dolar
print(f'Seus reais valem: {round(converçao, 2)} US$ em dólar')

"""

# 06 -  conversão de dólar para reais

print('Coverta DÓLAR em REAL')
dolar = float(input('Quantos dólares você tem?'))
converçao = dolar / 5.65
print(dolar, 'Dólares' f' valem: {round(converçao, 2)}R$ reais.')
