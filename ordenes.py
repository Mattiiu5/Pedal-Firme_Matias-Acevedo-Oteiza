from gestion_archivo import guardar_ordenes
import uuid

def validar_rut(rut):
    return rut.replace(".", "").replace("-", "").isdigit()


def crear_orden(ordenes):
    rut = input("RUT del cliente: ")
    if not validar_rut(rut):
        print("RUT inválido.")
        return
    
    cliente = input("Nombre del cliente: ").strip()
    servicios = input("Servicios (separados por comas): ")
    total = input("Monto total: ")

    if not total.isdigit():
        print("El total debe ser numérico.")
        return

    nueva = {
        "id": str(uuid.uuid4())[:4],
        "rut": rut,
        "cliente": cliente,
        "servicios": servicios,
        "total": total,
        "estado": "Abierta"
    }

    ordenes.append(nueva)
    guardar_ordenes(ordenes)
    print("Orden creada exitosamente.")


def listar_ordenes(ordenes):
    print("\nListado de órdenes")
    for o in ordenes:
        print(o)


def buscar_por_rut(ordenes):
    rut = input("Ingrese RUT a buscar: ")
    encontrados = [o for o in ordenes if o["rut"] == rut]

    if not encontrados:
        print("No se encontraron órdenes.")
        return

    for o in encontrados:
        print(o)


def editar_servicios(ordenes):
    id_buscar = input("ID de la orden: ")
    for o in ordenes:
        if o["id"] == id_buscar:
            print("Servicios actuales:", o["servicios"])
            nuevos = input("Nuevos servicios: ")
            o["servicios"] = nuevos
            guardar_ordenes(ordenes)
            print("Actualizado.")
            return
    print("Orden no encontrada.")


def cerrar_orden(ordenes):
    id_buscar = input("ID de la orden: ")
    for o in ordenes:
        if o["id"] == id_buscar:
            o["estado"] = "Cerrada"
            guardar_ordenes(ordenes)
            print("Orden cerrada.")
            return
    print("No existe esa orden.")


def eliminar_orden(ordenes):
    id_buscar = input("ID a eliminar: ")
    for o in ordenes:
        if o["id"] == id_buscar:
            ordenes.remove(o)
            guardar_ordenes(ordenes)
            print("Orden eliminada.")
            return
    print("No se encontró la orden.")
