"""

ANSI
escape sequence
\033[ 'aqui vai o código da cor' m    # o m fecha o codigo
\033[styletextbackm  # estilo da fonte; código do texto; código de fundo
\033[0;33;44m

códigos para estilo que melhor funciona no terminal para python
0 none = sem código nenhum
1 bold = negrito
4 underline = sunblihado
7 negative = inverter as configurações

código de textos  cores de back ground
30 = branco     40
31 = vermelho   41
32 = verde      42
33 = amarelo    43
34 = azul       44
35 = magenta    45
36 = ciano      46
37 = cinza      47

OBS: PESQUISAR COLORRIZE
"""
"""
print('\033[31mOlá mundo')
print('\033[1;34;41mHello, world!\033[m')
"""

nome = 'renan'
print(f'Olá, muito prazer \033[1;36;45m{nome}\033[m ')
