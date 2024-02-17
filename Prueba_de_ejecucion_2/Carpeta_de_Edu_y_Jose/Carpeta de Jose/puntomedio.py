import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from clase_geo_Gral import*
from funcion_geo_Gral import* # mas pequeño
from Funcion_Gral import* # copiamos aqui

# Función que calcula el punto medio y muestra el gráfico
def calcular_punto_medio_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())
    x2 = float(entrada_x2.get())
    y2 = float(entrada_y2.get())

    punto1 = Punto(x1 , y1)
    punto2 = Punto(x2 , y2)
    mx , my = punto1.punto_medio(punto2)

    resultado.set(f'Punto medio: {mx} , {my}')
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")  # Ajustar tamaño y color

    # Crear un gráfico de dispersión en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    plt.scatter(x1, y1, color='red', label='Punto A')
    plt.scatter(x2, y2, color='green', label='Punto B')
    plt.scatter(mx, my, color='blue', label='Punto Medio')
    plt.plot([x1, x2], [y1, y2], color='green', label='Recta que pasa por los puntos')  # Agrega la recta
    plt.legend()
    plt.title('Punto Medio')
    canvas.draw()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x1.delete(0, 'end')
    entrada_y1.delete(0, 'end')
    entrada_x2.delete(0, 'end')
    entrada_y2.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Punto Medio con Gráfico")



# Crear variables para las coordenadas y el resultado
entrada_x1 = tk.Entry(ventana, width=13)
entrada_y1 = tk.Entry(ventana, width=13)
entrada_x2 = tk.Entry(ventana, width=13)
entrada_y2 = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo1 = tk.Label(ventana, text="PUNTO A(X1,Y1)", font=("Helvetica", 13))
subtitulo1.grid(row=0, column=0, columnspan=2)
etiqueta_x1 = tk.Label(ventana, text="X1: ")
etiqueta_x1.grid(row=1, column=0)
entrada_x1.grid(row=1, column=1)
etiqueta_y1 = tk.Label(ventana, text="Y1: ")
etiqueta_y1.grid(row=2, column=0)
entrada_y1.grid(row=2, column=1)


subtitulo2 = tk.Label(ventana, text="PUNTO B(X2,Y2)", font=("Helvetica", 13))
subtitulo2.grid(row=3, column=0, columnspan=2)
etiqueta_x2 = tk.Label(ventana, text="X2: ")
etiqueta_x2.grid(row=4, column=0)
entrada_x2.grid(row=4, column=1)
etiqueta_y2 = tk.Label(ventana, text="Y2: ")
etiqueta_y2.grid(row=5, column=0)
entrada_y2.grid(row=5, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=6, column=0, columnspan=2)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Punto Medio y Gráfico", command=calcular_punto_medio_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=7, column=0, columnspan=2)
boton_limpiar.grid(row=8, column=0,)
boton_salir.grid(row=8, column=1)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
