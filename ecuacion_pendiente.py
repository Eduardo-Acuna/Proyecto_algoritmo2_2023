import cmd
import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from fractions import Fraction
from clase_geo_Gral import*
from funcion_geo_Gral import* # mas pequeño
from Funcion_Gral import* # copiamos aqui
from numpy import*

#Función para calcular la ecuación de la recta y mostrar el gráfico
#Función para calcular la ecuación de la recta y mostrar el gráfico
def calcular_ecuacion_general_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())

    numerador = float(entrada_numerador.get())
    denominador =float(entrada_denominador.get())

    # Calcular los coeficientes de la ecuación de la recta
    a = m
    b = -1
    c = y1 - m * x1

    # Convertir los coeficientes a fracciones si son números decimales
    a_frac = Fraction(a).limit_denominator()
    b_frac = Fraction(b).limit_denominator()
    c_frac = Fraction(c).limit_denominator()

    # Mostrar la ecuación general en fracciones
    ecuacion = f"{a_frac}x {'+' if b_frac >= 0 else '-'} {abs(b_frac)}y {'+' if c_frac >= 0 else '-'} {abs(c_frac)} = 0"
    resultado.set(f"Ecuación de la Recta:\n{ecuacion}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

#Constantes
    #A , B , C = aux_encontrar_constantes_recta_float(ecuacion)

    # Crear un gráfico de la recta en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    x = [x1 - 5, x1 + 5]
    y = [m * (x1 - 5) + c, m * (x1 + 5) + c]

    # ( ( ( Ax + C )-1 ) / B ) - 5 , ( ( ( Ax + C )-1 ) / B ) + 5

    plt.scatter(x1, y1, color='red', label='Punto A', marker='o')
    plt.plot(x, y, color='blue', label=f'Recta (y = {a_frac}x {"+" if b_frac >= 0 else "-"} {abs(b_frac)}x {"+" if c_frac >= 0 else "-"} {abs(c_frac)})')

    plt.legend()
    plt.title('Recta')

#Agregar ejes X e Y definidos
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

#Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x1.delete(0, 'end')
    entrada_y1.delete(0, 'end')
    entrada_pendiente.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

#Función para salir de la aplicación
def salir():
    ventana.quit()

#Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación de Recta con Gráfico")

#Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=200)

#Crear variables para los puntos y el resultado

entrada_x1 = tk.Entry(ventana, width=13)
entrada_y1 = tk.Entry(ventana, width=13)
entrada_numerador = tk.Entry(ventana, width=13)
entrada_denominador = tk.Entry(ventana, width=13)

resultado = tk.StringVar()

subtitulo = tk.Label(ventana, text="RECTA ax+by+c=0", font=("Helvetica", 13))
subtitulo.grid(row=0, column=0, columnspan=2, pady=(10, 0))

subtitulo1 = tk.Label(ventana, text="PUNTO A", font=("Helvetica", 13))
subtitulo1.grid(row=1, column=0, columnspan=2)
etiqueta_x1 = tk.Label(ventana, text="X: ")
etiqueta_x1.grid(row=2, column=0)
entrada_x1.grid(row=2, column=1)
etiqueta_y1 = tk.Label(ventana, text="Y: ")
etiqueta_y1.grid(row=3, column=0)
entrada_y1.grid(row=3, column=1)

subtitulo2 = tk.Label(ventana, text="PENDIENTE (m)", font=("Helvetica", 13))
subtitulo2.grid(row=4, column=0, columnspan=2)
etiqueta_numerador = tk.Label(ventana, text="numerador: ")
etiqueta_numerador.grid(row=5, column=0)
entrada_numerador.grid(row=5, column=1)

etiqueta_denominador = tk.Label(ventana, text="Denominador: ")
etiqueta_denominador.grid(row=6, column=0)
entrada_denominador.grid(row=6, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=2, pady=(10, 0))

boton_calcular = ttk.Button(ventana, text="Calcular Ecuación y Gráfico", command=calcular_ecuacion_general_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=2, pady=(10, 0))
boton_limpiar.grid(row=9, column=0, pady=(10, 0))
boton_salir.grid(row=9, column=1, pady=(10, 0))

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=7, padx=(20, 0))

ventana.mainloop()