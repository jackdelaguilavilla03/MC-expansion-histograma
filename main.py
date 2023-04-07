import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


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
        # ruta_imagen = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp")])
        # if ruta_imagen:
        #     self.imagen_original = Image.open(ruta_imagen)
        #     self.imagen_original.thumbnail((400, 400))
        #     self.imagen_tk = ImageTk.PhotoImage(self.imagen_original)
        #     self.imagen_label.config(image=self.imagen_tk)
        #     self.histograma_original = cv2.calcHist([np.array(self.imagen_original.convert('L'))], [0], None, [256],
        #                                             [0, 256])
        #     self.graficar_histograma(self.histograma_original)
        carpeta_imagen = filedialog.askdirectory()
        if carpeta_imagen:
            nombres_archivos = os.listdir(carpeta_imagen)
            for nombre_archivo in nombres_archivos:
                if nombre_archivo.endswith(".png") or nombre_archivo.endswith(".jpg") or nombre_archivo.endswith(
                        ".jpeg") or nombre_archivo.endswith(".bmp"):
                    ruta_imagen = os.path.join(carpeta_imagen, nombre_archivo)
                    self.imagen_original = Image.open(ruta_imagen)
                    self.imagen_original.thumbnail((400, 400))
                    self.imagen_tk = ImageTk.PhotoImage(self.imagen_original)
                    self.imagen_label.config(image=self.imagen_tk)
                    self.histograma_original = cv2.calcHist([np.array(self.imagen_original.convert('L'))], [0], None,
                                                            [256],
                                                            [0, 256])
                    self.graficar_histograma(self.histograma_original)
                    break

    def expandir_histograma(self):
        imagen_gris = np.array(self.imagen_original.convert('L'))
        imagen_expandida = cv2.equalizeHist(imagen_gris)
        self.imagen_expandida = Image.fromarray(imagen_expandida)
        self.imagen_expandida.thumbnail((400, 400))
        self.imagen_expandida_tk = ImageTk.PhotoImage(self.imagen_expandida)
        self.imagen_label.config(image=self.imagen_expandida_tk)
        histograma_expandido = cv2.calcHist([imagen_expandida], [0], None, [256], [0, 256])
        self.graficar_histograma(histograma_expandido)

    def graficar_histograma(self, histograma):
        plt.clf()
        plt.plot(histograma)
        plt.title("Histograma")
        plt.xlim([0, 256])
        plt.ylim([0, 5000])
        plt.xlabel("Intensidad de pixel")
        plt.ylabel("Cantidad de pixels")
        plt.tight_layout()
        plt.savefig('histograma.png')
        histograma_imagen = Image.open('histograma.png')
        histograma_imagen.thumbnail((300, 150))
        histograma_imagen_tk = ImageTk.PhotoImage(histograma_imagen)
        self.histograma_label.config(image=histograma_imagen_tk)
        self.histograma_label.image = histograma_imagen_tk


root = tk.Tk()
root.geometry("700x500")
app = VentanaPrincipal(master=root)
app.mainloop()
