# Built-in Functions

### open("archivo.csv", "r", encoding="utf-8")
- Abre el archivo en modo lectura
- "r" significa lectura
- "a" significa escritura con persistencia de datos
- "utf-8" es para que no haya problemas con los acentos
- "w" es una forma de escribir en un archivo, pero borraría todo el contenido dejandolo en blanco antes de escribir.
-

### csv.DictReader(archivo)
- Lee el archivo y lo convierte en una lista de diccionarios (Lo cual para nuestro caso funcionaría como un archivo)
- Las columnas se guardan como claves y los valores se guardan como valores

### len(texto)
- Devuelve la longitud del texto

### ljust(numero)
- Deja el texto a la izquierda y rellena el espacio sobrante con " "

### rjust(numero)
- Deja el texto a la derecha y rellena el espacio sobrante con " "


## Importante
En mi solucion propuesta, damos por hecho que existe un archivo
animales.csv con al menos la cabecera.
Esto se hace así para evitar confusiones con la escritura del archivo, si se desea crear el script sin el archivo de cabecera, se deberá incluir la librería os y verificar si existe antes
Esto agregaría una complejidad innecesaria para una situación como esta.
```
import csv
import os  # <-- Importamos esto para verificar si el archivo existe

def cargar_animales():
    id_animal = input("Ingrese el ID del animal: ")
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    edad = input("Ingrese la edad del animal: ")

    archivo_nombre = "animales.csv"
    
    # 1. Comprobamos si el archivo NO existe antes de abrirlo
    # os.path.exists devuelve True si el archivo ya está en la carpeta
    archivo_es_nuevo = not os.path.exists(archivo_nombre)

    with open(archivo_nombre, "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        
        # 2. Si el archivo es nuevo, escribimos primero los títulos (cabecera)
        if archivo_es_nuevo:
            escritor.writerow(["id", "nombre", "especie", "edad"])
        
        # 3. Luego escribimos los datos del animal que ingresó el usuario
        escritor.writerow([id_animal, nombre, especie, edad])
        
    print("Animal cargado exitosamente.")
```