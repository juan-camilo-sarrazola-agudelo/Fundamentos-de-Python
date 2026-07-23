# LAB - Operadores y expresiones
# Objetivo: combinar variables y operadores para construir expresiones

precio_producto = 50000
cantidad = 3
descuento = 0.10  # 10%

subtotal = precio_producto * cantidad
total_con_descuento = subtotal - (subtotal * descuento)

print(f"Subtotal de la compra: {subtotal}")
print(f"Total con descuento del {int(descuento*100)}%: {total_con_descuento}")

# Operadores de asignacion compuestos
contador = 0
contador += 1
contador += 1
print(f"El contador quedo en: {contador}")

# Expresion con operadores logicos
tiene_cupon = True
compra_mayor_a_20000 = subtotal > 20000

if tiene_cupon and compra_mayor_a_20000:
    print("Aplica descuento adicional")
else:
    print("No aplica descuento adicional")
