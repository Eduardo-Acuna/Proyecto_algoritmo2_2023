import tkinter as tk
from tkinter import ttk

# Clase que representa la aplicación
class CalculadoraApp:
    def __init__(self):
        self.menuPrincipal = tk.Tk()
        self.menuPrincipal.title("MENÚ PRINCIPAL")

        # Estilo para los botones
        self.style = ttk.Style()
        self.style.configure("TButton", padding=10, font=("Helvetica", 14))

        # Crear una etiqueta con un título grande
        self.titulo = tk.Label(self.menuPrincipal, text="MENÚ DE ELECCIÓN DE OPERACIÓN", font=("Helvetica", 20))
        self.titulo.pack(pady=20)

        # Obtener el tamaño de la pantalla
        self.ancho = self.menuPrincipal.winfo_screenwidth()
        self.alto = self.menuPrincipal.winfo_screenheight()

        # Configurar el tamaño de la ventana para que se ajuste a la pantalla
        self.menuPrincipal.geometry(f"{self.ancho}x{self.alto}")

        # Botones
        self.crear_boton("Punto Medio de un Segmento", self.crear_ventana, "PUNTO MEDIO DE UN SEGMENTO")
        self.crear_boton("Distancia entre dos puntos", self.crear_ventana, "DISTANCIA ENTRE DOS PUNTOS")
        self.crear_boton("Distancia entre un punto a una recta", self.crear_ventana, "DISTANCIA DE UN PUNTO A UNA RECTA")
        self.crear_boton("Ecuación de recta por un punto y la pendiente", self.crear_ventana, "ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE")
        self.crear_boton("Ecuación de recta por dos puntos", self.crear_ventana, "ECUACIÓN DE RECTA POR DOS PUNTOS")
        self.crear_boton("Ecuación de recta paralela a una recta por un punto", self.crear_ventana, "ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO")
        self.crear_boton("Ecuación de recta perpendicular a una recta por un punto", self.crear_ventana, "ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO")
        self.crear_boton("Ecuación de circunferencia con centro y radio", self.crear_ventana, "ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO")
        self.crear_boton("Ecuación de circunferencia por tres puntos", self.crear_ventana, "ECUACIÓN DE RECTA PERPENDICULAR A UN PUNTO")
        self.crear_boton("Hallar foco de una parábola", self.crear_ventana, "HALLAR FOCO DE UNA PARÁBOLA")
        self.crear_boton("Tangente a una parábola por un punto extremo", self.crear_ventana, "TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO")
        self.crear_boton("Intersección", self.crear_ventana, "INTERSECCIÓN")
        self.crear_boton("SALIR", self.salir)

    def crear_ventana(self, titulo):
        ventana = tk.Toplevel(self.menuPrincipal)
        ventana.title(titulo)
        ventana.geometry("1000x600")
        etiqueta = tk.Label(ventana, text="Esta es una nueva ventana")
        etiqueta.pack()

    def crear_boton(self, texto, comando, argumento=None):
        boton = ttk.Button(self.menuPrincipal, text=texto, command=lambda: comando(argumento) if argumento else comando, style="TButton")
        boton.pack()

    def salir(self):
        self.menuPrincipal.destroy()

    def ejecutar(self):
        self.menuPrincipal.mainloop()

# Instanciar y ejecutar la aplicación
app = CalculadoraApp()
app.ejecutar()
