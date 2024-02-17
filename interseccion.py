import tkinter as tk
from tkinter import ttk

class CalculadoraInterseccion:
    def __init__(self, ventana):
        self.ventana_interseccion = ventana
        self.ventana_interseccion.title("Calculadora de Intersección")
        self.ventana_interseccion.configure(bg="#3b598d")
        self.ventana_interseccion.grid_columnconfigure(0, minsize=910)

        self.estilo = ttk.Style()
        self.estilo.configure('EstiloBoton.TButton', padding=(20, 10))

        self.titulo = tk.Label(self.ventana_interseccion, text="Intersección", font=("Serif", 30), fg="white", bg="#3b598d")
        self.titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

        self.boton_recta_parabola = ttk.Button(self.ventana_interseccion, text="Recta y Parábola", command=self.calcular_interseccion_recta_parabola, style='EstiloBoton.TButton')
        self.boton_recta_circunferencia = ttk.Button(self.ventana_interseccion, text="Recta y Circunferencia", command=self.calcular_interseccion_recta_circunferencia, style='EstiloBoton.TButton')
        self.boton_circunferencia_parabola = ttk.Button(self.ventana_interseccion, text="Circunferencia y Parábola", command=self.calcular_interseccion_circunferencia_parabola, style='EstiloBoton.TButton')
        self.boton_salir = ttk.Button(self.ventana_interseccion, text="Salir", command=self.salir, style='EstiloBoton.TButton')

        self.boton_recta_parabola.grid(row=1, column=0, columnspan=10, pady=10)
        self.boton_recta_circunferencia.grid(row=2, column=0, columnspan=10, pady=10)
        self.boton_circunferencia_parabola.grid(row=3, column=0,columnspan=10, pady=10)
        self.boton_salir.grid(row=4, column=0, columnspan=10, pady=10)

    def calcular_interseccion_recta_parabola(self):
        self.ventana_interseccion.quit()
        try:
            from interseccion_recta_parabola import calcular_interseccion_recta_parabola as calcular
            calcular()
        except ImportError:
            print("Archivo interseccion_recta_parabola.py no encontrado.")

    def calcular_interseccion_recta_circunferencia(self):
        try:
            from interseccion_recta_circunferencia import calcular_interseccion_recta_circunferencia as calcular
            calcular()
        except ImportError:
            print("Archivo interseccion_recta_circunferencia.py no encontrado.")

    def calcular_interseccion_circunferencia_parabola(self):
        try:
            from interseccion_circunferencia_parabola import calcular_interseccion_circunferencia_parabola as calcular
            calcular()
        except ImportError:
            print("Archivo interseccion_circunferencia_parabola.py no encontrado.")

    def salir(self):
        self.ventana_interseccion.quit()

def interseccion_menu():
    ventana_interseccion = tk.Tk()
    app = CalculadoraInterseccion(ventana_interseccion)
    ventana_interseccion.mainloop()

if __name__ == "__main__":
    interseccion_menu()