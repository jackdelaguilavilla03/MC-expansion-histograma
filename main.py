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

        self.expander_boton = tk.Button(self, text="Ecualizar histograma", command=self.ecualizar_histograma)
        self.expander_boton.pack(side="right")

        self.equal_boton = tk.Button(self,text="Expandir histograma", command=self.expandir_histograma)
        self.equal_boton.pack(side="right")

    def cargar_imagen(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            if os.path.isfile(ruta_archivo) and (
                    ruta_archivo.endswith(".png") or ruta_archivo.endswith(".jpg") or ruta_archivo.endswith(
                    ".jpeg") or ruta_archivo.endswith(".bmp")):
                self.imagen_original = Image.open(ruta_archivo)
                self.imagen_original.thumbnail((400, 400))
                self.imagen_tk = ImageTk.PhotoImage(self.imagen_original)
                self.imagen_label.config(image=self.imagen_tk)
                self.histograma_original = cv2.calcHist([np.array(self.imagen_original.convert('L'))], [0], None, [256],
                                                        [0, 256])
                self.graficar_histograma(self.histograma_original)

    def ecualizar_histograma(self):
        imagen_gris = np.array(self.imagen_original.convert('L'))
        imagen_ecualizada = cv2.equalizeHist(imagen_gris)
        self.imagen_ecualizada = Image.fromarray(imagen_ecualizada)
        self.imagen_ecualizada.thumbnail((400, 400))
        self.imagen_ecualizada_tk = ImageTk.PhotoImage(self.imagen_ecualizada)
        self.imagen_label.config(image=self.imagen_ecualizada_tk)
        histograma_ecualizado = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])
        self.graficar_histograma(histograma_ecualizado)

    def expandir_histograma(self):
        imagen_gris = np.array(self.imagen_original.convert('L'))
        min_pixel = np.min(imagen_gris)
        max_pixel = np.max(imagen_gris)
        a = 255.0 / (max_pixel - min_pixel)
        b = -a * min_pixel
        imagen_expandida = (a * imagen_gris + b).astype(np.uint8)
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
root.geometry("700x600")
app = VentanaPrincipal(master=root)
app.mainloop()
