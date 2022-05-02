times = ('Corinthians', 'Bragatino', 'Atlético-MG', 'Santos',
         'Coritiba', 'Cuiabá', 'Internacional', 'Avaí', 'América-MG',
         'Palmeiras', 'Flamengo', 'Botafogo', 'São Paulo', 'Fluminense',
         'Ceará SC', 'Athetico-PR', 'Atlético-GO', 'Goiás', 'Juventude',
         'Fortaleza')
print('=' * 40)
print(f'Lista de times do Brasileirão: {times}')  # mostra a lista dos times
'''for t in times:
    print(t)
print('=' * 40)'''  # escreve a lista em coluna
print(f'Os 5 primeiros são: {times[0:5]}')  # mostra os 5 primeiros da tupla
print('=' * 40)
print(f'Os 4 últimos são: {times[-4:]}')  # mostra os 4 últimos da tupla
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')  # tupla em ordem alfabé.
print('=' * 40)
print(f'O Corinthians está em {times.index("Corinthians") + 1}'
      'ª no Ranking do Brasileirão serie A.')  # localiza o termo dentro da t.
