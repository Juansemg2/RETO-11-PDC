with open('mbox.txt', 'r') as archivo:
    texto = archivo.read().lower()  #Comenzamos leyendo todo el archivo y pasando todas sus letras a minúsculas para que asi se haga más facil contar las consonantes.

# En este codigo al igual que en el anterior vamos a definir las vocales para luego excluirlas de resultado final.
vocales = 'aeiou'

# Iniciamos un contador de consonantes
contador_consonantes = 0

# Empezamos a contar con .isalpha los caracteres que son letras, por cada letra que detecte va a sumar uno al contador de consonantes, y le pedimos que excluya las vocales dejando asi solo las consonantes
for caracter in texto:
    if caracter.isalpha() and caracter not in vocales:
        contador_consonantes += 1

print(f'Cantidad total de consonantes: {contador_consonantes}')#Finalmente imprimimos la cantidad de consonantes