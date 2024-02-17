import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from fractions import Fraction
import numpy as np
from clase_geo_Gral import*
from funcion_geo_Gral import* # mas pequeño
from Funcion_Gral import* # copiamos aqui
from numpy import*

# Función para calcular la ecuación de la recta paralela y mostrar el gráfico
# Función para calcular la ecuación de la recta paralela y mostrar el gráfico
def calcular_recta_paralela_y_grafico():
    ecuacion_original = entrada_ecuacion.get()
    punto_x = float(entrada_x.get())
    punto_y = float(entrada_y.get())

    a , b , c = aux_encontrar_constantes_recta_float(aux_ordenar_ecuación_final_float(ecuacion_original))

    # Mostrar la ecuación de la recta paralela
    ecuacion_paralela = f'{Perpendicular(ecuacion_original , punto_x , punto_y).replace(" " , "")}'
    resultado.set(f"Ecuación de la Recta Paralela:\n{ecuacion_paralela}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Coeficientes para la recta paralela
    if punto_x is int and punto_y is int:
        a_paralela , b_paralela , c_paralela = aux_encontrar_constantes_recta(ecuacion_paralela)
    else:
        a_paralela , b_paralela , c_paralela = aux_encontrar_constantes_recta_float(ecuacion_paralela)

    # Crear un gráfico de las dos rectas
    plt.cla()  # Limpia el gráfico anterior

    # Crear un rango de valores para X
    x_values = np.linspace(-10, 10, 400)

    # Calcular los valores correspondientes de Y para la recta original y la recta paralela
    y_values_original = (-a * x_values - c) / b
    y_values_paralela = (-a * x_values - c_paralela) / b

    # Dibujar la recta original de color azul
    plt.plot(x_values, y_values_original, color='blue', label=f'Recta Original: {ecuacion_original}')

    # Dibujar la recta paralela de color rojo
    plt.plot(x_values, y_values_paralela, color='red', label=f'Recta Paralela: {ecuacion_paralela}')

    # Dibujar el punto A en el gráfico
    plt.scatter(punto_x, punto_y, color='green', label='Punto A', s=80, marker='o')

    # Mostrar la leyenda
    plt.legend()
    plt.title('Recta Original y Recta Paralela')

    # Definir ejes X e Y y ajustar los límites
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

    # Ajustar los límites del gráfico
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    canvas.draw()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_ecuacion.delete(0, 'end')
    entrada_x.delete(0, 'end')
    entrada_y.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Recta Paralela con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=200)

# Crear variables para la ecuación y el resultado
entrada_ecuacion = tk.Entry(ventana, width=20)
entrada_x = tk.Entry(ventana, width=20)
entrada_y = tk.Entry(ventana, width=20)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="Ecuación de la Recta (ax + by + c = 0)", font=("Helvetica", 13))
subtitulo.grid(row=0, column=0, columnspan=2, pady=(10, 0))

etiqueta_ecuacion = tk.Label(ventana, text="Ecuación de la Recta Original: ")
etiqueta_ecuacion.grid(row=1, column=0)
entrada_ecuacion.grid(row=1, column=1)

etiqueta_punto = tk.Label(ventana, text="Punto A (Coordenadas): ")
etiqueta_punto.grid(row=2, column=0)
entrada_x.grid(row=2, column=1)
entrada_y.grid(row=2, column=2)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=3, column=0, columnspan=3, pady=(10, 0))

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Recta Paralela y Gráfico", command=calcular_recta_paralela_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=4, column=0, columnspan=2, pady=(10, 0))
boton_limpiar.grid(row=5, column=0, pady=(10, 0))
boton_salir.grid(row=5, column=1, pady=(10, 0))

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=3, rowspan=4, padx=(20, 0))

# Iniciar el bucle principal de Tkinter
ventana.mainloop()