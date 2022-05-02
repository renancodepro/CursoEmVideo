número = int(input('Digite um número: '))
mult = 0
for count in range(1, número + 1):
    if número % count == 0:
        print('Divisível por ', count)
        mult += 1
if (mult == 2):
    print('É primo')
else:
    print('Não é primo.')
