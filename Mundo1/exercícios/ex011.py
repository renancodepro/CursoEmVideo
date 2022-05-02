altura = float(input('Altura da parede em metros: '))
largura = float(input('Comprimento em metros da parede: '))
m2 = altura * largura
litros = m2 / 2
print(f'Sua parede tem {m2} metros². ')
print(f'Para pintar essa parede você precisará de {litros} litros de tinta')
