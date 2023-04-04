from PIL import Image


def obtener_histograma(imagen):
    """
    Obtiene el histograma de la imagen dada.
    :param imagen: Objeto de imagen PIL.
    :return: Lista con el histograma de la imagen.
    """
    return imagen.histogram()


def expandir_histograma(imagen):
    """
    Expande el histograma de la imagen dada para mejorar su contraste.
    :param imagen: Objeto de imagen PIL.
    :return: Objeto de imagen PIL con el histograma expandido.
    """
    # Obtiene el histograma de la imagen
    histograma = obtener_histograma(imagen)

    # Calcula los valores mínimo y máximo del histograma
    min_valor = 0
    max_valor = 255
    for i in range(256):
        if histograma[i] != 0:
            min_valor = i
            break
    for i in range(255, -1, -1):
        if histograma[i] != 0:
            max_valor = i
            break

    # Expande el histograma
    imagen_expandida = imagen.point(lambda x: (x - min_valor) * 255 / (max_valor - min_valor) if max_valor != min_valor else 0)

    return imagen_expandida


def procesar_imagen(ruta_imagen):
    """
    Carga la imagen desde el archivo y la procesa para mejorar su contraste.
    :param ruta_imagen: Ruta de la imagen a procesar.
    :return: Objeto de imagen PIL con el histograma expandido.
    """
    # Carga la imagen desde el archivo
    imagen_original = Image.open(ruta_imagen)

    # Expande el histograma de la imagen
    imagen_expandida = expandir_histograma(imagen_original)

    return imagen_expandida
