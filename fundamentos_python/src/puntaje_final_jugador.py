# Proyecto integrador - Puntaje final de un jugador
# Aqui uso variables, literales y operadores matematicos y de comparacion
# vistos en las secciones 1 a 4 de la guia.

nombre_jugador = "Juan camilo"

# Puntajes obtenidos en 3 rondas del juego
puntos_ronda1 = 120
puntos_ronda2 = 95
puntos_ronda3 = 150

# Bono extra si el jugador completo las 3 rondas
bono_por_completar = 30

# Operador aritmetico: suma de puntos + bono
puntaje_total = puntos_ronda1 + puntos_ronda2 + puntos_ronda3 + bono_por_completar

# Operador aritmetico: promedio de puntos por ronda (sin el bono)
promedio_por_ronda = (puntos_ronda1 + puntos_ronda2 + puntos_ronda3) / 3

print(f"Jugador: {nombre_jugador}")
print(f"Puntos ronda 1: {puntos_ronda1}")
print(f"Puntos ronda 2: {puntos_ronda2}")
print(f"Puntos ronda 3: {puntos_ronda3}")
print(f"Bono por completar el juego: {bono_por_completar}")
print(f"Puntaje total: {puntaje_total}")
print(f"Promedio por ronda: {promedio_por_ronda:.2f}")

# Operador de comparacion: se define si el jugador gano una medalla
puntaje_minimo_medalla = 300

if puntaje_total >= puntaje_minimo_medalla:
    print(f"{nombre_jugador} obtuvo medalla, su puntaje fue mayor o igual a {puntaje_minimo_medalla}")
else:
    print(f"{nombre_jugador} no obtuvo medalla esta vez")
