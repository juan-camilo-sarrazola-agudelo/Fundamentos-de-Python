# LAB - La función print() y sus argumentos
# Objetivo: usar los parametros sep y end de print()

# sep: cambia el separador entre los valores impresos
print("Python", "es", "genial", sep="-")

# end: cambia lo que se imprime al final (por defecto es un salto de linea)
print("Esta linea no salta al final...", end=" ")
print("porque use end=' '")

# combinando sep y end
print("uno", "dos", "tres", sep=" | ", end=" <-- fin\n")
