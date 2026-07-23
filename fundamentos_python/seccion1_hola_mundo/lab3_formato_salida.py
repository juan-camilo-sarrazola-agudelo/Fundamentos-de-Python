# LAB - Dando formato a la salida
# Objetivo: mostrar distintas formas de dar formato a un texto en Python

nombre = "juan camilo sarrazola"
edad = 37
promedio = 4.30

# Forma 1: concatenando con +
print("Hola " + nombre + ", tienes " + str(edad) + " años")

# Forma 2: usando comas en el print
print("Hola", nombre, ", tienes", edad, "años")

# Forma 3: f-strings (la mas usada y recomendada)
print(f"Hola {nombre}, tienes {edad} años y tu promedio es {promedio}")

# Forma 4: formateando decimales con f-strings
print(f"Tu promedio con 2 decimales es: {promedio:.2f}")
