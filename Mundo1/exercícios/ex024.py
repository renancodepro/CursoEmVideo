"""
FIZ ASSIM

c = str(input('Em que cidade você nasceu? ')).strip()
c = c.strip()
c = c.title()
lista = c.split()
print('Santo' in c)
"""
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
