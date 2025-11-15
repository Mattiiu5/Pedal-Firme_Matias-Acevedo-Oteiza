from datetime import datetime

def reporte_ventas(ordenes):
    total = sum(int(o["total"]) for o in ordenes if o["estado"] == "Cerrada")
    print("\n=== REPORTE DE VENTAS ===")
    print(f"Órdenes cerradas: {len([o for o in ordenes if o['estado'] == 'Cerrada'])}")
    print(f"Total recaudado: ${total}")
