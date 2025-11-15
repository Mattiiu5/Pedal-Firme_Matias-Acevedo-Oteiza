from gestion_archivo import cargar_ordenes
from ordenes import (
    crear_orden, listar_ordenes, buscar_por_rut,
    editar_servicios, cerrar_orden, eliminar_orden
)
from reportes import reporte_ventas

def menu():
    print("""
=== TALLER DE BICICLETAS - PEDAL FIRME ===
1. Crear orden
2. Listar órdenes
3. Buscar por RUT
4. Editar servicios
5. Cerrar orden
6. Eliminar orden
7. Reporte de ventas
0. Salir
""")

def main():
    ordenes = cargar_ordenes()

    while True:
        menu()
        op = input("Seleccione opción: ")

        if op == "1":
            crear_orden(ordenes)
        elif op == "2":
            listar_ordenes(ordenes)
        elif op == "3":
            buscar_por_rut(ordenes)
        elif op == "4":
            editar_servicios(ordenes)
        elif op == "5":
            cerrar_orden(ordenes)
        elif op == "6":
            eliminar_orden(ordenes)
        elif op == "7":
            reporte_ventas(ordenes)
        elif op == "0":
            print("Saliendo…")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
