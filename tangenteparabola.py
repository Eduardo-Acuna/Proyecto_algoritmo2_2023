import tkinter as tk
from tkinter import StringVar, ttk,filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*
from reportlab.pdfgen import canvas as reportlab_canvas

# Función que calcula la recta tangente y muestra el gráfico
def calcular_recta_tangente_y_grafico():
    ecuacion_parabola = entrada_ecuacion.get()
    punto_x = float(entrada_x.get())
    punto_y = float(entrada_y.get())

    parabola = aux_ordenar_ecuación_final_float(ecuacion_parabola)
    tangente = Tangente_parabola(parabola, punto_x, punto_y)

    # Mostrar el resultado
    resultado.set(f"Recta Tangente: {tangente}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de la parábola y la recta tangente en Matplotlib
    h, k, p, f1, f2, bandera = Foco_parabola(parabola)
    a, b, c = aux_encontrar_constantes_recta_float(tangente)

    plt.cla()  # Limpia el gráfico anterior
    """
    # Generar valores de y
    y_p = np.linspace(k - 10, k + 10, 200)
    # Calcular los valores correspondientes de x usando la ecuación de la parábola
    x_p = p * (y_p - k)**2 + h"""
    

    if bandera == 'x2':
        # Generar valores de y
        y_p = np.linspace(k - 10, k + 10,50)
        # Calcular los valores correspondientes de x usando la ecuación de la parábola
        x_p = p * (y_p - h)**2 + k

    else:
        # Generar valores de y
        y_p = np.linspace(k - 10, k + 10, 10+50)
        # Calcular los valores correspondientes de x usando la ecuación de la parábola
        x_p = p * (y_p - k)**2 + h



    # Graficar la parábola
    plt.plot(x_p, y_p, label=f'Parábola: {parabola}',color="red")




    # Calcular los puntos para dibujar la recta tangente
    x_r = np.linspace(-100 + punto_x, 100 + punto_x, 900)
    y_r = (-a * x_r - c) / b
    plt.plot(x_r, y_r, color='blue', label=f'Recta tangente: {tangente}',linestyle='--')


    # Dibujar el punto A en el centro del gráfico
    plt.scatter(punto_x, punto_y, color='green', label='Punto A', s=80, marker='o')
    # Ajusta la escala del gráfico y centra al puntoA
    plt.axis([punto_x - 10, punto_x + 10, punto_y - 10, punto_y + 10])

    # Configuraciones adicionales del gráfico
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(color = 'gray', linestyle = '--', linewidth =0.1 )

    plt.legend()
    plt.title('Parábola, Recta Tangente, Punto A')
    plt.xlabel('Eje Y')
    plt.ylabel('Eje X')

    # Ajustar automáticamente los límites del gráfico
    plt.axis('equal')  # Asegura que la escala en ambos ejes sea igual
    

    canvas.draw()




# Función para guardar el resultado y el gráfico en un PDF
def guardar_en_pdf():
    try:
        # Obtener la ruta de destino mediante un cuadro de diálogo
        ruta_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Verificar si el usuario ha seleccionado una ruta
        if ruta_destino:
            # Crear un documento PDF
            c = reportlab_canvas.Canvas(ruta_destino)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Cálculo de la Recta Tangente a una Parábola")
            c.drawString(100, 730, "--------------------------------------------------")
            c.drawString(100, 700, f"Ecuacion de la parabola: {entrada_ecuacion.get()}")
            c.drawString(100, 680, f"Punto A: ({entrada_x.get()}, {entrada_y.get()})")
            c.drawString(100, 660, resultado.get())

            # Agregar el gráfico al PDF
            fig.savefig("parabola_plot.png", bbox_inches='tight', pad_inches=0.1)
            c.drawImage("parabola_plot.png", 50, 100, width=400, height=300)

            c.showPage()
            # Guardar y cerrar el PDF
            c.save()

            canvas.draw()
        else:
            # Usuario canceló la selección de la ruta, puedes agregar un mensaje o realizar alguna acción adicional si lo deseas
            print("La operación de guardar fue cancelada por el usuario.")
    except Exception as e:
        print(f"Error al guardar el PDF: {e}")




    

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


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Recta Tangente a una Parábola con Gráfico")
# Configurar un tamaño mínimo para la parte izquierda de la ventana
ventana.grid_columnconfigure(0, minsize=125)

# Configurar color de fondo de la ventana
ventana.configure(bg="#3b598d")

# Etiqueta con el título
titulo = tk.Label(ventana, text="Ecuacion Recta Tangente a la Parabola", font=("Serif", 30), fg="white", bg="#3b598d")
titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")


# Crear variables para los coeficientes y el resultado
entrada_ecuacion = tk.Entry(ventana, width=13)
entrada_x = tk.Entry(ventana, width=13)
entrada_y = tk.Entry(ventana, width=13)
resultado = tk.StringVar()

# Etiquetas y entradas de usuario
subtitulo = tk.Label(ventana, text="Ingrese la Ecuacion\nde la Parabola:", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo.grid(row=1, column=0, columnspan=2)
entrada_ecuacion.grid(row=2, column=0, sticky="ew", columnspan=2, padx=10, pady=10)


subtitulo1 = tk.Label(ventana, text="Punto A", font=("Helvetica", 13), fg="white", bg="#3b598d")
subtitulo1.grid(row=3, column=0, columnspan=2)
etiqueta_x = tk.Label(ventana, text="Eje X: ", fg="white", bg="#3b598d")
etiqueta_x.grid(row=4, column=0)
entrada_x.grid(row=4, column=1)
etiqueta_y = tk.Label(ventana, text="Eje Y: ", fg="white", bg="#3b598d")
etiqueta_y.grid(row=5, column=0)
entrada_y.grid(row=5, column=1)



etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), fg="blue")
etiqueta_resultado.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10, ipadx=5, ipady=5)

# Botones
boton_calcular = ttk.Button(ventana, text="Calcular Recta Tangente y Gráfico", command=calcular_recta_tangente_y_grafico)
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