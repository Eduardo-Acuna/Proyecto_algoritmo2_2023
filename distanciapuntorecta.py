import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import sqrt
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas

# Función que calcula la distancia entre un punto y una recta y muestra el gráfico
def calcular_distancia_y_grafico():
    x1 = float(entrada_x.get())
    y1 = float(entrada_y.get())
    ecuacion_recta = entrada_recta.get()

    recta = aux_ordenar_ecuación_final_float(ecuacion_recta)

    distancia = Distancia_recta(x1 , y1 , recta)

    resultado.set(f"La distancia es: {distancia}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de dispersión en Matplotlib

    # Constantes
    a , b , c = aux_encontrar_constantes_recta_float(recta)

    plt.cla()  # Limpia el gráfico anterior
    x_values = np.linspace(-10 + x1, 10 + x1, 400)
    y_values_original = (-a * x_values - c) / b
    # Dibujar la recta original de color azul
    plt.plot(x_values, y_values_original, color='blue', label=f'Recta Original: {resultado}', linestyle='--')

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
    entrada_x.delete(0, 'end')
    entrada_y.delete(0, 'end')
    entrada_recta.delete(0, 'end')
    resultado.set("")
    plt.cla()
    canvas.draw()

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Función para guardar el resultado en un archivo PDF
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
            c.drawString(100, 750, "Cálculo de Distancia")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, f"Coordenadas Punto A: ({entrada_x.get()}, {entrada_y.get()})")
            c.drawString(100, 680, f"Recta: {entrada_recta.get()}")
            c.drawString(100, 660, resultado.get())

            # Agregar el gráfico al PDF
            fig.savefig("distancia_plot.png", bbox_inches='tight', pad_inches=0.1)
            c.drawImage("distancia_plot.png", 50, 100, width=400, height=300)

            c.showPage()
            # Guardar y cerrar el PDF
            c.save()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")
# Función que analiza la cadena y obtiene los valores a, b y c


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Distancia entre Punto y Recta con Gráfico")

# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Distancia entre un Punto y una Recta", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

# Crear variables para las coordenadas, coeficientes y el resultado
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
entrada_recta = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
etiqueta_punto = tk.Label(ventana, text="PUNTO P", font=("Helvetica", 13), fg="white", bg="#3b598d")
etiqueta_punto.grid(row=1, column=0, columnspan=2)
etiqueta_x = tk.Label(ventana, text="X: ", fg="white", bg="#3b598d")
etiqueta_x.grid(row=2, column=0)
entrada_x.grid(row=2, column=1)
etiqueta_y = tk.Label(ventana, text="Y: ", fg="white", bg="#3b598d")
etiqueta_y.grid(row=3, column=0)
entrada_y.grid(row=3, column=1)


etiqueta_rectas = tk.Label(ventana, text="Ingrese la Ecuacion\nde la Recta:", font=("Helvetica", 13), fg="white", bg="#3b598d")
etiqueta_rectas.grid(row=4, column=0, columnspan=2)

entrada_recta.grid(row=5, column=0,sticky="ew", columnspan=2, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Distancia y Gráfico", command=calcular_distancia_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=2)
boton_limpiar.grid(row=9, column=0)
boton_guardar_pdf.grid(row=9, column=1)
boton_salir.grid(row=10, column=0, columnspan=2)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10,padx=10, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
