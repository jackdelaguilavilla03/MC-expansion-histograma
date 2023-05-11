# Expansión de histograma

El proyecto es una aplicación de procesamiento de imágenes que permite cargar imágenes, aplicar filtros de ecualización y expansión de histograma, y visualizar los resultados en una interfaz gráfica de usuario. Utiliza la biblioteca tkinter para crear la interfaz de usuario y las bibliotecas PIL, cv2, numpy y matplotlib para el procesamiento de imágenes y generación de histogramas. El objetivo del proyecto es proporcionar una herramienta sencilla y fácil de usar para mejorar la calidad visual de las imágenes mediante técnicas de procesamiento de histogramas.

## Requisitos

- Python >= (versión 9.0)
- pip >=(versión 20.1)

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.

```bash
git clone https://github.com/jackdelaguilavilla03/MC-expansion-histograma.git
```

2. Crea un entorno virtual con Python.

```bash
python -m venv myenv
```

3. Activa el entorno virtual.

Windows:
```bash
myenv\Scripts\activate
```

MacOS/Linux:
```bash
source myenv/bin/activate
```

4. Instala las dependencias del proyecto.

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta el programa principal.
```bash
python main.py
```
2. Interactúa con la interfaz de usuario para cargar imágenes, aplicar filtros, etc.

3. Realiza las acciones deseadas y observa los resultados en la interfaz.

4. (Opcional) Para generar un ejecutable independiente:
```bash
pyinstaller --onefile --noconsole main.py
```
5. El ejecutable generado estará ubicado en la carpeta `dist`.

## Contribuciones

Las solicitudes de extracción son bienvenidas. Para cambios importantes, primero abra un problema para discutir qué le gustaría cambiar.

Asegúrese de actualizar las pruebas según corresponda.

## Licencia

[MIT License](https://choosealicense.com/licenses/mit/)
```

Recuerda personalizar la información en el README según las necesidades de tu proyecto, como el nombre del proyecto, la descripción, los requisitos específicos de Python y pip, y cualquier otra información relevante. También puedes incluir secciones adicionales, como una sección de "Características" o "Ejemplos de uso", si deseas proporcionar más detalles sobre el proyecto.

Espero que esto te ayude a crear el README para tu proyecto. ¡Si tienes más preguntas, no dudes en hacerlas!
```
## Recursos

- [Documentación de Markdown](https://www.markdownguide.org/basic-syntax/)
- [Documentación de PyInstaller](https://pyinstaller.readthedocs.io/en/stable/)
- [Documentación de PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [Documentación de Pillow](https://pillow.readthedocs.io/en/stable/)
- [Documentación de NumPy](https://numpy.org/doc/)
- [Documentación de Matplotlib](https://matplotlib.org/contents.html)
- [Documentación de OpenCV](https://docs.opencv.org/master/)
- [Documentación de Scikit-Image](https://scikit-image.org/docs/stable/)