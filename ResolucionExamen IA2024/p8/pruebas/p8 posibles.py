import random
import math

# Definir los nodos del grafo
#nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
nodos = ['A', 'B', 'C']

# Número total de combinaciones a mostrar
total_combinaciones = math.factorial(len(nodos))

# Almacenar las combinaciones generadas
combinaciones_generadas = set()

# Generar combinaciones hasta alcanzar el total
while len(combinaciones_generadas) < total_combinaciones:
    # Generar una nueva combinación
    nueva_combinacion = tuple(random.sample(nodos, len(nodos)))
    
    # Si la combinación no se ha generado antes, la agregamos al conjunto
    if nueva_combinacion not in combinaciones_generadas:
        combinaciones_generadas.add(nueva_combinacion)
        print(f"Combinación {len(combinaciones_generadas)}: {nueva_combinacion}")


