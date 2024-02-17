import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from fractions import Fraction
from reportlab.pdfgen import canvas as reportlab_canvas
import numpy as np

# Función para calcular la ecuación de la recta perpendicular y mostrar el gráfico
def calcular_recta_perpendicular_y_grafico():
    ecuacion = entrada_ecuacion.get()

    # Extraer los coeficientes a, b, y c de la ecuación ingresada
    ecuacion = ecuacion.replace("=", "")
    coeficientes = ecuacion.split("x")
    a_str = coeficientes[0].strip()
    b_str = coeficientes[1].split("y")[0].strip()
    c_str = ecuacion.split("y")[1].strip()

    # Convertir los coeficientes a números
    a = float(a_str)
    b = float(b_str)
    c = float(c_str)

    # Calcular la pendiente de la recta original
    if b != 0:
        m = -a / b
    else:
        m = None

    if m is not None:
        # Calcular la pendiente de la recta perpendicular
        m_perpendicular = -1 / m

        # Calcular la ecuación de la recta perpendicular
        a_perpendicular = m_perpendicular
        b_perpendicular = -1
        c_perpendicular = 0

        # Convertir los coeficientes a fracciones si son números decimales
        a_frac = Fraction(a_perpendicular).limit_denominator()
        b_frac = Fraction(b_perpendicular).limit_denominator()

        # Mostrar la ecuación de la recta perpendicular
        ecuacion_perpendicular = f"{a_frac}x {'+' if b_frac >= 0 else '-'} {abs(b_frac)}y = {c_perpendicular}"
        resultado.set(f"Ecuación Perpendicular:\n{ecuacion_perpendicular}")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

        # Crear un gráfico de las dos rectas
        plt.cla()  # Limpia el gráfico anterior

        # Crear un rango de valores para X
        x_values = np.linspace(-10, 10, 400)

        # Calcular los valores correspondientes de Y para la recta original y la recta perpendicular
        y_values_original = (-a * x_values - c) / b
        y_values_perpendicular = (-a_perpendicular * x_values - c_perpendicular) / b_perpendicular

        # Dibujar la primera recta de color azul
        plt.plot(x_values, y_values_original, color='blue', label=f'Recta Original: {ecuacion}')
        
        # Dibujar la recta perpendicular de color rojo
        plt.plot(x_values, y_values_perpendicular, color='red', label=f'Recta Perpendicular: {ecuacion_perpendicular}')

        plt.legend()
        plt.title('Recta y Recta Perpendicular')
        
        # Definir ejes X e Y y ajustar los límites
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
        
        # Ajustar los límites del gráfico
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])

        canvas.draw()

    else:
        resultado.set("La recta ingresada es vertical, \nla perpendicular es horizontal.")
        etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_ecuacion.delete(0, 'end')
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
            c.drawString(100, 700, "Ecuación de la Recta: {}".format(entrada_ecuacion.get()))
            c.drawString(100, 680, resultado.get())

            # Agregar el gráfico al PDF
            fig.savefig("recta_perpendicular_plot.png", bbox_inches='tight', pad_inches=0.1)
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
entrada_ecuacion = tk.Entry(ventana, width=20)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="Ecuación de la Recta \n(ax + by + c = 0)", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo.grid(row=1, column=0, columnspan=2)
entrada_ecuacion.grid(row=2, column=0, sticky="ew", columnspan=2, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=0, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Recta Perpendicular y Gráfico", command=calcular_recta_perpendicular_y_grafico)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=5, column=0, columnspan=2)
boton_limpiar.grid(row=6, column=0)
boton_guardar_pdf.grid(row=6, column=1)
boton_salir.grid(row=7, column=0, columnspan=2 )

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
