palavras = ('CAFE', 'CHA', 'PIPOCA', 'TAXI', 'PYTHON',
            'CARRO', 'MAE', 'RENAN', 'PNEU', 'MOTO',
            'BRINCAR', 'COSTELA', 'BIFE')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
