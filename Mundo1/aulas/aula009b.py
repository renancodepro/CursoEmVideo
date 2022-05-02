frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))  # no python pode juntar comandos, aqui estou
# mandando contar quantas vezes tem o 'O'
# maiusculo em uma frase que mandei ser jogada para maiuculo.

frase = 'Curso em Video Python'
frase = frase.replace('Python', 'Android')
print(frase)

frase = 'Curso em Video Python'
print('Curso' in frase)

frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0][2])  # pega o individo 0 e me mostra a letra 2
