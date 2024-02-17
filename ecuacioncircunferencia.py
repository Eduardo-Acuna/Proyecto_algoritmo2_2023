import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas  # Agregar esta línea
from fractions import Fraction
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

# Función que calcula la ecuación general y muestra el gráfico
def calcular_ecuacion_general_y_grafico():
    x = float(entrada_x.get())
    y = float(entrada_y.get())
    radio = abs(float(entrada_radio.get()))

    ecuacion = Circunf1(x,y,radio)

    resultado.set(f"Ecuación General: \n{ecuacion}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")  # Ajustar tamaño y color

    # Crear un gráfico de la circunferencia en Matplotlib
    plt.cla()  # Limpia el gráfico anterior

    # Definir ejes y límites
    ax.set_aspect('equal', adjustable='box')  # Aspecto cuadrado
    ax.set_xlim([x - radio - 1, x + radio + 1])
    ax.set_ylim([y - radio - 1, y + radio + 1])

    theta = np.linspace(0, 2 * np.pi, 100)
    x_circunferencia = x + radio * np.cos(theta)
    y_circunferencia = y + radio * np.sin(theta)
    plt.plot(x_circunferencia, y_circunferencia, color='blue', label='Circunferencia')
    plt.scatter(x, y, color='red', label='Centro')

    # Agregar la línea del radio en verde
    plt.plot([x, x + radio * np.cos(np.pi / 4)], [y, y + radio * np.sin(np.pi / 4)], color='green', label='Radio')
    plt.legend(loc='upper left') # Colocar la leyenda en la esquina superior izquierda
    
    plt.title('Circunferencia')

    
    canvas.draw()

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x.delete(0, 'end')
    entrada_y.delete(0, 'end')
    entrada_radio.delete(0, 'end')
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
            c.drawString(100, 750, "Cálculo de Ecuación de Circunferencia")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, f"Centro de la circunferencia: ({entrada_x.get()}, {entrada_y.get()})")
            c.drawString(100, 680, f"Radio: {entrada_radio.get()}")
            c.drawString(100, 660, resultado.get())

            # Agregar el gráfico al PDF
            fig.savefig("circunferencia_plot.png", bbox_inches='tight', pad_inches=0.1)
            c.drawImage("circunferencia_plot.png", 50, 100, width=400, height=300)

            # Guardar y cerrar el PDF
            c.save()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Circunferencia con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Ecuación de la Circunferencia", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para las coordenadas y el resultado
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
entrada_radio = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo1 = tk.Label(ventana, text="CENTRO DE LA CIA.", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=1, column=0, columnspan=2)
etiqueta_x = tk.Label(ventana, text="Eje X: ", fg="white", bg="#3b598d")
etiqueta_x.grid(row=2, column=0)
entrada_x.grid(row=2, column=1)
etiqueta_y = tk.Label(ventana, text="Eje Y: ", fg="white", bg="#3b598d")
etiqueta_y.grid(row=3, column=0)
entrada_y.grid(row=3, column=1)



subtitulo1 = tk.Label(ventana, text="RADIO DE LA CIA.", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=4, column=0, columnspan=2)
etiqueta_radio = tk.Label(ventana, text="Radio:", fg="white", bg="#3b598d")
etiqueta_radio.grid(row=5, column=0)
entrada_radio.grid(row=5, column=1)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=6, column=0, columnspan=2,  sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Ecuación y Gráfico", command=calcular_ecuacion_general_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=7, column=0, columnspan=2)
boton_limpiar.grid(row=8, column=0)
boton_guardar_pdf.grid(row=8, column=1)
boton_salir.grid(row=9, column=0, columnspan=2)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10, padx=10, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()


