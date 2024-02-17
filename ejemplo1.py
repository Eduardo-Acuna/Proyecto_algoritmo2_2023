import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas

# Función para calcular la ecuación general y mostrar el gráfico
def calcular_ecuacion_general_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())
    pendiente = float(entrada_pendiente.get())

    # Asegurarse de que la pendiente sea positiva
    if pendiente < 0:
        pendiente = -pendiente

    # Ecuación general de la recta: Ax + By - C = 0
    A = pendiente
    B = -1
    C = pendiente * x1 - y1

    # Crear la ecuación general como cadena
    ecuacion_general = f'{A}x + {B}y - {abs(C)} = 0'

    # Crear la ecuación de la pendiente
    ecuacion_pendiente = f'y = {pendiente}(x - {x1}) + {y1}'

    resultado.set(f"Ecuación de la Recta:\n{ecuacion_general}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la recta en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    x = [x1 - 5, x1 + 5]
    y = [( ( ( A*x1 + C )-1 ) / B ) - 5 , ( ( ( A*x1 + C )-1 ) / B ) + 5]

    plt.scatter(x1, y1, color='red', label='Punto A', marker='o')
    plt.plot(x, y, color='blue', label=f'Recta ({ecuacion_general})')

    plt.legend()
    plt.title('Recta')

    # Agregar ejes X e Y definidos
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    canvas.draw()

# Resto del código...

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Recta con Gráfico")
ventana.grid_columnconfigure(0, minsize=125)
ventana.configure(bg="#3b598d")

# Etiquetas y entradas de usuario
# ... (código anterior)

# Etiqueta y entrada para la pendiente
etiqueta_pendiente = tk.Label(ventana, text="Pendiente:", fg="white", bg="#3b598d")
etiqueta_pendiente.grid(row=7, column=0)
entrada_pendiente = tk.Entry(ventana, width=13)
entrada_pendiente.grid(row=7, column=1)

# Resto del código...

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=3, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
