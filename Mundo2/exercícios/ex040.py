nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Quem tirou nota {nota1:.1f} e {nota2:.1f} tem média {média:.1f}')
if média >= 7.0:
    print('Aluno foi APROVADO!!!')
elif média < 5.0:
    print('Aluno está REPROVADO!!!')
elif média >= 5.0 and média <= 6.9:
    print('Aluno em RECUPERAÇÃO')
