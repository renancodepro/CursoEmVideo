x = 16
z = 18

idade = float(input("Digite sua idade!"))
if idade < x:
    print("MENOR DE IDADE")
elif idade > z:
    print("MAIOR DE IDADE")
elif idade >= x <= z:
    print("EMANCIPADO")
