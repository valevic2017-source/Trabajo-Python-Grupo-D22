import csv
from datetime import datetime

from prints_utils import (
    mostrar_saludo,
    menu_inicio,
    mostrar_mensaje_atenciones,
    menu_atencion,
    mostrar_cabecera,
    elegir_especie,
    elegir_atenciones,
    calcular_precios,
    mensaje_confirmacion,
    mostrar_resumen_estadistico,
    confirmar_datos
)

from csv_utils import (
    leer_csv,
    obtener_ultimo_id,
    traer_mascota_del_csv
)



def generar_reporte_estadistico():
    # 1. Inicializamos los contadores tradicionales
    total_perros = 0
    total_gatos = 0
    total_pajaros = 0
    total_reptiles = 0
    total_otros = 0
    total_atenciones = 0
    recaudacion_total = 0.0

    print("\nPROCESANDO ESTADÍSTICAS DE ATENCIONES...")

    try:
        # Agregamos skipinitialspace=True por las dudas con los espacios
        with open("atenciones.csv", "r", encoding="utf-8") as archivo_atenciones:
            lector_atenciones = csv.DictReader(archivo_atenciones, skipinitialspace=True)
            
            for atencion in lector_atenciones:
                total_atenciones += 1
                id_m = atencion['id_mascota']
                
                # Convertimos el texto del CSV a número decimal para poder sumarlo
                precio_atencion = float(atencion['precio'])
                recaudacion_total += precio_atencion
                
                mascota = traer_mascota_del_csv(id_m)
                
                if mascota is not None:
                    especie = mascota['especie']
                    
                    if especie == "Perro":
                        total_perros += 1
                    elif especie == "Gato":
                        total_gatos += 1
                    elif especie == "Pájaro":
                        total_pajaros += 1
                    elif especie == "Reptil":
                        total_reptiles += 1
                    else:
                        total_otros += 1
                else:
                    total_otros += 1 
                    
        # Enviamos todas las variables a tu función de diseño, incluyendo la recaudación
        mostrar_resumen_estadistico(
            total_atenciones, 
            total_perros, 
            total_gatos, 
            total_pajaros, 
            total_reptiles, 
            total_otros,
            recaudacion_total  
        )

    except FileNotFoundError:
        print("Error: No se encontró el archivo de atenciones.")

    except FileNotFoundError:
        print("Error: No se pudo generar el reporte porque falta alguno de los archivos CSV.")



def cargar_animales_csv():
    while True:
        id_animal = str(obtener_ultimo_id("animales") + 1)
        nombre = input("\nIngrese el nombre del animal: ")
        especie = elegir_especie()
        edad = input("Ingrese la edad del animal: ")
        confirmar_datos(nombre, especie, edad) 

        
        confirmacion = input("¿Guardar cambios? (S/N): ").strip().upper()

        if confirmacion == "S":
            # Si confirma, guardamos en el archivo
            with open("animales.csv", "a", encoding="utf-8", newline='') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([id_animal, nombre, especie, edad])
            
            print("¡Animal cargado exitosamente!")
            
            # Cortamos el bucle infinito y devolvemos los datos al main
            return id_animal, nombre, especie, edad
            
        else:
            # Si pone 'N' (o cualquier otra cosa), avisamos y el while True reinicia el proceso
            print("\nReintentando la carga del animal desde el principio...")


def cargar_atencion_csv(id_mascota):
    id_atencion = str(obtener_ultimo_id("atenciones") + 1)
    id_mascota = id_mascota
    atencion = elegir_atenciones()
    precio = calcular_precios(atencion)
    fecha_actual = datetime.now()
    fecha_atencion = fecha_actual.strftime("%Y-%m-%d")

    with open("atenciones.csv", "a", encoding="utf-8", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_atencion, id_mascota, atencion, precio, fecha_atencion])
        
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
                    
                else:
                    print("OPCION no valida")
                    break
                opcion2 = menu_atencion()
                
        elif opcion == "2":
            generar_reporte_estadistico()
            
            
            
        else:
            print("Opcion no valida")
            break
            
        opcion = menu_inicio()

    print("Gracias por usar el sistema")


if __name__ == "__main__":
    main()