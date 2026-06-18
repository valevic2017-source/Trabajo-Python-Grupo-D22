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

### datetime.now()

- Se necesita importar from datetime import datetime
- Obtiene la fecha y la hora actual

### fecha.strftime("%Y-%m-%d")

- Formatea la fecha y hora a solamente fecha, util para el resumen estadistico

### .strip().upper()

- strip elimina los espacios en blanco
- upper convierte la variable ingresada a mayusculas

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

# Uso de Inteligencia Artificial en el proyecto

## Manejo de errores

La propuesta consiste en modularizar el código en funciones para identificar donde se originan los fallos.
Ante un error, se consultará a la IA proporcionando el mensaje de error como la función afectada.
Se especifica en el prompt que la IA proporcione una guía teórica en lugar de generar el código corregido de forma automática. De este modo se promueve la comprensión de la lógica y sintaxis del lenguaje, evitando la práctica del "copiar y pegar"

## Conectar dos archivos

Para el resumen estadistico se necesita unir los archivos de animales y atenciones, ya que hay que contar cuantas mascotas de cada especie se atendieron en un mismo dia. Se consulta a la IA como desarrollar una funcion que acceda a dos archivos.
