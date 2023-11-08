import matplotlib.pyplot as plt
import numpy as np

def generar_colores(n):
    """Genera n colores aleatorios."""
    return ['#' + ''.join([f"{np.random.randint(0, 255):02x}" for _ in range(3)]) for _ in range(n)]

def dividir_pintar_marimekko(proporciones_x, proporciones_y):
    """Dibuja un gráfico de Marimekko con las proporciones dadas."""
    assert sum(proporciones_x) == 1, "Las proporciones horizontales deben sumar 1."
    assert sum(proporciones_y) == 1, "Las proporciones verticales deben sumar 1."

    colores = generar_colores(len(proporciones_x) * len(proporciones_y))
    color_idx = 0
    
    fig, ax = plt.subplots()
    inicio_x = 0
    
    for i, ancho in enumerate(proporciones_x):
        inicio_y = 0
        for j, alto in enumerate(proporciones_y):
            rect = plt.Rectangle((inicio_x, inicio_y), ancho, alto, facecolor=colores[color_idx])
            ax.add_patch(rect)
            inicio_y += alto
            color_idx += 1
        inicio_x += ancho

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

# Ejemplo de uso:
proporciones_horizontales = [0.3, 0.2, 0.5]  # deben sumar 1
proporciones_verticales = [0.4, 0.3, 0.3]    # deben sumar 1

dividir_pintar_marimekko(proporciones_horizontales, proporciones_verticales)
