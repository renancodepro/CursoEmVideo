times = ('Corinthians', 'Bragatino', 'Atlético-MG', 'Santos',
         'Coritiba', 'Cuiabá', 'Internacional', 'Avaí', 'América-MG',
         'Palmeiras', 'Flamengo', 'Botafogo', 'São Paulo', 'Fluminense',
         'Ceará SC', 'Athetico-PR', 'Atlético-GO', 'Goiás', 'Juventude',
         'Fortaleza')
print('=' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('=' * 40)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=' * 40)
print(f'Os 4 últimos são: {times[-1:-5:-1]}')
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 40)
print('O Corinthians está em ', end='')
print(times.index('Corinthians') + 1, end='')
print('° Lugar no ranking do Brasileirão serie A.')
