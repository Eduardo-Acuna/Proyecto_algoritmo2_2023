import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas

# Función que calcula la recta tangente y muestra el gráfico
def calcular_recta_tangente_y_grafico():
    a = float(entrada_a.get())
    b = float(entrada_b.get())
    c = float(entrada_c.get())
    punto_x = float(entrada_x.get())
    punto_y = float(entrada_y.get())

    # Calcular la pendiente de la tangente
    derivada = 2 * a * punto_x + b
    m = derivada

    # Calcular la ecuación de la recta tangente
    c_tangente = punto_y - m * punto_x

    # Mostrar el resultado
    resultado.set(f"Recta Tangente: y = {m}x + {c_tangente}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la parábola y la recta tangente en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    x = np.linspace(punto_x - 5, punto_x + 5, 400)
    y_parabola = a * x ** 2 + b * x + c
    y_tangente = m * x + c_tangente

    plt.plot(x, y_parabola, color='blue', label='Parábola')
    plt.plot(x, y_tangente, color='red', label='Recta Tangente')

    plt.scatter(punto_x, punto_y, color='green', label='Punto A', s=80, marker='o')

    plt.legend()
    plt.title('Parábola y Recta Tangente')
    canvas.draw()

# Función para guardar el resultado y el gráfico en un PDF
def guardar_en_pdf():
    from reportlab.pdfgen import canvas as reportlab_canvas

    # Crear un documento PDF
    c = reportlab_canvas.Canvas("recta_tangente.pdf")
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Cálculo de la Recta Tangente a una Parábola")
    c.drawString(100, 730, "--------------------------------------------------")
    c.drawString(100, 700, "Coeficiente a: " + entrada_a.get())
    c.drawString(100, 680, "Coeficiente b: " + entrada_b.get())
    c.drawString(100, 660, "Coeficiente c: " + entrada_c.get())
    c.drawString(100, 640, "Punto A: (" + entrada_x.get() + ", " + entrada_y.get() + ")")
    c.drawString(100, 610, resultado.get())
    c.showPage()

    # Agregar el gráfico al PDF
    fig.savefig("parabola_plot.png", bbox_inches='tight', pad_inches=0.1)
    c.drawImage("parabola_plot.png", 50, 100, width=400, height=300)

    # Guardar y cerrar el PDF
    c.save()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_a.delete(0, 'end')
    entrada_b.delete(0, 'end')
    entrada_c.delete(0, 'end')
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
ventana.title("Calculadora de Recta Tangente a una Parábola con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=200)

# Crear variables para los coeficientes, el punto y el resultado
entrada_a = tk.Entry(ventana, width=13)
entrada_b = tk.Entry(ventana, width=13)
entrada_c = tk.Entry(ventana, width=13)
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="PARÁBOLA \nax^2 + bx + c = 0", font=("Helvetica", 13))
subtitulo.grid(row=0, column=0, columnspan=2, pady=(10, 0))
etiqueta_a = tk.Label(ventana, text="Coeficiente a: ")
etiqueta_a.grid(row=1, column=0)
entrada_a.grid(row=1, column=1)
etiqueta_b = tk.Label(ventana, text="Coeficiente b: ")
etiqueta_b.grid(row=2, column=0)
entrada_b.grid(row=2, column=1)
etiqueta_c = tk.Label(ventana, text="Coeficiente c: ")
etiqueta_c.grid(row=3, column=0)
entrada_c.grid(row=3, column=1)
etiqueta_punto = tk.Label(ventana, text="Punto A (Coordenadas): ")
etiqueta_punto.grid(row=4, column=0)
entrada_x.grid(row=4, column=1)
entrada_y.grid(row=4, column=2)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Recta Tangente y Gráfico", command=calcular_recta_tangente_y_grafico)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=6, column=0, columnspan=2, pady=(10, 0))
boton_guardar_pdf.grid(row=7, column=0, columnspan=2, pady=(10, 0))
boton_limpiar.grid(row=8, column=0, pady=(10, 0))
boton_salir.grid(row=8, column=1, pady=(10, 0))

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=3, rowspan=9, padx=(20, 0))

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
