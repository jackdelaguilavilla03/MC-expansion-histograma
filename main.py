import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
            self.imagen_original = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
            self.imagen_tk = ImageTk.PhotoImage(Image.fromarray(self.imagen_original).resize((400, 400)))
            self.imagen_label.config(image=self.imagen_tk)
            self.histograma_original = cv2.calcHist([self.imagen_original], [0], None, [256], [0,256])
            self.graficar_histograma(self.histograma_original)

    def expandir_histograma(self):
        imagen_expandida = cv2.equalizeHist(self.imagen_original)
        histograma_expandido = cv2.calcHist([imagen_expandida], [0], None, [256], [0,256])
        imagen_expandida_tk = ImageTk.PhotoImage(Image.fromarray(imagen_expandida).resize((400, 400)))
        self.imagen_label.config(image=imagen_expandida_tk)
        self.graficar_histograma(histograma_expandido)

    def graficar_histograma(self, histograma):
        plt.clf()
        plt.bar(range(256), histograma.ravel())
        plt.xlim([0, 256])
        plt.xlabel("Intensidad de pixel")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.savefig("histograma.png")
        histograma_tk = ImageTk.PhotoImage(Image.open("histograma.png").resize((400, 200)))
        self.histograma_label.config(image=histograma_tk)
        self.histograma_label.image = histograma_tk

root = tk.Tk()
root.geometry("900x500")
app = VentanaPrincipal(master=root)
app.mainloop()
