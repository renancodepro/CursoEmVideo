expre = input('Digite uma expressão algébrica com parênteses: ')
cont = 0
for c in expre:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
    # se o contador é negativo, foi encontrado um ')' sem '(' correspondente
    if cont < 0:
        break  # sai do for
if cont == 0:
    print('A sua expressão é válida.')
else:
    print('Sua expressão inválida.')

# professor fez assim:

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
