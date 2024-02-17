import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from fractions import Fraction
import numpy as np
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
from reportlab.pdfgen import canvas as reportlab_canvas


# Función para calcular la ecuación de la recta y mostrar el gráfico
def calcular_ecuacion_general_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())

    numerador = float(entrada_numerador.get())
    denominador = float(entrada_denominador.get())

    ecuacion = Recta2(x1 , y1 , numerador , denominador)
    resultado.set(f"Ecuación de la Recta:\n{ecuacion}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Constantes
    a , b , c = aux_encontrar_constantes_recta_float(ecuacion)


    # Crear un gráfico de la recta en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    x_values = np.linspace(-10 + x1, 10 + x1, 400)
    y_values_original = (-a * x_values - c) / b
    # Dibujar la recta original de color azul
    plt.plot(x_values, y_values_original, color='blue', label=f'Recta Original: {ecuacion}', linestyle='--')

    plt.scatter(x1, y1, color='red', label='Punto A', marker='o')
    #plt.plot(x, y, color='blue', label=f'Recta ({ecuacion})')

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

    # Ajustar automáticamente los límites del gráfico
    plt.axis('equal')  # Asegura que la escala en ambos ejes sea igual
    plt.autoscale()

    canvas.draw()


# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x1.delete(0, 'end')
    entrada_y1.delete(0, 'end')
    entrada_numerador.delete(0, 'end')
    entrada_denominador.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Función para guardar el resultado en un archivo PDF
def guardar_en_pdf():
    try:
        # Obtener la ruta de destino mediante un cuadro de diálogo
        ruta_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Verificar si el usuario ha seleccionado una ruta
        if ruta_destino:
            # Guardar el gráfico como una imagen
            fig.savefig("recta_plot.png", bbox_inches='tight', pad_inches=0.1)

            # Crear un documento PDF usando ReportLab
            c = reportlab_canvas.Canvas(ruta_destino)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Cálculo de Ecuación de la Recta Pendiente")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, f"Coordenadas Punto A: ({entrada_x1.get()}, {entrada_y1.get()})")
            c.drawString(100, 680, f"Pendiente (m): ({entrada_numerador.get()}/{entrada_denominador.get()})")
            c.drawString(100, 660, resultado.get())

            # Agregar el gráfico al PDF
            c.drawImage("recta_plot.png", 50, 100, width=400, height=300)

            c.showPage()
            # Guardar y cerrar el PDF
            c.save()


            canvas.draw()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación de Recta con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Ecuación de la Recta Pendiente", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para los puntos y el resultado
entrada_x1 = tk.Entry(ventana, width=13)
entrada_y1 = tk.Entry(ventana, width=13)
entrada_numerador = tk.Entry(ventana, width=13)
entrada_denominador = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario

subtitulo1 = tk.Label(ventana, text="PUNTO A", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=1, column=0, columnspan=2)
etiqueta_x1 = tk.Label(ventana, text="X: ", fg="white", bg="#3b598d")
etiqueta_x1.grid(row=2, column=0)
entrada_x1.grid(row=2, column=1)
etiqueta_y1 = tk.Label(ventana, text="Y: ", fg="white", bg="#3b598d")
etiqueta_y1.grid(row=3, column=0)
entrada_y1.grid(row=3, column=1)

subtitulo2 = tk.Label(ventana, text="PENDIENTE (m)", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo2.grid(row=4, column=0, columnspan=2)

etiqueta_numerador = tk.Label(ventana, text="Numerador: ", fg="white", bg="#3b598d")
etiqueta_numerador.grid(row=5, column=0)
entrada_numerador.grid(row=5, column=1)

etiqueta_denominador = tk.Label(ventana, text="Denominador: ", fg="white", bg="#3b598d")
etiqueta_denominador.grid(row=6, column=0)
entrada_denominador.grid(row=6, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=2,  sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)


# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Ecuación y Gráfico", command=calcular_ecuacion_general_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=2)
boton_limpiar.grid(row=9, column=0)
boton_guardar_pdf.grid(row=9, column=1)
boton_salir.grid(row=10, column=0, columnspan=2)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10, padx=10, pady=10)

ventana.mainloop()
