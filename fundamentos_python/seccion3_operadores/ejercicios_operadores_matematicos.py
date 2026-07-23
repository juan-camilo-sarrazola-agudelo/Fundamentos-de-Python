# Sección 3 - Ejercicios de Operadores Matemáticos
# Objetivo: practicar los operadores aritméticos, de comparación y asignación

a = 15
b = 4

print("=== Operadores Aritméticos ===")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicacion: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Division entera: {a} // {b} = {a // b}")
print(f"Modulo (residuo): {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

print("\n=== Operadores de Comparación ===")
print(f"{a} == {b} -> {a == b}")
print(f"{a} != {b} -> {a != b}")
print(f"{a} > {b} -> {a > b}")
print(f"{a} < {b} -> {a < b}")
print(f"{a} >= {b} -> {a >= b}")
print(f"{a} <= {b} -> {a <= b}")

print("\n=== Ejercicio aplicado: calcular el área de un rectángulo ===")
base = 8
altura = 5
area = base * altura
print(f"El area de un rectangulo de base {base} y altura {altura} es {area}")

print("\n=== Ejercicio aplicado: promedio de 3 notas ===")
nota1 = 4.5
nota2 = 3.8
nota3 = 4.0
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es: {promedio:.2f}")

if promedio >= 3.0:
    print("El estudiante aprobó la materia")
else:
    print("El estudiante no aprobó la materia")
