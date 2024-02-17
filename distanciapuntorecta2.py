import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import sqrt

# Función que calcula la distancia entre un punto y una recta y muestra el gráfico
def calcular_distancia_y_grafico():
    x = float(entrada_x.get())
    y = float(entrada_y.get())
    recta_str = entrada_recta.get()
    
    # Validar el formato de la recta
    if not validar_recta(recta_str):
        resultado.set("Error:\nFormato de recta incorrecto")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="red")
        return
    
    a, b, c = obtener_coeficientes(recta_str)

    if a == 0 and b == 0:
        resultado.set("Error:\nLos coeficientes 'a' y 'b' \nno pueden ser ambos cero.")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="red")
        return

    if a == 0:
        distancia = abs(c / b)
    elif b == 0:
        distancia = abs(c / a)
    else:
        distancia = abs((a * x + b * y + c) / sqrt(a ** 2 + b ** 2))

    resultado.set(f"La distancia es: {distancia:.2f}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de dispersión en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    plt.scatter(x, y, color='red', label='Punto')
    
    # Generar puntos en la recta para el gráfico
    x_vals = [x - 10, x + 10]
    if a == 0:
        y_vals = [y, y]
    elif b == 0:
        y_vals = [y - 10, y + 10]
    else:
        y_vals = [(c - a * x) / b for x in x_vals]
    plt.plot(x_vals, y_vals, color='blue', label='Recta')
    
    plt.legend()
    plt.title('Distancia entre Punto y Recta')
    canvas.draw()


# Función para validar el formato de la recta
def validar_recta(recta_str):
    # Formato permitido: "ax+by+c=0"
    parts = recta_str.split('=')
    if len(parts) != 2:
        return False
    
    left_part = parts[0]
    right_part = parts[1]
    
    if len(left_part) == 0 or len(right_part) == 0:
        return False
    
    return True

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

# Función que analiza la cadena y obtiene los valores a, b y c
def obtener_coeficientes(recta_str):
    recta_str = recta_str.replace(" ", "")  # Eliminar espacios
    parts = recta_str.split('=')
    
    left_part = parts[0]
    right_part = parts[1]
    
    # Inicializar los coeficientes en caso de que no se encuentren
    a, b, c = 0, 0, 0
    
    # Verificar si la ecuación tiene un signo negativo al principio
    if left_part[0] == '-':
        left_part = '-' + left_part[1:]  # Mantener el signo negativo

    # Separar la parte izquierda (ax+by+c)
    left_parts = left_part.split('+')
    
    if len(left_parts) >= 3:
        a_str = left_parts[0].replace("x", "")
        b_str = left_parts[1].replace("y", "")
        c_str = left_parts[2]
        
        if 'x' not in a_str:
            a_str = '-' + a_str
        if 'y' not in b_str:
            b_str = '-' + b_str
        if 'x' not in c_str:
            c_str = '-' + c_str
        
        a = float(a_str) if a_str else 0
        b = float(b_str) if b_str else 0
        c = float(c_str) if c_str else 0

    if right_part:  # Si la parte derecha no está vacía, es el valor de 'c'
        if 'x' not in right_part:
            right_part = '-' + right_part
        c = float(right_part)

    return a, b, c




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
