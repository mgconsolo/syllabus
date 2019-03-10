from collections import defaultdict

msg = 'supercalifragilisticoespialidoso'

vocales = {'a':0,'e':0,'i':0,'o':0,'u':0}
#Pasamos int como callable. El callable se va a llamar sin parámetros
# cada vez que se consulte por una key que no existe.
# En este caso, int() devolverá el valor por defecto de este tipo (0)

for letra in msg:
    if letra not in 'aeiou': # Revisa si la letra es una vocal
        continue
    vocales[letra] += 1 # si ya existe, agrega una cuenta mas

print(vocales)
