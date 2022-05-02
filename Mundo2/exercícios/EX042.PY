print('-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-' * 20)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('Equilátero.')
    elif reta1 != reta2 != reta3 and reta1 != reta3:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
