dia = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km percorridos? '))
pd = dia * 60.00
pk = km * 0.15
pfinal = pd + pk
print(f'O total a pagar é de {pfinal:.2f}')
