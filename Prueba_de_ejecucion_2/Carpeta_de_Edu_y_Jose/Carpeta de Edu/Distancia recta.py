import tkinter as tk
from tkinter import StringVar, ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import sqrt
from reportlab.pdfgen import canvas as reportlab_canvas
from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*


# Función que calcula la distancia entre un punto y una recta y muestra el gráfico
def calcular_distancia_y_grafico():
    x = float(entrada_x.get())
    y = float(entrada_y.get())
    recta_str = entrada_recta.get()
    recta = aux_ordenar_ecuación_final_float(recta_str)
    print(f'Punto: {x} , {y}')
    print(f'Recta: {recta}\n')

    a , b , c = aux_encontrar_constantes_recta_float(recta)
    print(f'Constante C: {c}')

    distancia = Distancia_recta(x , y , recta)
    print(f'Distancia: {distancia}')

    resultado.set(f"La distancia es: {distancia}")
    etiqueta_resultado.config(font=("Helvetica", 12), fg="blue")

    # Crear un gráfico de dispersión en Matplotlib
    plt.cla()  # Limpia el gráfico anterior
    plt.scatter(x, y, color='red', label='Punto')
    
    # Generar puntos en la recta para el gráfico
    x_vals = [x - 10 , x + 10]
    if a == 0:
        y_vals = [y, y]
    elif b == 0:
        y_vals = [y - 10, y + 10]
    else:
        y_vals = [( (a * x + c) / b )*-1 - 5 , ( (a * x + c) / b )*-1 + 5]
    plt.plot(x_vals, y_vals, color='blue', label='Recta')
    
    plt.legend()
    plt.title('Distancia entre Punto y Recta')
    canvas.draw()


# Función para validar el formato de la recta
def validar_recta(recta_str):
    # Formato permitido: "ax+by+c=0"
    parts = recta_str.split('=')
    if len(parts) != 2:
        return False
    
    left_part = parts[0]
    right_part = parts[1]
    
    if len(left_part) == 0 or len(right_part) == 0:
        return False
    
    return True

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
            c.drawString(100, 700, f"Coordenadas Punto P: ({entrada_x.get()}, {entrada_y.get()})")
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
def obtener_coeficientes(recta_str):
    recta_str = recta_str.replace(" ", "")  # Eliminar espacios
    parts = recta_str.split('=')
    
    left_part = parts[0]
    right_part = parts[1]
    
    # Inicializar los coeficientes en caso de que no se encuentren
    a, b, c = 0, 0, 0
    
    # Verificar si la ecuación tiene un signo negativo al principio
    if left_part[0] == '-':
        left_part = '-' + left_part[1:]  # Mantener el signo negativo

    # Separar la parte izquierda (ax+by+c)
    left_parts = left_part.split('+')
    
    if len(left_parts) >= 3:
        a_str = left_parts[0].replace("x", "")
        b_str = left_parts[1].replace("y", "")
        c_str = left_parts[2]
        
        if 'x' not in a_str:
            a_str = '-' + a_str
        if 'y' not in b_str:
            b_str = '-' + b_str
        if 'x' not in c_str:
            c_str = '-' + c_str
        
        a = float(a_str) if a_str else 0
        b = float(b_str) if b_str else 0
        c = float(c_str) if c_str else 0

    if right_part:  # Si la parte derecha no está vacía, es el valor de 'c'
        if 'x' not in right_part:
            right_part = '-' + right_part
        c = float(right_part)

    return a, b, c

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


etiqueta_rectas = tk.Label(ventana, text="RECTA", font=("Helvetica", 13), fg="white", bg="#3b598d")
etiqueta_rectas.grid(row=4, column=0, columnspan=2)
etiqueta_r = tk.Label(ventana, text="ax+by+c=0: ", fg="white", bg="#3b598d")
etiqueta_r.grid(row=5, column=0)
entrada_recta.grid(row=5, column=1)

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
canvas_widget.grid(row=1, column=2, rowspan=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
