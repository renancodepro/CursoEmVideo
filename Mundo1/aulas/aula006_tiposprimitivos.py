"""
int - números inteiros
7 , -4 , 0 , 9875

float - números reais ou números de ponto flutuantes
4.5 , 0.076 , -15.223 , 7.0

bool - valores lógicos ou boleanos
True , False

str - valores caracteres ou strings
'Olá' , '7.5' , ''


"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}.')

print(f'A soma entre {n1} e {n2} vale: {s} .')
# print('A soma entre {0} e {1} vale: {2}'.format(n1, n2, s))
