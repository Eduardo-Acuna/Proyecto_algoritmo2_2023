import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import sqrt
from clase_geo_Gral import*
from Funcion_Gral import*




# Función que calcula la distancia entre un punto y una recta y muestra el gráfico
def calcular_distancia_y_grafico():
    x = float(entrada_x.get())
    y = float(entrada_y.get())
    recta_str = entrada_recta.get()
    recta = aux_ordenar_ecuación_final_float(recta_str)
    print(f'Punto: {x} , {y}')
    print(f'Recta: {recta}\n')

    a , b , c = aux_encontrar_constantes_recta_float(recta)

    distancia = Distancia_recta(x , y , recta)
    print(f'Distancia: {distancia}')

    resultado.set(f"La distancia es: {distancia}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de dispersión en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    plt.scatter(x, y, color='red', label='Punto')
    
    # Generar puntos en la recta para el gráfico
    x_vals = [x - 10 , x + 10]
    if a == 0:
        y_vals = [y, y]
    elif b == 0:
        y_vals = [y - 10, y + 10]
    else:
        y_vals = [( (a * x + c) / b )*-1 - 5 , ( (a * x + c) / b )*-1 + 5]
    plt.plot(x_vals, y_vals, color='blue', label='Recta')
    
    plt.legend()
    plt.title('Distancia entre Punto y Recta')
    canvas.draw()


# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x.delete(0, 'end')
    entrada_y.delete(0, 'end')
    entrada_recta.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Distancia entre Punto y Recta con Gráfico")

# Crear variables para las coordenadas, coeficientes y el resultado
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
entrada_recta = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
etiqueta_punto = tk.Label(ventana, text="PUNTO P(X, Y)", font=("Helvetica", 13))
etiqueta_punto.grid(row=0, column=0, columnspan=2)
etiqueta_x = tk.Label(ventana, text="X: ")
etiqueta_x.grid(row=1, column=0)
entrada_x.grid(row=1, column=1)
etiqueta_y = tk.Label(ventana, text="Y: ")
etiqueta_y.grid(row=2, column=0)
entrada_y.grid(row=2, column=1)


etiqueta_rectas = tk.Label(ventana, text="RECTA", font=("Helvetica", 13))
etiqueta_rectas.grid(row=3, column=0, columnspan=2)
etiqueta_r = tk.Label(ventana, text="ax+by+c=0: ")
etiqueta_r.grid(row=4, column=0)
entrada_recta.grid(row=4, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=5, column=0, columnspan=2)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Distancia y Gráfico", command=calcular_distancia_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=7, column=0, columnspan=2)
boton_limpiar.grid(row=8, column=0)
boton_salir.grid(row=8, column=1)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
