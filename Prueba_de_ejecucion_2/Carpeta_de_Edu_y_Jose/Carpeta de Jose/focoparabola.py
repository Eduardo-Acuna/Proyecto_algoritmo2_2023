import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas

# Función que calcula el foco y muestra el gráfico
def calcular_foco_y_grafico():
    a = float(entrada_a.get())
    b = float(entrada_b.get())
    c = float(entrada_c.get())

    # Calcular el foco de la parábola
    p = 1 / (4 * a)
    foco_x = -b / (2 * a)
    foco_y = c - (1 / (4 * a))

    # Mostrar el resultado
    resultado.set(f"Foco de la Parábola:\n ({foco_x}, {foco_y})")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la parábola en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    x = np.linspace(foco_x - 5, foco_x + 5, 400)
    y = a * (x - foco_x) ** 2 + foco_y
    plt.plot(x, y, color='blue', label='Parábola')
    plt.scatter(foco_x, foco_y, color='red', label='Foco')

    plt.legend()
    plt.title('Parábola')
    canvas.draw()

# Función para guardar el resultado y el gráfico en un PDF
def guardar_en_pdf():
    from reportlab.pdfgen import canvas as reportlab_canvas

    # Crear un documento PDF
    c = reportlab_canvas.Canvas("foco_de_parabola.pdf")
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Cálculo del Foco de una Parábola")
    c.drawString(100, 730, "--------------------------------------------------")
    c.drawString(100, 700, "Coeficiente a: " + entrada_a.get())
    c.drawString(100, 680, "Coeficiente b: " + entrada_b.get())
    c.drawString(100, 660, "Coeficiente c: " + entrada_c.get())
    c.drawString(100, 630, resultado.get())
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
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Foco de Parábola con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=200)

# Crear variables para los coeficientes y el resultado
entrada_a = tk.Entry(ventana, width=13)
entrada_b = tk.Entry(ventana, width=13)
entrada_c = tk.Entry(ventana, width=13)
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

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Foco y Gráfico", command=calcular_foco_y_grafico)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=5, column=0, columnspan=2, pady=(10, 0))
boton_guardar_pdf.grid(row=6, column=0, columnspan=2, pady=(10, 0))
boton_limpiar.grid(row=7, column=0, pady=(10, 0))
boton_salir.grid(row=7, column=1, pady=(10, 0))

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=2, rowspan=8, padx=(20, 0))

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
