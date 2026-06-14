import csv
from datetime import datetime

def mostrar_saludo():
    print("====================================")
    print("Bienvenido al sistema de veterinaria")
    print("====================================")
    print("\nMenú Principal")


def menu_inicio():
    print("1. Atender una Mascota")
    print("2. Resumen estadistico")
    print("Otro número para salir")
    opcion = input("Ingrese una opcion: ")
    return opcion



def mostrar_mensaje_atenciones():
    print("\n==========================================")
    print("ATENCION DE MASCOTAS")
    print("==========================================")


def menu_atencion():
    print("\n1. Cargar nuevo animal")
    print("2. Ver lista de animales")
    print("3. Resumen estadistico")
    print("Otro número para salir")
    opcion = input("Ingrese una opcion: ")
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
    

def elegir_especie():
    print("Especies disponibles:")
    print("1. Perro")
    print("2. Gato")
    print("3. Pájaro")
    print("4. Reptil")
    print("5. Otro")
    opcion = input("Seleccione una especie: ")
    if opcion == "1":
        return "Perro"
    elif opcion == "2":
        return "Gato"
    elif opcion == "3":
        return "Pájaro"
    elif opcion == "4":
        return "Reptil"
    else:
        return "Otro"


def cargar_animales():
    id_animal = str(obtener_ultimo_id() + 1)
    nombre = input("Ingrese el nombre del animal: ")
    especie = elegir_especie()
    edad = input("Ingrese la edad del animal: ")
    ultima_atencion = datetime.now()

    with open("animales.csv", "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_animal, nombre, especie, edad, ultima_atencion])
    print("Animal cargado exitosamente.")
    atender_mascota(
        id=id_animal, 
        nombre=nombre, 
        especie=especie, 
        edad=edad)
    
def tipo_atencion():
    print("Tipos de atención:")
    print("1. Atención médica")
    print("2. SPA")
    opcion_atencion = input("Seleccione el tipo de atención: ")
    return opcion_atencion
    
    
def atender_mascota(id, nombre, especie, edad):
    if especie == 'Perro':
        print("Atendiendo a un perro llamado", nombre)
        contador_perros = contador_perros + 1
        print("Desea una atención medica o atención de SPA?")
        print("Si es atención medica presione 1, si es SPA 2")
        
    elif especie == 'Gato':
        print("Atendiendo a un gato llamado", nombre)
        contador_gatos = contador_gatos + 1
        
    elif especie == 'Pájaro':
        print("Atendiendo a un pájaro llamado", nombre)
        contador_pajaros = contador_pajaros + 1
        
    elif especie == 'Reptil':
        print("Atendiendo a un reptil llamado", nombre)
        contador_reptil = contador_reptil +1
        
    else:
        print("Atendiendo a una mascota de especie desconocida llamada", nombre)
        contador_otros = contador_otros + 1
        

def traer_mascota_del_csv(id):
    with open("animales.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila['id'] == id:
                return fila
    return None


mostrar_saludo()
opcion = menu_inicio()

while opcion == "1" or opcion == "2":
    if opcion == "1":
        mostrar_mensaje_atenciones()
        opcion2 = menu_atencion()
        while opcion2 == "1" or opcion2 == "2" or opcion2 == "3":
            if opcion2 == "1":
                cargar_animales()
                
            elif opcion2 == "2":
                mostrar_cabecera()
                leer_csv()
                opcionMascota = input("Seleccione una mascota: ")
                mascota = traer_mascota_del_csv(opcionMascota)
                atender_mascota(
                    id=opcionMascota, 
                    nombre=mascota["nombre"], 
                    especie=mascota["especie"], 
                    edad=mascota["edad"])
                
                
            elif opcion2 == "3":
                print("Has elegido la opcion2 3")
            else:
                print("opcion2 no valida")
                break
            opcion2 = menu_atencion()
            
            
            
            
    elif opcion == "2":
        print("Has elegido la opcion 2")
    else:
        print("Opcion no valida")
        break
    opcion = menu_inicio()


print("Gracias por usar el sistema")
