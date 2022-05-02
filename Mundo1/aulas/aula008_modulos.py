"""
import - mais módulo importará todas as funcionalidade do módulo

from - mais modulo-  import -  funcionalidade importará apenas as
funcionalidades que eu escolher

biblioteca matemática - math

ceil - faz um arrendondamento para cima
floor - arredondamento para baixo
trunc - elimina da vírgula para frente
pow - calcula a potencia
sqrt - calcular raiz quadrada
factorial - calcular fatorial
hypot - calcula a hipotenusa

import match - vai importar todas as funcionalidades

from math import sqrt - vai importa somente a sqrt
from math import sqrt, ceil - importa as duas

"""
"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')  # arredondando para cima
print(f'A raiz de {num} é igual a {math.floor(raiz)}')  # ''  ''  ''para baixo
print(f'A raiz de {num} é igual a {raiz:.2f}')  # sem arredondar apenas com
# duas casa decimais depois do ponto.
"""
"""
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')


import emoji
print(emoji.emojize('Olá, mundo :sunglasses:', use_aliases=True))

"""
