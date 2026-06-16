import csv
from datetime import datetime

from prints_utils import (
    mostrar_saludo,
    menu_inicio,
    mostrar_mensaje_atenciones,
    menu_atencion,
    mostrar_cabecera,
    elegir_especie,
    atender_mascota_print
)

from csv_utils import (
    leer_csv,
    obtener_ultimo_id,
    traer_mascota_del_csv
)
    




def cargar_animales_csv():
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



def cargar_animales(id_animal, nombre, especie, edad):
    contador_perros = 0
    contador_gatos = 0
    contador_pajaros = 0
    contador_reptil = 0
    contador_otros = 0

    
    esp_atendida = atender_mascota(id_animal, nombre, especie, edad)
    
    if esp_atendida == 'Perro':
        contador_perros += 1
    elif esp_atendida == 'Gato':
        contador_gatos += 1
    elif esp_atendida == 'Pájaro':
        contador_pajaros += 1
    elif esp_atendida == 'Reptil':
        contador_reptil += 1
    else:
        contador_otros += 1
    




def main():
    """Función principal que controla el flujo del programa."""
    mostrar_saludo()
    opcion = menu_inicio()

    while opcion == "1" or opcion == "2":
        if opcion == "1":
            mostrar_mensaje_atenciones()
            opcion2 = menu_atencion()
            
            while opcion2 == "1" or opcion2 == "2" or opcion2 == "3":
                if opcion2 == "1":
                    cargar_animales_csv()
                    
                elif opcion2 == "2":
                    mostrar_cabecera()
                    leer_csv()
                    opcionMascota = input("Seleccione una mascota: ")
                    mascota = traer_mascota_del_csv(opcionMascota)
                    
                    cargar_animales(
                        opcionMascota, 
                        mascota["nombre"], 
                        mascota["especie"], 
                        mascota["edad"]
                    )
                    
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


if __name__ == "__main__":
    main()