# Sistema de Gestión de Veterinaria

Trabajo Final Integrador - Laboratorio de Python
Algoritmos y Estructuras de Datos - ISI - Ciclo 2026

## Integrantes del grupo

- Vicentin Valentina
- Cabral Viola Luka
- Sanabria Lucas

## Comisión 1.4 D

## Descripción general del sistema

Este proyecto es un sistema de consola desarrollado en Python para la gestión de una veterinaria, correspondiente al escenario **"Gestión de veterinaria"**. Permite registrar mascotas, cargar atenciones (consultas, vacunaciones, cirugías, etc.) y generar un resumen estadístico de la actividad del negocio.

El sistema persiste la información en dos archivos CSV:

- **animales.csv**: guarda el registro de mascotas (id, nombre, especie, edad).
- **atenciones.csv**: guarda el historial de atenciones realizadas (id, id de la mascota, tipo de atención, precio y fecha).

### Estructura del proyecto

El código está modularizado en tres archivos:

- **veterinaria.py**: contiene el punto de entrada del programa y controla el flujo principal a través de menús (atender mascota, ver resumen estadístico), además de las funciones que orquestan la carga de animales y atenciones, y la generación del reporte estadístico.
- **prints_utils.py**: concentra toda la interacción con el usuario (menús, mensajes, confirmaciones) y la lógica de negocio simple, como el cálculo de precios de cada atención según una tasa de servicio base.
- **csv_utils.py**: agrupa las funciones de lectura de los archivos CSV, como listar las mascotas registradas, obtener el último ID utilizado (para autoincrementar nuevos registros) y buscar una mascota puntual por su ID.

### Funcionalidades principales

1. **Atender una mascota**

   - Cargar un animal nuevo: se ingresan nombre, especie (elegida de un menú: Perro, Gato, Pájaro, Reptil u Otro) y edad, se confirma la carga (S/N) y se guarda en `animales.csv` con un ID autoincremental.
   - Atender un animal ya existente: se muestra la lista de mascotas cargadas y se selecciona una por ID.
   - En ambos casos, se elige un tipo de atención (vacunación, desparasitación, castración, consulta general, cirugías, emergencias, etc.), se calcula su precio y se guarda el registro en `atenciones.csv`, mostrando luego un mensaje de confirmación con los datos de la atención.

2. **Resumen estadístico**
   - Recorre el archivo `atenciones.csv` y, cruzando cada atención con la mascota correspondiente en `animales.csv`, calcula:
     - cantidad total de atenciones realizadas;
     - cantidad de atenciones por especie (perros, gatos, pájaros, reptiles, otros);
     - recaudación total acumulada.

### Estructuras y buenas prácticas aplicadas

- **Estructuras condicionales** (`if`/`elif`/`else`): selección de especie, tipo de atención, cálculo de precios y clasificación de estadísticas por especie.
- **Estructuras repetitivas** (`while`): menús principales que se repiten hasta que el usuario elige una opción válida de salida; recorrido de los archivos CSV con `for`.
- **Funciones**: todo el sistema está modularizado en funciones con responsabilidades específicas (mostrar menús, calcular precios, leer/escribir CSV, generar reportes, etc.).
- **Validaciones**: confirmación de datos antes de guardar un nuevo animal (S/N), control de opciones inválidas en los menús.
- **Acumuladores y contadores**: variables como `total_perros`, `total_gatos`, `total_atenciones` y `recaudacion_total` se van incrementando a medida que se procesan los registros.
- **Manejo de errores**: uso de `try/except FileNotFoundError` al leer los archivos CSV, para informar al usuario si falta algún archivo en lugar de que el programa se detenga abruptamente.

## Built-in Funciones

### open("archivo.csv", "r", encoding="utf-8")

- Abre el archivo en modo lectura
- "r" significa lectura
- "a" significa escritura con persistencia de datos
- "utf-8" es para que no haya problemas con los acentos
- "w" es una forma de escribir en un archivo, pero borraría todo el contenido dejandolo en blanco antes de escribir.

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

### Importante

En la solución propuesta, se da por hecho que existe un archivo `animales.csv` con al menos la cabecera. Esto se hace así para evitar confusiones con la escritura del archivo. Si se desea crear el script sin el archivo de cabecera, se debería incluir la librería `os` y verificar si existe antes de escribir. Esto agregaría una complejidad innecesaria para una situación como esta.

```python
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

## Instrucciones de ejecución

### Requisitos

- Tener instalado Python 3.

### Pasos

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/valevic2017-source/Trabajo-Python-Grupo-D22.git
   cd Trabajo-Python-Grupo-D22
   ```
2. Asegurarse de que los archivos `animales.csv` y `atenciones.csv` estén en la misma carpeta que `veterniaria.py` (se incluyen archivos de ejemplo en el repositorio; si no existen, el sistema los puede ir generando a medida que se cargan animales y atenciones).
3. Ejecutar el programa desde la consola:
   ```bash
   python veterniaria.py
   ```
4. Navegar el sistema a través del menú principal:
   - Opción **1**: Atender una mascota (cargar un animal nuevo o atender uno existente).
   - Opción **2**: Ver el resumen estadístico de atenciones.
   - Cualquier otra opción: salir del programa.

## Uso de Inteligencia Artificial en el proyecto
Se utilizó mayoritariamente la IA de Gemini 3.5 Flash

### Manejo de errores

La propuesta consiste en modularizar el código en funciones para identificar dónde se originan los fallos. Ante un error, se consulta a la IA proporcionando el mensaje de error y la función afectada. Se especifica en el prompt que la IA proporcione una guía teórica en lugar de generar el código corregido de forma automática. De este modo se promueve la comprensión de la lógica y sintaxis del lenguaje, evitando la práctica del "copiar y pegar".

### Conectar dos archivos

Para el resumen estadístico se necesita unir los archivos de animales y atenciones, ya que hay que contar cuántas mascotas de cada especie se atendieron en un mismo día. Se consulta a la IA cómo desarrollar una función que acceda a dos archivos.
