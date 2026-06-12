import csv
from datetime import datetime

def cargar_saludo():
    print("====================================")
    print("Bienvenido al sistema de veterinaria")
    print("====================================")


def mostrar_menu():
    print("\nMenú Principal")
    print("1. Cargar nuevo animal")
    print("2. Ver lista de animales")
    print("3. Resumen estadistico")
    print("Otro número para salir")
    opcion = input("ingrese una opcion: ")
    return opcion

def mostrar_cabecera():
    print("------------------------------------")
    print("ID |   NOMBRE   | ESPECIE | EDAD")
    print("------------------------------------")

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


def cargar_animales():
    id_animal = str(obtener_ultimo_id() + 1)
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    edad = input("Ingrese la edad del animal: ")
    ultima_atencion = datetime.now()

    with open("animales.csv", "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_animal, nombre, especie, edad, ultima_atencion])
    print("Animal cargado exitosamente.")


cargar_saludo()
opcion = mostrar_menu()

while opcion == "1" or opcion == "2" or opcion == "3":
    if opcion == "1":
        cargar_animales()
    elif opcion == "2":
        mostrar_cabecera()
        leer_csv()
    elif opcion == "3":
        print("has elegido la opcion 3")
    else:
        print("opcion no valida")
        break
    opcion = mostrar_menu()

print("gracias por usar el sistema")
