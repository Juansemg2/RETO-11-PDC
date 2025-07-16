from collections import Counter
import string# Utilizamos collectiones.counter para contar las palabras más adelante

#Comenzamos leyendo todo el archivo y pasando todas sus letras a minúsculas para que no haya diferencia en ciertas palabras
with open('mbox.txt', 'r') as archivo:
    texto = archivo.read().lower()

translator = str.maketrans('', '', string.punctuation)
texto_sin_puntuacion = texto.translate(translator)# Quitamos los signos de puntuación (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~), esto para eliminar la diferencia que se genera sobre una palabra que tiene signo y una que no, como "hola," no tiene el mismo valor o significado en python que "hola", son diferentes y pueden hacernos cometer errores para sacar nuestro listado

# Utilizamos .split() para dividir las palabras
palabras = texto_sin_puntuacion.split()

# Contamos las ocurrencias de cada palabra
contador_palabras = Counter(palabras)

# utilizamos most_common(x) para obtener las x más repetidas, en este caso las 50 más repetidas
palabras_mas_comunes = contador_palabras.most_common(50)

# Imprimimos el resultado
print("\nLas 50 palabras más frecuentes:")
for palabra, frecuencia in palabras_mas_comunes:
    print(f"{palabra}: {frecuencia}")