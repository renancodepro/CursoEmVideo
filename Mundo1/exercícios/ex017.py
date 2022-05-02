
"""
from math import sqrt
num = float(input('Comprimento do catento adjacente: '))
num2 = float(input('Comprimento do cateto oposto: '))
a = num ** 2 + num2 ** 2
print(f'O valor da hipotenusa é {sqrt(a):.2f}')

"""
"""
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto'))
hi = (ca ** 2 + co ** 2) ** (1/2)
print(f'O valor da hipotenusa é {hi:.2f}')

"""
"""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa é {hi:.2f}')
"""
