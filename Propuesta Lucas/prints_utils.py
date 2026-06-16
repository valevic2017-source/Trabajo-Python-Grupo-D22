
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
    

def atender_mascota_print(id, nombre, especie, edad):
    print("\n==========================================")
    print("\nAtendiendo a la mascota con ID:", id)
    print("===========================================")
    if especie == 'Perro':
        print("Atendiendo a un perro llamado", nombre)
    elif especie == 'Gato':
        print("Atendiendo a un gato llamado", nombre)
    elif especie == 'Pájaro':
        print("Atendiendo a un pájaro llamado", nombre)
    elif especie == 'Reptil':
        print("Atendiendo a un reptil llamado", nombre)
    else:
        print("Atendiendo a una mascota de especie desconocida llamada", nombre)

    if especie in ['Perro', 'Gato']:
        print("Desea una atención medica o atención de SPA?")
        print("Si es atención medica presione 1, si es SPA 2")
    else:
        print("Le corresponde atención médica directa.")
    return especie