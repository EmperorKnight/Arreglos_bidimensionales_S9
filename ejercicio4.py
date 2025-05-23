# a. Solicitar n y m
while True:
    n = int(input("Ingrese el número de filas (menor que 10): "))
    m = int(input("Ingrese el número de columnas (menor que 10): "))
    if 0 < n < 10 and 0 < m < 10:
        break
    else:
        print("Error: n y m deben ser positivos y menores que 10.")

# b. Ingresar valores de la matriz
matriz = []
print("\nIngrese los valores de la matriz:")
for i in range(n):
    fila = []
    for j in range(m):
        val = int(input(f"Elemento en fila {i+1}, columna {j+1}: "))
        fila.append(val)
    matriz.append(fila)

# c. Suma por fila
print("\nSuma de cada fila:")
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"Fila {i+1}: {suma_fila}")

# d. Promedio por columna
print("\nPromedio de cada columna:")
for j in range(m):
    suma_col = sum(matriz[i][j] for i in range(n))
    promedio = suma_col / n
    print(f"Columna {j+1}: {promedio:.2f}")

# e. Mayor valor de la matriz y su posición
mayor = matriz[0][0]
fila_mayor = 0
col_mayor = 0
for i in range(n):
    for j in range(m):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila_mayor = i
            col_mayor = j

print(f"\nMayor valor en la matriz: {mayor}")
print(f"Ubicación: fila {fila_mayor + 1}, columna {col_mayor + 1}")