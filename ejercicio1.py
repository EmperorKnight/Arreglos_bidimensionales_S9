# Datos de ventas de julio a diciembre 2022 por tienda
ventas = {
    "ABSA 1": [50000, 60000, 65000, 62000, 78000, 95000],
    "ABSA 2": [89000, 90000, 98000, 80000, 85000, 90000],
    "ABSA 3": [65000, 72000, 85000, 72000, 83000, 98000],
    "ABSA 4": [92000, 88000, 90000, 76000, 82000, 93000]
}

# a. Venta total por todas las tiendas
venta_total_general = sum(sum(mensual) for mensual in ventas.values())
print(f"a. Venta total por todas las tiendas: ${venta_total_general:,}")

# b. Venta total por tienda
print("b. Venta total por tienda:")
ventas_por_tienda = {}
for tienda, mensual in ventas.items():
    total = sum(mensual)
    ventas_por_tienda[tienda] = total
    print(f"   - {tienda}: ${total:,}")

# c. Tienda que más vendió en los 6 meses
tienda_mas_venta = max(ventas_por_tienda, key=ventas_por_tienda.get)
print(f"c. Tienda que más vendió: {tienda_mas_venta} con ${ventas_por_tienda[tienda_mas_venta]:,}")

# d. Tienda que menos vendió en los 6 meses
tienda_menos_venta = min(ventas_por_tienda, key=ventas_por_tienda.get)
print(f"d. Tienda que menos vendió: {tienda_menos_venta} con ${ventas_por_tienda[tienda_menos_venta]:,}")