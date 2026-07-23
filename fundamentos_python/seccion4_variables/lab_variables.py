# LAB - Variables
# Objetivo: declarar variables de distintos tipos y mostrar su valor y tipo

nombre = "Andres"          # str
edad = 22                  # int
estatura = 1.75            # float
es_estudiante = True       # bool

print(nombre, type(nombre))
print(edad, type(edad))
print(estatura, type(estatura))
print(es_estudiante, type(es_estudiante))

# reasignacion de variables
edad = edad + 1
print(f"El proximo año {nombre} tendra {edad} años")
