import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import sqrt
from clase_geo_Gral import*
from funcion_geo_Gral import* # mas pequeño
from Funcion_Gral import* # copiamos aqui

# Función que calcula la distancia entre dos puntos y muestra el gráfico
def calcular_distancia_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())
    x2 = float(entrada_x2.get())
    y2 = float(entrada_y2.get())

    punto1 = Punto(x1 , y1)
    punto2 = Punto(x2 , y2)

    distancia = punto1.distancia_punto(punto2)

    resultado.set(f"Distancia A y B: {distancia:.2f}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")  # Ajustar tamaño y color

    # Crear un gráfico de dispersión en Matplotlib
    ax.clear()  # Limpia el gráfico anterior

    ax.scatter(x1, y1, color='red', label='Punto A')
    ax.scatter(x2, y2, color='green', label='Punto B')
    ax.plot([x1, x2], [y1, y2], color='blue', label='Línea que conecta los puntos')
    ax.legend()
    ax.set_title('Distancia entre Punto A y Punto B')
    canvas.draw()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x1.delete(0, 'end')
    entrada_y1.delete(0, 'end')
    entrada_x2.delete(0, 'end')
    entrada_y2.delete(0, 'end')
    resultado.set("")
    ax.clear()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Distancia entre Puntos con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Distancia Dos Puntos", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para las coordenadas y el resultado
entrada_x1 = tk.Entry(ventana, width=13)
entrada_y1 = tk.Entry(ventana, width=13)
entrada_x2 = tk.Entry(ventana, width=13)
entrada_y2 = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo1 = tk.Label(ventana, text="PUNTO A", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=1, column=0, columnspan=2)
etiqueta_x1 = tk.Label(ventana, text="X1: ", fg="white", bg="#3b598d")
etiqueta_y1 = tk.Label(ventana, text="Y1: ", fg="white", bg="#3b598d")
etiqueta_x1.grid(row=2, column=0)
etiqueta_y1.grid(row=3, column=0)
entrada_x1.grid(row=2, column=1)
entrada_y1.grid(row=3, column=1)

subtitulo2 = tk.Label(ventana, text="PUNTO B", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo2.grid(row=4, column=0, columnspan=2)
etiqueta_x2 = tk.Label(ventana, text="X2: ", fg="white", bg="#3b598d")
etiqueta_y2 = tk.Label(ventana, text="Y2: ", fg="white", bg="#3b598d")
etiqueta_x2.grid(row=5, column=0)
etiqueta_y2.grid(row=6, column=0)
entrada_x2.grid(row=5, column=1)
entrada_y2.grid(row=6, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Distancia y Gráfico", command=calcular_distancia_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=2)
boton_limpiar.grid(row=9, column=0)
boton_salir.grid(row=10, column=0, columnspan=2)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
