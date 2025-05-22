# 3. La linealización es un proceso por el cual, se transforma un arreglo bidimensional en un
# arreglo unidimensional. Existen tres técnicas para realizar este proceso: por filas, por
# columnas o en zigzag. Crear un programa que permita la linealización de un arreglo
# bidimensional por columnas. Los datos del arreglo bidimensional serán tomados de la tabla. 

# Ejemplo:  Arreglo original                  Arreglo linealizado
#           [1 2 3 7]                         [1 4 2 5 3 6 7 8]
#           [4 5 6 8]

import os 

os.system("cls || clear")

matriz = [[1,2,3,7], [4,5,6,8]]

print(f"Arreglo original")

for i in matriz:
    print("[",end="")
    for a in i:
        print(a, end=" ")
    print("]")

print(" ")

filas = len(matriz)
columnas = len(matriz[0])
matriz3 = []

for x in range(columnas):
    for v in range(filas):
        matriz3.append(matriz[v][x])

print(f"Arreglo linealizado")

print("[",end="")
for columnas in matriz3:
    print(columnas,end = " ")
print("]")
