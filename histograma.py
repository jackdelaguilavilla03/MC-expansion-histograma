from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def obtener_histograma(imagen):
    # Convertir imagen a escala de grises
    imagen_gris = imagen.convert('L')
    # Obtener histograma
    histograma = np.array(imagen_gris.histogram())
    return histograma


def graficar_histograma(imagen):
    # Obtener histograma
    histograma = obtener_histograma(imagen)
    # Graficar histograma
    plt.bar(range(len(histograma)), histograma)
    plt.title('Histograma')
    plt.xlabel('Valor de intensidad')
    plt.ylabel('Frecuencia')
    plt.show()

