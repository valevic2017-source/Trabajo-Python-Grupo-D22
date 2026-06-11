import csv
    
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

def mostrar_cabecera():
    print("------------------------------------")
    print("ID |   NOMBRE   | ESPECIE | EDAD")
    print("------------------------------------")


cargar_saludo()
opcion = mostrar_menu()

while opcion == "1" or opcion == "2" or opcion == "3":
    if opcion == "1":
        print("has elegido la opcion 1")
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
