import random

def simular_canicas(num_canicas, num_niveles):
    resultados = []
    
    for _ in range(num_canicas):
        # Cuenta cuántas veces cae la canica a la derecha
        caidas_a_la_derecha = sum(random.choice([0, 1]) for _ in range(num_niveles))
        resultados.append(caidas_a_la_derecha)
    
    return resultados
import matplotlib.pyplot as plt

def graficar_histograma(resultados, num_niveles):
    # Generamos el histograma
    plt.hist(resultados, bins=num_niveles+1, edgecolor='black', density=True)
    
    # Títulos y etiquetas
    plt.title(f"Simulación de la Máquina de Galton con {len(resultados)} canicas y {num_niveles} niveles")
    plt.xlabel("Posición final (número de caídas a la derecha)")
    plt.ylabel("Frecuencia relativa")
    
    # Mostrar el gráfico
    plt.show()
# Parámetros
num_canicas = 3000
num_niveles = 12
probabilidad_min = 0.5
probabilidad_max = 0.95
# Simular las canicas
resultados = simular_canicas(num_canicas, num_niveles)

# Graficar el histograma
graficar_histograma(resultados, num_niveles)
