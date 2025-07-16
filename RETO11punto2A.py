with open('mbox.txt', 'r') as archivo:
    texto = archivo.read().lower()#Comenzamos leyendo todo el archivo y pasando todas sus letras a minúsculas para que asi se haga más facil contar las vocales.

#Iniciamos un contador
vocales = 'aeiou'
contador_vocales = 0

for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1 #Por cada vocal que detecte va a sumar uno al contador de vocales.

print(f'Cantidad total de vocales: {contador_vocales}') #Finalmente imprimimos la cantidad de vocales