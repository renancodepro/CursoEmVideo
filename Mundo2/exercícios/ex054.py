from datetime import date
atual = date.today().year
adulto = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if atual - nascimento >= 21:
        adulto += 1
    if atual - nascimento < 21:
        menor += 1
print(f'Temos {adulto} maiores de idade e {menor} menores de idade.')
