# 2. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
# 5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
# promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla.

import os

estudiantes = 5
calificaciones = 3
nombres_estudiantes = []
promedios = []

for i in range(1,estudiantes+1):
    os.system("cls || clear")
    print(f"Estudiante {i}")
    nombre = input(f"Escriba el nombre del estudiante\n-> ").strip().capitalize()
    nombres_estudiantes.append(nombre)
    calificacion = 0
    calificando = 0
    print(" ")
    for j in range(1,calificaciones+1):
        calificacion = int(input(f"Introduzca la calificacion numero {j}: "))
        calificando += calificacion

    promedio = calificando / calificaciones
    promedios.append(promedio)

os.system("cls || clear")
posicion = 0
for k in nombres_estudiantes:
    print(f"El promedio del estudiante {k} es de: {promedios[posicion]}%")
    posicion += 1