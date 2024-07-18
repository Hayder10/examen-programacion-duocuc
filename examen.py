import random

TRABAJADORES = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

def mostrar_menu():
    while True:
        try:
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            opcion = int(input("Ingrese su opción: "))
            if opcion > 5 or opcion < 1: print("Ingrese una opción válida! (1-5)")
            else: return opcion
        except ValueError:
            print("Ingrese una opción válida! (Debe ser un entero)")

def generar_sueldo():
    return random.randint(300_000,2_500_000)




def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            break
main()
