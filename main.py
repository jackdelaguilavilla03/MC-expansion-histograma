import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import histograma
import image_processing

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.imagen_label = tk.Label(self)
        self.imagen_label.pack()

        self.histograma_label = tk.Label(self)
        self.histograma_label.pack()

        self.cargar_boton = tk.Button(self, text="Cargar imagen", command=self.cargar_imagen)
        self.cargar_boton.pack(side="left")

        self.expander_boton = tk.Button(self, text="Expandir histograma", command=self.expandir_histograma)
        self.expander_boton.pack(side="right")

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp")])
        if ruta_imagen:
            self.imagen_original = image_processing.procesar_imagen(ruta_imagen)
            imagen_redimensionada = self.imagen_original.resize((500, 500))  # Cambia las dimensiones a lo que necesites
            self.imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
            self.imagen_label.config(image=self.imagen_tk)
            self.histograma_original = histograma.obtener_histograma(imagen_redimensionada)
            self.graficar_histograma(self.histograma_original)

    def expandir_histograma(self):
        imagen_expandida = image_processing.expandir_histograma(self.imagen_original)
        histograma_expandido = histograma.obtener_histograma(imagen_expandida)
        self.imagen_expandida_tk = ImageTk.PhotoImage(imagen_expandida)

        # Crear figura con dos subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        # Mostrar imagen original en el primer subplot
        ax1.imshow(self.imagen_original, cmap="gray")
        ax1.set_title("Imagen original")

        # Mostrar imagen expandida en el segundo subplot
        ax2.imshow(imagen_expandida, cmap="gray")
        ax2.set_title("Imagen expandida")

        # Mostrar histograma expandido debajo del segundo subplot
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        ax3 = fig.add_subplot(3, 1, 3)
        ax3.bar(range(len(histograma_expandido)), histograma_expandido)
        ax3.set_title("Histograma expandido")

        canvas.draw()

    def graficar_histograma(self, histograma):
        canvas = tk.Canvas(self.histograma_label, width=400, height=200)
        canvas.pack()
        for i, valor in enumerate(histograma):
            x0 = i * 4
            y0 = 200 - (valor * 200 / max(histograma))
            x1 = (i + 1) * 4
            y1 = 200
            canvas.create_rectangle(x0, y0, x1, y1, fill="gray")
        canvas.update()


root = tk.Tk()
root.geometry("700x800")
app = VentanaPrincipal(master=root)
app.mainloop()

