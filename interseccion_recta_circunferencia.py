import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
from reportlab.pdfgen import canvas as reportlab_canvas

# Función que calcula la recta tangente y muestra el gráfico
def calcular_interseccion_recta_parabola_y_grafico():

    recta = entrada_recta.get()
    circunferencia = entrada_ciarcuferencia.get()



    parabola = aux_ordenar_ecuación_final_float(ecuacion_parabola)
    tangente = Tangente_parabola(parabola, punto_x, punto_y)

    # Mostrar el resultado
    resultado.set(f"Recta Tangente: {tangente}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la parábola y la recta tangente en Matplotlib
    h, k, p, _, _, bandera = Foco_parabola(parabola)
    a, b, c = aux_encontrar_constantes_recta_float(tangente)

    plt.cla()  # Limpia el gráfico anterior

    if bandera == 'x2':
        # Para parábolas verticales, intercambiamos x e y en la ecuación
        x_parabola = np.linspace(k - 2, k + 2, 400)
        y_parabola = p * (x_parabola - h)**2 + k
    else:
        # Para parábolas horizontales, intercambiamos x e y
        y_parabola = np.linspace(k - 5, k + 5, 400)
        x_parabola = p * (y_parabola - k)**2 + h

    plt.plot(x_parabola, y_parabola, color='blue', label='Parábola')

    # Calcular los puntos para dibujar la recta tangente
    x_tangente = np.linspace(punto_x - 5, punto_x + 5, 400)
    y_tangente = a * (x_tangente - punto_x)**2 + b * (x_tangente - punto_x) + c

    plt.plot(x_parabola, y_parabola, color='blue', label='Parábola')
    plt.plot(x_tangente, y_tangente, color='red', label=f'Recta Tangente: {tangente}', linestyle='--')

    # Dibujar el punto A en el centro del gráfico
    plt.scatter(punto_x, punto_y, color='green', label='Punto A', s=80, marker='o')

    # Ajusta la escala del gráfico y centra al puntoA
    plt.axis([punto_x - 10, punto_x + 10, punto_y - 10, punto_y + 10])
    # Ajustar automáticamente los límites del gráfico
    plt.axis('equal')  # Asegura que la escala en ambos ejes sea igual
    plt.autoscale()

    plt.legend()
    plt.title('Parábola, Recta Tangente, Punto A')
    plt.xlabel('Eje Y')
    plt.ylabel('Eje X')

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
    
    # Agregar el gráfico al PDF
    fig.savefig("parabola_plot.png", bbox_inches='tight', pad_inches=0.1)
    c.drawImage("parabola_plot.png", 50, 100, width=400, height=300)

    c.showPage()
    # Guardar y cerrar el PDF
    c.save()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_recta.delete(0, 'end')
    entrada_parabola.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.withdraw()


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Interseccion Recta y circunferencia con Gráfico")
# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Interseccion entre Recta y Circunferencia", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para los coeficientes y el resultado
entrada_recta = tk.Entry(ventana, width=13)
entrada_circunferencia = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo1 = tk.Label(ventana, text="Ingrese la ecuacion de la Recta:", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=1, column=0, columnspan=2)
entrada_recta.grid(row=2, column=0, sticky="ew", columnspan=2, padx=10, pady=10)

subtitulo2 = tk.Label(ventana, text="Ingrese la ecuacion de la Cia.:", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo2.grid(row=3, column=0, columnspan=2)
entrada_circunferencia.grid(row=4, column=0, sticky="ew", columnspan=2, padx=10, pady=10)



subtitulo3 = tk.Label(ventana, text="Respuesta:", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo3.grid(row=5, column=0, columnspan=2)
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular interseccion y Gráficar", command=calcular_interseccion_recta_parabola_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=2)
boton_limpiar.grid(row=9, column=0)
boton_guardar_pdf.grid(row=9, column=1)
boton_salir.grid(row=10, column=0,columnspan=2)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10, padx=10, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()