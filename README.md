# RETO-11-PDC

Juan Sebastian Martinez Garcia

## 1.Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

### Endswith:
Verifica si una cadena de strings termina en una subcadena de strings determinada retornando un valor booleano.

    texto = "Hola mundo"
    print(texto.endswith("mundo"))  # True
    print(texto.endswith("Hola"))   # False
    
### Startwith:
Verifica si una cadena de strings inicia en una subcadena de strings determinada retornando un valor booleano.

    texto = "Python es genial"
    print(texto.startswith("Python"))  # True
    print(texto.startswith("java"))    # False

### Isalpha
Verifica si TODOS los caracteres del string son alfabéticos y no está vacío retornando un valor booleano.

    print("abc".isalpha())   # True
    print("a1".isalpha())    # False 
    print("".isalpha())      # False

### Isalnum
Verifica si TODOS los caracteres del string son alfanumericos y no está vacío retornando un valor booleano.

    print("abc123".isalnum())  # True
    print("abc 123".isalnum()) # False
    print("123".isalnum())     # True

### Isdigit
Verifica si TODOS los caracteres del string son numericos (enteros) y no está vacío retornando un valor booleano.

    print("123".isdigit())    # True
    print("12.3".isdigit())   # False
    print("abc".isdigit())    # False

### Isspace
Verifica si todos los caracteres son espacios en blanco y no está vacío.

    print("   ".isspace())    # True
    print(" a ".isspace())    # False
    print("".isspace())       # False

### Istitle
Verifica si el string está en formato título (cada palabra comienza con mayúscula).

        print("Este Es Un Título".istitle())  # True
        print("Este no es un título".istitle()) # False

### Islower
Verifica si todos los caracteres alfabéticos están en minúsculas debe haber al menos un carácter alfabético.

    print("hola mundo".islower())  # True
    print("Hola mundo".islower())  # False
    print("123".islower())         # False

### Isupper
Verifica si todos los caracteres alfabéticos están en mayúsculas debe haber al menos un carácter alfabético.

    print("HOLA MUNDO".isupper())  # True
    print("Hola Mundo".isupper())  # False
    print("123".isupper())         # False (no hay letras)



## 2.Procesar el archivo y extraer:

A)Cantidad de vocales

    with open('mbox.txt', 'r') as archivo:
        texto = archivo.read().lower()#Comenzamos leyendo todo el archivo y pasando todas sus letras a minúsculas para que asi se haga más facil contar las vocales.
    
    #Iniciamos un contador
    vocales = 'aeiou'
    contador_vocales = 0
    
    for caracter in texto:
        if caracter in vocales:
            contador_vocales += 1 #Por cada vocal que detecte va a sumar uno al contador de vocales.
    
    print(f'Cantidad total de vocales: {contador_vocales}') #Finalmente imprimimos la cantidad de vocales

B)Cantidad de consonantes

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

C)Listado de las 50 palabras que más se repiten

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


### Resultados
### A)
Cantidad de vocales en el archivo: 1597835
### B)
Cantidad de consonantes en el archivo: 2612121
### C)
Lista de 50 palabras que mas se repiten en el archivo:

from: 21720

by: 18028

received: 16176

with: 12757

id: 12607

nakamurauitsiupuiedu: 10774

dec: 9267

nov: 8988

sourcecollabsakaiprojectorg: 8985

for: 7715

esmtp: 7188

paploouhiacuk: 7188

textplain: 5391

charsetutf8: 5391

gmt: 4941

thu: 4764

to: 4566

tue: 4498

oct: 4164

fri: 4007

mon: 3685

you: 3621

date: 3612

sakai: 3607

murder: 3594

mailumichedu: 3594

cyrus: 3594

lmtpa: 3594

localhost: 3594

postfix: 3594

smtp: 3594

wed: 3518

the: 2544

svn: 2537

log: 2100

site: 1887

modify: 1884

this: 1882

new: 1879

message: 1842

was: 1835

revision: 1833

at: 1824

can: 1822

using: 1821

set: 1814

commit: 1812

my: 1811

notification: 1808

source: 1807

sent: 1802
