n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valror: '))
n3 = int(input('Terceiro valor: '))
maior = n1
menor = n1
#  verificando o quem é o maior
if n2 > maior and n2 > n3:
    maior = n2
if n3 > maior and n3 > n2:
    maior = n3
# verificando quem é o menor
if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n3
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
