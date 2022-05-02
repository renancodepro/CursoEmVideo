"""
from math import floor
import emoji
v = float(input('Digite um valor: '))
print(f'O valor digitado é {v} e sua porção inteira é {floor(v)}')
print(emoji.emojize(':heart_eyes:', use_aliases=True))
# o comando que representa o emoji tem que está dentro de aspas!
"""

v = float(input('Digite um valor: '))
print(f'O valor digitado foi {v} e sua porção inteira é {int(v)}')
# nem sempre é preciso importar biblioteca!
