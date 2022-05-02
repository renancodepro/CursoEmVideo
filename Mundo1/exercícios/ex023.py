"""
A FORMA QUE EU FIZ

print('Digite um número entre 0 e 9999')
num = int(input('Digite um número:'))
unidade = num % 10
numero = (num - unidade)/10
dezena = numero % 10
numero = (numero - dezena)/10
centena = numero % 10
numero = (numero - centena)/10
milhar = numero
dezena = int(dezena)
centena = int(centena)
milhar = int(milhar)
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')
"""

# professor fez assim
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número... {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centenan: {c}')
print(f'Milhar: {m}')
