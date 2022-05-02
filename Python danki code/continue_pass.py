"""
Comando continue e pass

continue - Usado em laços ou estruturas de repetição (for)

pass - usado em estruturas condicionais.(if - else)
"""
"""
for x in range(10):
    if x == 3:
        continue
    print(x)


basicamente é um comando para que agente pare o laço de repetição
atual, e prossiga para o próximo laço de repetição.

"""
"""
pass nós usamos quando queremos aplicar ele em estruturas
condicionais vazias.

"""
for x in range(10):
    if x == 3:
        continue
    print(x)


if x == 5:
    pass  # significado é ignore
print('Olá mundo')

"""

cuidado com uso do pass

não utilizar frequentemente, porque você está gerendo um erro
e falando pro seu comando ignorar o erro.

"""
