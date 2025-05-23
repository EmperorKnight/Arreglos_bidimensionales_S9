# Crear matriz vacía de 3x4
ventas = []

print("Ingrese la cantidad de computadoras vendidas por cada vendedor en cada zona:")

for i in range(3):  # 3 vendedores
    fila = []
    for j in range(4):  # 4 zonas
        cantidad = int(input(f"Ingrese ventas del Vendedor {i} en la Zona {j}: "))
        fila.append(cantidad)
    ventas.append(fila)

# Mostrar la matriz de ventas
print("\nMatriz de ventas (Vendedores x Zonas):")
for i, fila in enumerate(ventas):
    print(f"Vendedor {i}: {fila}")

# a. La zona en la que más computadores se vendió
zona_mas_ventas = 0
mayor_ventas_zona = 0

for zona in range(4):
    total_zona = sum(ventas[vendedor][zona] for vendedor in range(3))
    if total_zona > mayor_ventas_zona:
        mayor_ventas_zona = total_zona
        zona_mas_ventas = zona

# b. El vendedor que menos computadores vendió
vendedor_menos_ventas = 0
menor_ventas = float('inf')

for i, vendedor in enumerate(ventas):
    total_vendedor = sum(vendedor)
    if total_vendedor < menor_ventas:
        menor_ventas = total_vendedor
        vendedor_menos_ventas = i

# c. Total de computadores vendidos
total_general = sum(sum(vendedor) for vendedor in ventas)

# Resultados
print(f"\na. La zona en la que más se vendió es la zona {zona_mas_ventas} con {mayor_ventas_zona} computadoras.")
print(f"b. El vendedor que menos vendió es el vendedor {vendedor_menos_ventas} con {menor_ventas} computadoras.")
print(f"c. El total de computadoras vendidas es: {total_general}")


