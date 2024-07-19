import random
import csv
from math import pow

TRABAJADORES = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
dict_trabajadores = []

def mostrar_menu():
    while True:
        try:
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            opcion = int(input("Ingrese su opción: "))
            if opcion > 5 or opcion < 1: imprimir_error("Ingrese una opción válida! (1-5)")
            else: return opcion
        except ValueError:
            imprimir_error("Ingrese una opción válida! (Debe ser un entero)")

def generar_sueldo():
    return random.randint(300_000,2_500_000)

def asignar_sueldos_aleatorios():
    for trabajador in TRABAJADORES:
        nuevo_trabajador = {
            "Nombre" : trabajador,
            "Sueldo" : generar_sueldo()
        }
        dict_trabajadores.append(nuevo_trabajador)

def sueldos_trabajadores():
    sueldos = []
    for trabajador in dict_trabajadores:
        sueldos.append(trabajador["Sueldo"])
    return sueldos

def clasificar_sueldos():
    sueldos_bajos = []
    sueldos_medios = []
    sueldos_altos = []
    for trabajador in dict_trabajadores:
        if trabajador["Sueldo"] < 800_000:
            sueldos_bajos.append(trabajador)
        elif trabajador["Sueldo"] >= 800_000 and trabajador["Sueldo"] <= 2_000_000:
            sueldos_medios.append(trabajador)
        elif trabajador["Sueldo"] > 2_000_000:
            sueldos_altos.append(trabajador)

    if len(sueldos_bajos):
        print(f"\nSueldos menores a $800.000 TOTAL: {len(sueldos_bajos)}\n")   
        print("Nombre empleado\t\tSueldo")
        for trabajador in sueldos_bajos:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")
    
    if len(sueldos_medios):
        print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldos_medios)}\n")
        print("Nombre empleado\t\tSueldo")
        for trabajador in sueldos_medios:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")

    if len(sueldos_altos):
        print(f"\nSueldos superiores a $2.000.000 TOTAL: {len(sueldos_altos)}\n")
        print("Nombre empleado\t\tSueldo")
        for trabajador in sueldos_altos:
            print(f"{trabajador["Nombre"]}\t\t${trabajador["Sueldo"]}")
    
    sueldos = sueldos_trabajadores()

    print(f"\nTOTAL SUELDOS: ${sum(sueldos)}\n")

def ver_estadisticas():
    trabajador_sueldo_alto = encontrar_trabajador(alto=True)
    trabajador_sueldo_bajo = encontrar_trabajador(alto=False)
    promedio_sueldos = calcular_promedio_sueldos()
    media_geometrica = calcular_media_geometrica()
    print("\nSUELDO MÁS ALTO:\n")
    print("Nombre\t\t\tSueldo")
    print(f"{trabajador_sueldo_alto["Nombre"]}\t\t${trabajador_sueldo_alto["Sueldo"]}")
    print("\nSUELDO MÁS BAJO:\n")
    print("Nombre\t\t\tSueldo")
    print(f"{trabajador_sueldo_bajo["Nombre"]}\t\t${trabajador_sueldo_bajo["Sueldo"]}")
    print("\nPROMEDIO DE SUELDOS:\n")
    print(f"${promedio_sueldos}\n")
    print("\nMEDIA GEOMETRICA DE SUELDOS:\n")
    print(f"${media_geometrica}\n")

def encontrar_trabajador(alto):
    if alto:
        trabajador_max = {"Sueldo": 0}
        for trabajador in dict_trabajadores:
            if trabajador["Sueldo"] > trabajador_max["Sueldo"]:
                trabajador_max = trabajador
        return trabajador_max
    else:
        trabajador_min = {"Sueldo": 9999999999}
        for trabajador in dict_trabajadores:
            if trabajador["Sueldo"] < trabajador_min["Sueldo"]:
                trabajador_min = trabajador
        return trabajador_min

def calcular_promedio_sueldos():
    sueldos = sueldos_trabajadores()
    return int(sum(sueldos) / len(sueldos))

def calcular_media_geometrica():
    sueldos = sueldos_trabajadores()
    multiplicado = 1
    for sueldo in sueldos:
        multiplicado*=sueldo
    return int(pow(multiplicado,1/len(sueldos)))

def reporte_sueldos():
    trabajadores_completos = calcular_trabajadores_completos()
    with open("reporte_sueldos.csv","w") as archivo:
        archivo_csv = csv.DictWriter(archivo,trabajadores_completos[0].keys())
        archivo_csv.writeheader()
        archivo_csv.writerows(trabajadores_completos)


def calcular_trabajadores_completos():
    trabajadores_completos = []
    for trabajador in dict_trabajadores:
        desc_salud = int(trabajador["Sueldo"] * 0.07)
        desc_afp = int(trabajador["Sueldo"] * 0.12)
        trabajador = {
            "Nombre empleado" : trabajador["Nombre"],
            "Sueldo Base" : trabajador["Sueldo"],
            "Descuento Salud": desc_salud,
            "Descuento AFP": desc_afp,
            "Sueldo Líquido": trabajador["Sueldo"] - (desc_salud + desc_afp)
        }
        trabajadores_completos.append(trabajador)
    return trabajadores_completos


def imprimir_mensaje(mensaje):
    print("")
    print("------------------")
    print(mensaje)
    print("------------------")
    print("")

def imprimir_error(mensaje):
    print("")
    print("###########")
    print("¡ERROR!")
    print(mensaje)
    print("###########")
    print("")


def main():
    sueldos_generados = False
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            asignar_sueldos_aleatorios()
            sueldos_generados = True
            imprimir_mensaje("Sueldos asignados correctamente.")
        elif opcion == 2:
            if sueldos_generados: clasificar_sueldos()
            else: imprimir_error("Debes asignar los sueldos primero!")
        elif opcion == 3:
            if sueldos_generados: ver_estadisticas()
            else: imprimir_error("Debes asignar los sueldos primero!")
        elif opcion == 4:
            if sueldos_generados: reporte_sueldos()
            else: imprimir_error("Debes asignar los sueldos primero!")
        elif opcion == 5:
            break
main()