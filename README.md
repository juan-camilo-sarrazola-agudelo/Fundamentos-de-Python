# Fundamentos de Python - GA1-220501093-04-AA1-EV01

Repositorio del proyecto de clase para la actividad de **Fundamentos de Python**, donde se trabajan variables, literales, operadores y manejo básico de cadenas.

## Estructura del repositorio

```
fundamentos_python/
├── seccion1_hola_mundo/
│   ├── lab1_print_basico.py
│   ├── lab2_print_argumentos.py
│   └── lab3_formato_salida.py
├── seccion2_literales/
│   └── lab_literales_cadenas.py
├── seccion3_operadores/
│   └── ejercicios_operadores_matematicos.py
├── seccion4_variables/
│   ├── lab_variables.py
│   ├── lab_convertidor_simple.py
│   └── lab_operadores_expresiones.py
└── src/
    └── puntaje_final_jugador.py
```

Cada carpeta corresponde a una sección de la guía y contiene los laboratorios trabajados.

## Cómo ejecutar los programas

Se necesita tener Python 3 instalado. Desde la raíz del proyecto se ejecuta cada script así:

```bash
python3 seccion1_hola_mundo/lab1_print_basico.py
python3 seccion3_operadores/ejercicios_operadores_matematicos.py
python3 src/puntaje_final_jugador.py
```

Y así con cualquiera de los demás archivos.

## Ejercicios de operadores matemáticos (Sección 3)

En el archivo `seccion3_operadores/ejercicios_operadores_matematicos.py` se resuelven los ejercicios de la sección de operadores. La idea es usar dos variables (`a = 15`, `b = 4`) y probar sobre ellas los operadores aritméticos y de comparación.

### Operadores aritméticos usados

| Operador | Significado | Ejemplo (a=15, b=4) | Resultado |
|----------|-------------|----------------------|-----------|
| `+`  | Suma                | `15 + 4`  | `19` |
| `-`  | Resta               | `15 - 4`  | `11` |
| `*`  | Multiplicación      | `15 * 4`  | `60` |
| `/`  | División real       | `15 / 4`  | `3.75` |
| `//` | División entera     | `15 // 4` | `3` |
| `%`  | Módulo (residuo)    | `15 % 4`  | `3` |
| `**` | Potencia            | `15 ** 4` | `50625` |

**Lógica:** la división normal (`/`) siempre entrega un número decimal, mientras que la división entera (`//`) descarta los decimales y deja solo la parte entera. El módulo (`%`) es útil para saber si un número es divisible por otro (si el resultado es 0, es divisible).

### Operadores de comparación usados

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a        | `15 == 4` | `False` |
| `!=` | Diferente de   | `15 != 4` | `True`  |
| `>`  | Mayor que      | `15 > 4`  | `True`  |
| `<`  | Menor que      | `15 < 4`  | `False` |
| `>=` | Mayor o igual  | `15 >= 4` | `True`  |
| `<=` | Menor o igual  | `15 <= 4` | `False` |

Estos operadores devuelven siempre un valor booleano (`True` o `False`), y por eso se usan mucho en condicionales (`if`).

### Ejemplos aplicados

Además de los ejercicios básicos, se resolvieron dos casos prácticos:

- **Área de un rectángulo:** usando el operador `*` con `base = 8` y `altura = 5`, el área da `40`.
- **Promedio de 3 notas:** se suman las 3 notas y se dividen entre 3 con el operador `/`. Con las notas `4.5`, `3.8` y `4.0` el promedio es `4.10`, y como es mayor o igual a `3.0` (operador `>=`) el programa indica que el estudiante aprobó.

### Salida en consola del script de operadores

```
=== Operadores Aritméticos ===
Suma: 15 + 4 = 19
Resta: 15 - 4 = 11
Multiplicacion: 15 * 4 = 60
Division: 15 / 4 = 3.75
Division entera: 15 // 4 = 3
Modulo (residuo): 15 % 4 = 3
Potencia: 15 ** 4 = 50625

=== Operadores de Comparación ===
15 == 4 -> False
15 != 4 -> True
15 > 4 -> True
15 < 4 -> False
15 >= 4 -> True
15 <= 4 -> False

=== Ejercicio aplicado: calcular el área de un rectángulo ===
El area de un rectangulo de base 8 y altura 5 es 40

=== Ejercicio aplicado: promedio de 3 notas ===
El promedio de las notas es: 4.10
El estudiante aprobó la materia
```

## Proyecto integrador: puntaje final de un jugador

En `src/puntaje_final_jugador.py` se combina todo lo aprendido (variables, operadores aritméticos y de comparación) en un solo ejemplo: se suman los puntos de 3 rondas de un juego más un bono, se calcula el promedio por ronda, y con un operador de comparación (`>=`) se decide si el jugador se gana una medalla.

Salida de ejemplo:

```
Jugador: Juan camilo sarrazola
Puntos ronda 1: 120
Puntos ronda 2: 95
Puntos ronda 3: 150
Bono por completar el juego: 30
Puntaje total: 395
Promedio por ronda: 121.67
Juan obtuvo medalla, su puntaje fue mayor o igual a 300
```

## Recursos usados

- Guía "Fundamentos de Python" (Secciones 1 a 4).
- Documentación oficial de Python (tipos numéricos, cadenas y variables).
- Artículos sobre operadores en Python y concatenación de cadenas.

## Autor

Actividad individual - GA1-220501093-04-AA1-EV01.
