
def mostrar_saludo():
    print("====================================")
    print("Bienvenido al sistema de veterinaria")
    print("====================================")

    
def menu_inicio():
    print("\nMenú Principal")
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
    print("Otro número para salir")
    opcion = input("Ingrese una opcion: ")
    return opcion


def mostrar_cabecera():
    print("------------------------------------")
    print("ID |   NOMBRE   | ESPECIE | EDAD")
    print("------------------------------------")


def elegir_especie():
    print("\nEspecies disponibles:")
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

    if especie == 'Perro' or especie == 'Gato':
        print("Desea una atención medica o atención de SPA?")
        print("Si es atención medica presione 1, si es SPA 2")
    else:
        print("Le corresponde atención médica directa.")
    return especie



def elegir_atenciones():
    print("\nAtenciones disponibles:")
    print("1. Vacunación")
    print("2. Desparasitación")
    print("3. Castracion")
    print("4. Consulta general")
    print("5. Quimioterapia para mascotas con cáncer")
    print("6. Terapia de rehabilitación para mascotas con lesiones musculares o articulares")
    print("7. Cirugias estéticas")
    print("8. Control de peso y nutrición personalizada")
    print("9. Atención de emergencia 24/7")
    print("0. Otro")
    opcion = input("Seleccione una atención: ")
    if opcion == "1":
        return "Vacunación"
    elif opcion == "2":
        return "Desparasitación"
    elif opcion == "3":
        return "Castracion"
    elif opcion == "4":
        return "Consulta general"
    elif opcion == "5":
        return "Quimioterapia para mascotas con cáncer"
    elif opcion == "6":
        return "Terapia de rehabilitación para mascotas con lesiones musculares o articulares"
    elif opcion == "7":
        return "Cirugias estéticas"
    elif opcion == "8":
        return "Control de peso y nutrición personalizada"
    elif opcion == "9":
        return "Atención de emergencia 24/7"
    elif opcion == "0":
        return input("Ingrese el tipo de atención que desea: ")
    else:
        return "Atención desconocida"



def calcular_precios(atencion):
    tasa_de_servicio = 20000
    
    if atencion == "Vacunación":
        return tasa_de_servicio + 5000
    elif atencion == "Desparasitación":
        return tasa_de_servicio + 3000
    elif atencion == "Castracion":
        return tasa_de_servicio + 15000
    elif atencion == "Consulta general":
        return tasa_de_servicio + 10000
    elif atencion == "Quimioterapia para mascotas con cáncer":
        return tasa_de_servicio + 50000
    elif atencion == "Terapia de rehabilitación para mascotas con lesiones musculares o articulares":
        return tasa_de_servicio + 25000
    elif atencion == "Cirugias estéticas":
        return tasa_de_servicio + 20000
    elif atencion == "Control de peso y nutrición personalizada":
        return tasa_de_servicio + 15000
    elif atencion == "Atención de emergencia 24/7":
        return tasa_de_servicio + 30000
    else:
        return tasa_de_servicio + 100000
    
    
def mensaje_confirmacion(nombre, especie, edad, atencion, precio):
    print("\n==========================================")
    print(f"Se atendió a {nombre} un {especie} de {edad} años.")
    print(f"Se le realizó el procedimiento de {atencion} con un costo de ${precio}.")
    print("\n==========================================")


def confirmar_datos(nombre, especie, edad):
        print("\n------------------------------------")
        print("¿Confirmas los datos del nuevo animal?")
        print(f"Nombre:  {nombre}")
        print(f"Especie: {especie}")
        print(f"Edad:    {edad} años")
        print("------------------------------------")


def mostrar_resumen_estadistico(
    total_atenciones, 
    total_perros, 
    total_gatos, 
    total_pajaros, 
    total_reptiles, 
    total_otros, 
    recaudacion_total):
    
        print("\n==========================================")
        print("          RESUMEN ESTADÍSTICO             ")
        print("==========================================")
        print(f"Total de atenciones realizadas: {total_atenciones}")
        print("------------------------------------------")
        print(f" Atenciones a Perros:  {total_perros}")
        print(f" Atenciones a Gatos:   {total_gatos}")
        print(f" Atenciones a Pájaros: {total_pajaros}")
        print(f" Atenciones a Reptiles:{total_reptiles}")
        print(f" Atenciones a Otros:   {total_otros}")
        print("==========================================")

        print(f"Recaudación total: ${recaudacion_total}")
        
        