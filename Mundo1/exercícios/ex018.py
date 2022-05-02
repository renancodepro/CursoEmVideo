import math
a = float(input('Digite um ângulo: '))
coseno = math.cos(math.radians(a))
seno = math.sin(math.radians(a))
tang = math.tan(math.radians(a))
print(f'O ângulo de {a} tem o seno de {seno:.2f} ')
print(f'O ângulo de {a} tem o coseno de {coseno:.2f} ')
print(f'O ângulo de {a} tem a tangente de {tang:.2f} ')
