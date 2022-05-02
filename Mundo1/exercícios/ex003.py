a = int(input('\033[32mDigite um valor: \033[m'))
b = int(input('\033[31mDigite outro valor: \033[m'))
s = a + b
print(f'A soma entre \033[32m{a}\033[m e \033[31m{b}\033[m', end=" ")
print(f'vale \033[33m{s}\033[m .')
