while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    for tabuada in range(1, 11):
        print(f'{num} x {tabuada} = {num * tabuada}')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
