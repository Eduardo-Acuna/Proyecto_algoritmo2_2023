import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from fractions import Fraction
from clase_geo_Gral import *
from funcion_geo_Gral import *
from Funcion_Gral import *
from reportlab.pdfgen import canvas as reportlab_canvas
import numpy as np

# Función para calcular la ecuación de la recta perpendicular y mostrar el gráfico
def calcular_recta_perpendicular_y_grafico():
    ecuacion = entrada_ecuacion.get()
    punto_x = float(entrada_x.get())
    punto_y = float(entrada_y.get())

    recta = aux_ordenar_ecuación_final_float(ecuacion)
    recta_perpendicular = Perpendicular(recta, punto_x, punto_y)

    resultado.set(f"Ecuación de la Recta Perpendicular:\n{recta_perpendicular}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    a, b, c = aux_encontrar_constantes_recta_float(recta)
    a1, b1, c1 = aux_encontrar_constantes_recta_float(recta_perpendicular)

    plt.cla()  # Limpia el gráfico anterior

    # Crear un rango de valores para X
    x_values = np.linspace(-10 + punto_x, 10 + punto_x, 400)

    # Calcular los valores correspondientes de Y para la recta original y la recta perpendicular
    y_values_original = (-a * x_values - c) / b
    y_values_perpendicular = (-a1 * x_values - c1) / b1

    # Dibujar la recta original de color azul
    plt.plot(x_values, y_values_original, color='blue', label=f'Recta Original: {recta}', linestyle='--')

    # Dibujar la recta perpendicular de color rojo
    plt.plot(x_values, y_values_perpendicular, color='red', label=f'Recta Perpendicular: {recta_perpendicular}')

    # Calcular el punto A en la recta perpendicular
    punto_a_perpendicular_x = punto_x  # Mantener la misma coordenada X que el punto original
    punto_a_perpendicular_y = (-a1 * punto_a_perpendicular_x - c1) / b1  # Calcular la coordenada Y en la recta perpendicular

    # Dibujar el punto A en el centro del gráfico
    plt.scatter(punto_a_perpendicular_x, punto_a_perpendicular_y, color='green', label='Punto A', s=80, marker='o')

    # Mostrar la leyenda
    plt.legend()
    plt.title('Recta Original, Recta Perpendicular y Punto A')

    # Ajustar automáticamente los límites del gráfico
    plt.axis('equal')  # Asegura que la escala en ambos ejes sea igual
    plt.autoscale()

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

# Función para guardar el resultado en un archivo PDF
def guardar_en_pdf():
    try:
        # Obtener la ruta de destino mediante un cuadro de diálogo
        ruta_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Verificar si el usuario ha seleccionado una ruta
        if ruta_destino:
            # Crear un documento PDF
            c = reportlab_canvas.Canvas(ruta_destino)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Cálculo de Recta Perpendicular")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 720, "Ecuación de la Recta: {}".format(entrada_ecuacion.get()))
            c.drawString(100, 700, f"Punto A: ({entrada_x.get()}, {entrada_y.get()})")
            c.drawString(100, 680, resultado.get())

            # Guardar el gráfico como una imagen
            fig.savefig("recta_perpendicular_plot.png", bbox_inches='tight', pad_inches=0.1)
            plt.close(fig)

            # Agregar el gráfico al PDF
            c.drawImage("recta_perpendicular_plot.png", 50, 100, width=400, height=300)

            c.showPage()
            # Guardar y cerrar el PDF
            c.save()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Recta Perpendicular con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")


# Etiqueta con el título
titulo = tk.Label(ventana, text="Ecuación de la Recta Perpendicular", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

# Crear variables para la ecuación y el resultado
entrada_ecuacion = tk.Entry(ventana, width=13)
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="Ecuación de la Recta \n(ax + by + c = 0)", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo.grid(row=1, column=0, columnspan=2)
entrada_ecuacion.grid(row=2, column=0, sticky="ew", columnspan=2, padx=10, pady=10)

subtitulo1 = tk.Label(ventana, text="Punto A", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=4, column=0, columnspan=2)
etiqueta_x = tk.Label(ventana, text="Eje X: ", fg="white", bg="#3b598d")
etiqueta_x.grid(row=5, column=0)
entrada_x.grid(row=5, column=1)
etiqueta_y = tk.Label(ventana, text="Eje Y: ", fg="white", bg="#3b598d")
etiqueta_y.grid(row=6, column=0)
entrada_y.grid(row=6, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Recta Perpendicular y Gráfico", command=calcular_recta_perpendicular_y_grafico)
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
