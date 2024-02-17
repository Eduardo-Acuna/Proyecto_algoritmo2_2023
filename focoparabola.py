import tkinter as tk
from tkinter import StringVar, ttk,filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
from reportlab.pdfgen import canvas as reportlab_canvas




def calcular_foco_y_grafico():
    ecuacion_parabola = entrada_ecuacion.get()
    parabola = aux_ordenar_ecuación_final_float(ecuacion_parabola)
    h, k, p, fx, fy, bandera = Foco_parabola(parabola)

    # Mostrar el resultado
    resultado.set(f"Foco de la Parábola:\n ({fx}, {fy})")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la parábola en Matplotlib
    plt.cla()  # Limpia el gráfico anterior

    if bandera == 'x2':
        # Para parábolas verticales, intercambiamos x e y en la ecuación
        x_parabola = np.linspace(h - 5, h + 5, 400)
        y_parabola = p * (x_parabola - h)**2 + k
    else:
        # Para parábolas horizontales, intercambiamos x e y
        y_parabola = np.linspace(k - 5, k + 5, 400)
        x_parabola = p * (y_parabola - k)**2 + h

    plt.plot(x_parabola, y_parabola, color='blue', label='Parábola')
    plt.scatter(fx, fy, color='red', label='Foco')

    plt.legend()
    plt.title('Parábola')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # Ajusta la escala del gráfico y centra el foco
    plt.axis([h - 8, h + 8, k - 10, k + 10])

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
    

    # Agregar el gráfico al PDF
    fig.savefig("parabola_plot.png", bbox_inches='tight', pad_inches=0.1)
    c.drawImage("parabola_plot.png", 50, 100, width=400, height=300)
    c.showPage()
    # Guardar y cerrar el PDF
    c.save()


def guardar_en_pdf():
    try:
        # Obtener la ruta de destino mediante un cuadro de diálogo
        ruta_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Verificar si el usuario ha seleccionado una ruta
        if ruta_destino:
            # Crear un documento PDF
            c = reportlab_canvas.Canvas(ruta_destino)  # Utiliza la ruta seleccionada por el usuario
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Cálculo del Foco de una Parábola")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, "Ecuacion de la Parabola: " + entrada_ecuacion.get())
            c.drawString(100, 680, resultado.get())
            
            # Agregar el gráfico al PDF
            fig.savefig("parabola_plot.png", bbox_inches='tight', pad_inches=0.1)
            c.drawImage("parabola_plot.png", 50, 100, width=400, height=300)
            c.showPage()
            # Guardar y cerrar el PDF
            c.save()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")

# Función para limpiar los campos y el gráfico
def limpiar():
    entrada_ecuacion.delete(0, 'end')

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
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Foco de la Parabola", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para los coeficientes y el resultado
entrada_ecuacion = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="Ingrese la Ecuacion\nde la Parabola:", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo.grid(row=1, column=0, columnspan=2)
entrada_ecuacion.grid(row=2, column=0, sticky="ew", columnspan=2, padx=10, pady=10)


etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Foco y Gráfico", command=calcular_foco_y_grafico)
boton_guardar_pdf = ttk.Button(ventana, text="Guardar en PDF", command=guardar_en_pdf)
boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_salir = ttk.Button(ventana, text="Salir", command=salir)

boton_calcular.grid(row=5, column=0, columnspan=2)
boton_limpiar.grid(row=6, column=0)
boton_guardar_pdf.grid(row=6, column=1)
boton_salir.grid(row=7, column=0, columnspan=2)

# Configurar el gráfico de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=10, padx=10, pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
