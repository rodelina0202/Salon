import sys
from utilidades import limpiar, banner
from funciones import *

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# MENÚ GENÉRICO
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def menu(titulo, opciones):
    while True:
        limpiar()
        banner(titulo)
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op[0]}")
        print(f"{len(opciones) + 1}. Volver")
        opcion = input("\nSeleccione: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(opciones):
                opciones[opcion - 1][1]()
            elif opcion == len(opciones) + 1:
                break

#━━━━━━━━━━━━━━━━━━━━━━━━━━
# MENU PRINCIPAL
#━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    while True:
        limpiar()
        banner("RODE'S SALÓN")
        print("1. Clientes")
        print("2. Empleados")
        print("3. Servicios")
        print("4. Citas")
        print("5. Módulo Administrativo")
        print("6. Salir")
        opcion = input("\nSeleccione: ")
        if opcion == "1":
            menu("CLIENTES", [
                ("Agregar cliente", agregar_cliente),
                ("Listar clientes", listar_clientes),
                ("Buscar cliente", buscar_cliente),
                ("Eliminar cliente", eliminar_cliente)
            ])
        elif opcion == "2":
            menu("EMPLEADOS", [
                ("Agregar empleado", agregar_empleado),
                ("Listar empleados", listar_empleados),
                ("Buscar empleado", buscar_empleado),
                ("Eliminar empleado", eliminar_empleado)
            ])
        elif opcion == "3":
            menu("SERVICIOS", [
                ("Agregar servicio", agregar_servicio),
                ("Listar servicios", listar_servicios),
                ("Buscar servicio", buscar_servicio),
                ("Eliminar servicio", eliminar_servicio)
            ])
        elif opcion == "4":
            menu("CITAS", [
                ("Crear cita", agregar_cita),
                ("Listar citas", listar_citas),
                ("Buscar cita", buscar_cita),
                ("Eliminar cita", eliminar_cita)
            ])
        elif opcion == "5":
            menu("MÓDULO ADMINISTRATIVO", [
                ("Ver citas por día", citas_por_dia),
                ("Ver total de ganancias", total_ganancias),
                ("Ver ganancias por mes", ganancias_por_mes),
                ("Resumen semanal", resumen_semanal)
])
        elif opcion == "6":
            print("Saliendo del sistema...")
            sys.exit()

if __name__ == "__main__":
    main()
