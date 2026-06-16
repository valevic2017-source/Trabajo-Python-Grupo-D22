import csv
from datetime import datetime


def leer_csv():
    with open("animales.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            id_animal = fila['id']
            nombre = fila['nombre']
            especie = fila['especie']
            edad = fila['edad']

            if len(nombre) < 10:
                nombre = nombre.ljust(10)
            if len(especie) < 7:
                especie = especie.ljust(7)
            if len(edad) < 4:
                edad = edad.rjust(4)

            print(f"{id_animal}  | {nombre} | {especie} | {edad}")


def obtener_ultimo_id():
    try:
        with open("animales.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            lista_de_ids = [] 
            # 2. Recorremos el archivo fila por fila de forma tradicional
            for fila in lector:
                # Convertimos el ID de texto a número entero
                id_numero = int(fila['id'])
                # Lo agregamos a nuestra lista
                lista_de_ids.append(id_numero)
            # 3. Si la lista tiene elementos, buscamos el mayor. Si está vacía, devolvemos 0.
            if lista_de_ids:
                return max(lista_de_ids)
            else:
                return 0
    except FileNotFoundError: # Comprobación de error en caso de que el archivo no exista
        return 0
    

def traer_mascota_del_csv(id):
    with open("animales.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila['id'] == id:
                return fila
    return None
