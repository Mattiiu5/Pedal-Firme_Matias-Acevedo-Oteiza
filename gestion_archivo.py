import csv

ARCHIVO = "datos.csv"

def cargar_ordenes():
    ordenes = []
    try:
        with open("datos/ordenes.csv", "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for row in lector:
                ordenes.append(row)
    except FileNotFoundError:
        pass
    return ordenes


def guardar_ordenes(ordenes):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as file:
        campos = ["id", "rut", "cliente", "servicios", "total", "estado"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for o in ordenes:
            writer.writerow(o)
