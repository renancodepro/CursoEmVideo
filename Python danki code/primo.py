"""
Descobrir se um número é primo

O Que é um número primo?
É Um número que só pode ser dividido por 1 e por ele mesmo.

"""

print(30 * "-")

numero = int(input("Insira um numero para descobrir se o mesmo é primo:"))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Esse não é primo")
            break
    else:
        print("Esse número é primo:")
else:
    print('Esse número é primo: numero menor ou igual a 1')


print(30 * "-")
