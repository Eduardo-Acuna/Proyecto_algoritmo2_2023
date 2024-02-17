import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
import numpy as np
from reportlab.pdfgen import canvas as reportlab_canvas

# Función para calcular la ecuación general y mostrar el gráfico
def calcular_ecuacion_general_y_grafico():
    x1 = float(entrada_x1.get())
    y1 = float(entrada_y1.get())
    x2 = float(entrada_x2.get())
    y2 = float(entrada_y2.get())
    x3 = float(entrada_x3.get())
    y3 = float(entrada_y3.get())

    # Verificar que los puntos no sean colineales
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0:
        ecuacion = Circunf2(x1, y1, x2, y2, x3, y3)
        h, k, radio = cia_encontrar_hkr_cadena(ecuacion)
        D, E, F = cia_encontrar_constantes_DEF(ecuacion)

        resultado.set(f"Ecuación General: \n{ecuacion}")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

        # Crear un gráfico de la circunferencia en Matplotlib
        plt.cla()  # Limpia el gráfico anterior

        # Definir ejes y límites
        ax.set_aspect('equal', adjustable='box')  # Aspecto cuadrado
        ax.set_xlim([h - radio - 1, h + radio + 1])  # Ajustar límites de x
        ax.set_ylim([k - radio - 1, k + radio + 1])  # Ajustar límites de y

        theta = np.linspace(0, 2 * np.pi, 100)
        x_circunferencia = h + radio * np.cos(theta)
        y_circunferencia = k + radio * np.sin(theta)
        plt.plot(x_circunferencia, y_circunferencia, color='blue', label='Circunferencia')
        plt.scatter(h, k, color='red', label='Centro')

        # Agregar la línea del radio en verde
        plt.plot([h, h + radio], [k, k], color='green', label='Radio')

        plt.scatter(x1, y1, color='red', label='Punto A')
        plt.scatter(x2, y2, color='green', label='Punto B')
        plt.scatter(x3, y3, color='blue', label='Punto C')

        plt.legend(loc='upper left')  # Colocar la leyenda en la esquina superior izquierda

        plt.title('Circunferencia')
        canvas.draw()
    else:
        resultado.set("Los puntos son colineales, no se puede calcular la circunferencia.")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="red")

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_x1.delete(0, 'end')
    entrada_y1.delete(0, 'end')
    entrada_x2.delete(0, 'end')
    entrada_y2.delete(0, 'end')
    entrada_x3.delete(0, 'end')
    entrada_y3.delete(0, 'end')
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
            c.drawString(100, 750, "Ecuación de la Circunferencia por Tres Puntos dado")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, "Punto A: ({}, {})".format(entrada_x1.get(), entrada_y1.get()))
            c.drawString(100, 680, "Punto B: ({}, {})".format(entrada_x2.get(), entrada_y2.get()))
            c.drawString(100, 660, "Punto C: ({}, {})".format(entrada_x3.get(), entrada_y3.get()))
            c.drawString(100, 640, "Ecuación de la circunferencia:\n {}".format(resultado.get()))

            # Agregar el gráfico al PDF
            fig.savefig("circunferencia_plot.png", bbox_inches='tight', pad_inches=0.1)
            c.drawImage("circunferencia_plot.png", 50, 100, width=400, height=300)

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
ventana.title("Calculadora de Circunferencia con Gráfico")
# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")


# Etiqueta con el título
titulo = tk.Label(ventana, text="Ecuación de la Circunferencia por Tres Puntos", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")



# Crear variables para los puntos y el resultado
entrada_x1 = tk.Entry(ventana, width=13)
entrada_y1 = tk.Entry(ventana, width=13)
entrada_x2 = tk.Entry(ventana, width=13)
entrada_y2 = tk.Entry(ventana, width=13)
entrada_x3 = tk.Entry(ventana, width=13)
entrada_y3 = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo1 = tk.Label(ventana, text="PUNTO A", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=1, column=0, columnspan=3)
etiqueta_A = tk.Label(ventana, text="A(X,Y): ", fg="white", bg="#3b598d")
etiqueta_A.grid(row=2, column=0)
entrada_x1.grid(row=2, column=1)
entrada_y1.grid(row=2, column=2)


subtitulo2 = tk.Label(ventana, text="PUNTO B", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo2.grid(row=3, column=0, columnspan=3)
etiqueta_B = tk.Label(ventana, text="B(X,Y): ", fg="white", bg="#3b598d")
etiqueta_B.grid(row=4, column=0)
entrada_x2.grid(row=4, column=1)
entrada_y2.grid(row=4, column=2)

subtitulo3 = tk.Label(ventana, text="PUNTO C", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo3.grid(row=5, column=0, columnspan=3)
etiqueta_C = tk.Label(ventana, text="C(X,Y): ", fg="white", bg="#3b598d")
etiqueta_C.grid(row=6, column=0)
entrada_x3.grid(row=6, column=1)
entrada_y3.grid(row=6, column=2)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=3, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Ecuación y Gráfico", command=calcular_ecuacion_general_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=8, column=0, columnspan=3)
boton_limpiar.grid(row=9, column=0,)
boton_guardar_pdf.grid(row=9, column=2)
boton_salir.grid(row=10, column=0, columnspan=3)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=3, rowspan=10, padx=10, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()

