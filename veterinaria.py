import csv
from datetime import datetime

from prints_utils import (
    mostrar_saludo,
    menu_inicio,
    mostrar_mensaje_atenciones,
    menu_atencion,
    mostrar_cabecera,
    elegir_especie,
    atender_mascota_print,
    tipo_atencion,
    elegir_atenciones,
    calcular_precios,
    mensaje_confirmacion
)

from csv_utils import (
    leer_csv,
    obtener_ultimo_id,
    traer_mascota_del_csv
)




def cargar_animales_csv():
    id_animal = str(obtener_ultimo_id("animales") + 1)
    nombre = input("Ingrese el nombre del animal: ")
    especie = elegir_especie()
    edad = input("Ingrese la edad del animal: ")
    ultima_atencion = datetime.now()

    with open("animales.csv", "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_animal, nombre, especie, edad, ultima_atencion])
    print("Animal cargado exitosamente.")
    
    return id_animal, nombre, especie, edad


def cargar_atencion_csv(id_mascota):
    id_atencion = str(obtener_ultimo_id("atenciones") + 1)
    id_mascota = id_mascota
    atencion = elegir_atenciones()
    precio = calcular_precios(atencion)

    with open("atenciones.csv", "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_atencion, id_mascota, atencion, precio])
        
    return atencion, precio



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
                    id_mascota, nombre_m, especie_m, edad_m = cargar_animales_csv()
                    atencion, precio = cargar_atencion_csv(id_mascota)
                    mensaje_confirmacion(nombre_m, especie_m, edad_m, atencion, precio)
                    
                    
                elif opcion2 == "2":
                    mostrar_cabecera()
                    leer_csv()
                    opcionMascota = input("Seleccione una mascota: ")
                    mascota = traer_mascota_del_csv(opcionMascota)
                    atencion, precio = cargar_atencion_csv(mascota["id"])
                    mensaje_confirmacion(mascota["nombre"], mascota["especie"], mascota["edad"], atencion, precio)
                    
                    
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