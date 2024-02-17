import tkinter as tk
from tkinter import ttk
import subprocess

class Opcion:
    def __init__(self, menu_principal):
        self.menu_principal = menu_principal
        self.menu_principal.title("MENÚ PRINCIPAL")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Configurar el tamaño de la ventana para que se ajuste a la pantalla
        ancho = self.menu_principal.winfo_screenwidth()
        alto = self.menu_principal.winfo_screenheight()
        self.menu_principal.geometry(f"{ancho}x{alto}")

        # Configurar color de fondo de la ventana
        self.menu_principal.configure(bg="#3b598d")

        # Marco para los botones
        self.marco = tk.Frame(self.menu_principal, bg="#3b598d")
        self.marco.pack()

        # Etiqueta con el título
        self.titulo = tk.Label(self.marco, text="MENÚ DE ELECCIÓN DE OPERACIÓN", font=("Serif", 30), fg="white", bg="#3b598d")
        self.titulo.pack(pady=10)

        # Lista de nombres de operaciones y funciones correspondientes
        operaciones = [
            ("Punto Medio", self.abrir_punto_medio),
            ("Distancia Dos Puntos", self.abrir_distancia_dos_puntos),
            ("Distancia Punto Recta", self.abrir_distancia_punto_recta),
            ("Ecuación Recta Pendiente", self.abrir_ecuacion_recta_pendiente),
            ("Ecuación Recta Dos Puntos", self.abrir_ecuacion_recta_dos_puntos),
            ("Ecuación Recta Paralela", self.abrir_ecuacion_recta_paralela),
            ("Ecuación Recta Perpendicular", self.abrir_ecuacion_recta_perpendicular),
            ("Ecuación Circunferencia", self.abrir_ecuacion_circunferencia),
            ("Ecuación Circunferencia Tres Puntos", self.abrir_ecuacion_circunferencia_tres_puntos),
            ("Foco Parabola", self.abrir_foco_parabola),
            ("Tangente Parabola", self.abrir_tangente_parabola),
            ("Interseccion", self.abrir_interseccion),
            ("Salir", self.salir)
        ]

        # Crear botones para cada operación con un estilo personalizado
        for nombre, funcion in operaciones:
            estilo_boton = ttk.Style()
            estilo_boton.configure(f"Estilo.{nombre}.TButton", font=("Helvetica", 13), padding=9, background="#fefefe")
            boton = ttk.Button(self.marco, text=nombre, style=f"Estilo.{nombre}.TButton", command=funcion)
            boton.pack(pady=2)

    # Métodos de apertura de las operaciones
    def abrir_programa(self, nombre_programa):
        subprocess.Popen(["python", nombre_programa])

    def abrir_punto_medio(self):
        self.abrir_programa("puntomedio.py")

    def abrir_distancia_dos_puntos(self):
        self.abrir_programa("distanciadospuntos.py")
    
    def abrir_distancia_punto_recta(self):
        self.abrir_programa("distanciapuntorecta.py")

    def abrir_ecuacion_recta_pendiente(self):
        self.abrir_programa("ecuacionrectapendiente.py")

    def abrir_ecuacion_recta_dos_puntos(self):
        self.abrir_programa("ecuacionrectadospuntos.py")

    def abrir_ecuacion_recta_paralela(self):
        self.abrir_programa("ecuacionrectaparalela.py")

    def abrir_ecuacion_recta_perpendicular(self):
        self.abrir_programa("ecuacionrectaperpendicular.py")

    def abrir_ecuacion_circunferencia(self):
        self.abrir_programa("ecuacioncircunferencia.py")

    def abrir_ecuacion_circunferencia_tres_puntos(self):
        self.abrir_programa("ecuacioncircunferenciatrespuntos.py")

    def abrir_foco_parabola(self):
        self.abrir_programa("focoparabola.py")

    def abrir_tangente_parabola(self):
        self.abrir_programa("tangenteparabola.py")

    def abrir_interseccion(self):
        self.abrir_programa("interseccion.py")

    def salir(self):
        self.menu_principal.destroy()

def menu():
    ventana = tk.Tk()
    app = Opcion(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    menu()
