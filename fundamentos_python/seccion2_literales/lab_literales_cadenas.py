# LAB - Literales de Python: Cadenas
# Objetivo: practicar distintos tipos de literales de cadena (strings)

# Cadenas simples con comillas simples y dobles
cadena1 = 'Hola'
cadena2 = "juan camilo sarrazola"
print(cadena1, cadena2)

# Cadenas con comillas triples (multilinea)
poema = """Este es un texto
que ocupa
varias lineas"""
print(poema)

# Caracteres de escape
print("Ella dijo: \"Python es facil\"")
print("Primera linea\nSegunda linea")
print("Columna1\tColumna2")

# Cadena cruda (raw string), no interpreta \n ni \t
ruta = r"C:\Users\estudiante\Documents"
print(ruta)

# Concatenacion de cadenas
saludo = "Hola" + " " + "a todos"
print(saludo)

# Repeticion de cadenas
linea = "-" * 20
print(linea)
