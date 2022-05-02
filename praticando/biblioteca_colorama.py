from colorama import init, Fore, Back, Style
init(autoreset=True)  # não vai permitir que o print que não quero colorido se
# torne colorido.

print(Fore.GREEN + 'Hello, world!')
print('hello, world!')
print(Back.BLUE + 'hello, world!')
print(Back.GREEN + Fore.RED + 'hello, world!')  # tanta a frente(fore)
# como o fundo(back) ficaram coloridos
print('hello,' + Fore.LIGHTBLUE_EX + ' world!')  # apenas o world!
# ficará colorido
print(Style.BRIGHT + 'hello, world!')
