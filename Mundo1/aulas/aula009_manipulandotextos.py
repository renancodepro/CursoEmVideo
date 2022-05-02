frase = 'Curso em Video Python'
f2 = frase[9::3]
print(f2)

"""
frase[9:21:2] começa no 9 termina no 20 e mostra de 2 em 2
frase[:5] começa do inicio e para no 4
frase[15:] começa no 15 e vai até o final
frase[9::3] começa no 9 e mostra de 3 em 3

"""
"""

Análise com len() len(frase) mostra o comprimento da frase

count() ex. frase.count('o') vai mostra quantas vezes aparece a
letra 'o' minuscula.

find() frase.find('deo') vai mostrar quantas vezes ele
encontrou 'deo' e onde ele encontrou.

transformações com
replace() frase.replace('Python', 'Android') ele substituiria aonde
tem 'Python' por 'Android'

upper() frase.upper() vai transformar as letras em maiúscula

lower() frase.lower() vai deixar tudo em minùsculo

capitalize() frase.capitalize() vai passar toda a frase para minúscula menos
a primeira letra que ele vai transformar em maiúscula.

title()  frase.title() vai deixar toda primeira letra
das palavras em maiúscula.

strip()  frase.strip() vai remover todo espaço inutil no
começo e no final da sting.
frase.rstip() somente os espaços da direita(RIGTH) serão removidos
frase.lstrip() somente os espaços da esquerda (left) serão removidos

frase.split() ele cria uma lista separando cada palavra
cada palavra se torna uma lista.

junção com join() ' '.join(frase) ele vai juntar as palavras em um frase.


"""

print("""Um texto é uma manifestação da linguagem
Pode ser definido como tudo aquilo que é dito por um
emissor e interpretado por um receptor. """)
