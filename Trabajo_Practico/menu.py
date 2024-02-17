import tkinter as tk

# -------------------------------------------------------------------------------
# PUNTO MEDIO DE UN SEGMENTO
def punto_medio_de_un_segmento():
    punto_medio = tk.Toplevel(menuPrincipal)
    punto_medio.title("PUNTO MEDIO DE UN SEGMENTO")
    punto_medio.geometry("1000x600")
    etiqueta = tk.Label(punto_medio, text="Esta es una nueva ventana")
    root.configure(bg='blue')

# DISTANCIA ENTRE DOS PUNTOS
def distancia_entre_dos_puntos():
    distancia_dos_puntos = tk.Toplevel(menuPrincipal)
    distancia_dos_puntos.title("DISTANCIA ENTRE DOS PUNTOS")
    distancia_dos_puntos.geometry("1000x600")
    etiqueta = tk.Label(distancia_dos_puntos, text="Esta es una nueva ventana")
    root.configure(bg='blue')

# DISTANCIA DE UNA PUNTO A UNA RECTA
def distancia_entre_un_punto_a_una_recta():
    distancia_punto_recta = tk.Toplevel(menuPrincipal)
    distancia_punto_recta.title("DISTANCIA DE UNA PUNTO A UNA RECTA")
    distancia_punto_recta.geometry("1000x600")
    etiqueta = tk.Label(distancia_punto_recta, text="Esta es una nueva ventana")
    root.configure(bg='blue')

# ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE
def ecuacion_recta_por_un_punto_y_pendiente():
    ecuacion_recta_pendiente = tk.Toplevel(menuPrincipal)
    ecuacion_recta_pendiente.title("ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE")
    ecuacion_recta_pendiente.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_recta_pendiente, text="Esta es una nueva ventana")
    root.configure(bg='blue')

# ECUACIÓN DE RECTA POR DOS PUNTOS
def ecuacion_recta_dos_puntos():
    ecuacion_recta_puntos = tk.Toplevel(menuPrincipal)
    ecuacion_recta_puntos.title("ECUACIÓN DE RECTA POR DOS PUNTOS")
    ecuacion_recta_puntos.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_recta_puntos, text="Esta es una nueva ventana")
    ecuacion_recta_puntos.configure(bg='green')

# ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO
def ecuacion_recta_paralela_recta_punto():
    ecuacion_recta_paralelas = tk.Toplevel(menuPrincipal)
    ecuacion_recta_paralelas.title("ECUACIÓN DE RECTA POR DOS PUNTOS")
    ecuacion_recta_paralelas.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_recta_paralelas, text="Esta es una nueva ventana")
    ecuacion_recta_paralelas.configure(bg='black')

# ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO
def ecuacion_recta_perpendicular_recta_punto():
    ecuacion_recta_perpendicular = tk.Toplevel(menuPrincipal)
    ecuacion_recta_perpendicular.title("ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO")
    ecuacion_recta_perpendicular.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_recta_perpendicular, text="Esta es una nueva ventana")
    ecuacion_recta_perpendicular.configure(bg='red')


# ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO
def ecuacion_circunferencia_centro_radio():
    ecuacion_circunferencia_radio = tk.Toplevel(menuPrincipal)
    ecuacion_circunferencia_radio.title("ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO")
    ecuacion_circunferencia_radio.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_circunferencia_radio, text="Esta es una nueva ventana")
    ecuacion_circunferencia_radio.configure(bg='yellow')


# ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS
def ecuacion_circunferencia_tres_puntos():
    ecuacion_circunferencia_puntos = tk.Toplevel(menuPrincipal)
    ecuacion_circunferencia_puntos.title("ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS")
    ecuacion_circunferencia_puntos.geometry("1000x600")
    etiqueta = tk.Label(ecuacion_circunferencia_puntos, text="Esta es una nueva ventana")
    ecuacion_circunferencia_puntos.configure(bg='green')


# HALLAR FOCO DE UNA PARÁBOLA
def foco_de_parabola():
    foco_parabola = tk.Toplevel(menuPrincipal)
    foco_parabola.title("ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO")
    foco_parabola.geometry("1000x600")
    etiqueta = tk.Label(foco_parabola, text="Esta es una nueva ventana")
    foco_parabola.configure(bg='green')



# TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO
def tangente_parabola():
    tangente_parabola_punto = tk.Toplevel(menuPrincipal)
    tangente_parabola_punto.title("TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO")
    tangente_parabola_punto.geometry("1000x600")
    etiqueta = tk.Label(tangente_parabola_punto, text="Esta es una nueva ventana")
    tangente_parabola_punto.configure(bg='green')




# INTERSECCIÓN
def interseccion():
    interseccion = tk.Toplevel(menuPrincipal)
    interseccion.title("INTERSECCIÓN")
    interseccion.geometry("1000x600")
    etiqueta = tk.Label(interseccion, text="Esta es una nueva ventana")
    interseccion.configure(bg='orange')


# Salir del Asistente
def salir():
    menuPrincipal.destroy()

# -------------------------------------------------------------------------------

# MENU PRINCIPAL
menuPrincipal = tk.Tk()
menuPrincipal.title("MENÚ PRINCIPAL")
menuPrincipal.configure(bg='blue')

# Crear una etiqueta con un título grande
titulo = tk.Label(menuPrincipal, text="MENÚ DE ELECCIÓN DE OPERACIÓN", font=("Helvetica", 20))
titulo.pack()

# Obtener el tamaño de la pantalla
ancho= menuPrincipal.winfo_screenwidth()
alto= menuPrincipal.winfo_screenheight()
# Configurar el tamaño de la ventana para que se ajuste a la pantalla
menuPrincipal.geometry(f"{ancho}x{alto}")




# -------------------------------------------------------------------------------
# BOTON DE PUNTO MEDIO
boton = tk.Button(menuPrincipal, text="Punto Medio de un Segmento", command=punto_medio_de_un_segmento, width=200, height=2)
boton.pack()

# BOTON DE DISTANCIA ENTRE DOS PUNTOS
boton = tk.Button(menuPrincipal, text="Distancia entre dos puntos", command=distancia_entre_dos_puntos, width=200, height=2)
boton.pack()

# BOTON DE DISTANCIA DE UNA PUNTO A UNA RECTA
boton = tk.Button(menuPrincipal, text="Distancia entre un punto a una recta", command=distancia_entre_un_punto_a_una_recta, width=200, height=2)
boton.pack()

# BOTON DE ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE
boton = tk.Button(menuPrincipal, text="Ecuación de recta por un punto y la pendiente", command=ecuacion_recta_por_un_punto_y_pendiente, width=200, height=2)
boton.pack()

# BOTON DE ECUACIÓN DE RECTA POR DOS PUNTOS
boton = tk.Button(menuPrincipal, text="Ecuación de recta por dos puntos", command=ecuacion_recta_dos_puntos, width=200, height=2)
boton.pack()

# BOTON DE ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO
boton = tk.Button(menuPrincipal, text="Ecuación de recta paralela a una recta por un punto", command=ecuacion_recta_paralela_recta_punto, width=200, height=2)
boton.pack()

# BOTON DE ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO
boton = tk.Button(menuPrincipal, text="Ecuación de recta perpendicular a una recta por un punto", command=ecuacion_recta_perpendicular_recta_punto, width=200, height=2)
boton.pack()


# BOTON DE ECUACIÓN DE CIRCUNFERENCIA CON CENTRO Y RADIO DADO
boton = tk.Button(menuPrincipal, text="Ecuación de circunferencia con centro y radio", command=ecuacion_circunferencia_centro_radio, width=200, height=2)
boton.pack()


# BOTON DE ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS
boton = tk.Button(menuPrincipal, text="Ecuación de circunferencia por tres puntos", command=ecuacion_circunferencia_tres_puntos, width=200, height=2)
boton.pack()

#
# BOTON DE HALLAR FOCO DE UNA PARÁBOLA
boton = tk.Button(menuPrincipal, text="Hallar foco de una parabola", command=foco_de_parabola, width=200, height=2)
boton.pack()

# TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO
boton = tk.Button(menuPrincipal, text="Tangente a una parabola por un punto extremo", command=tangente_parabola, width=200, height=2)
boton.pack()

# INTERSECCIÓN
boton = tk.Button(menuPrincipal, text="interseccion", command=interseccion, width=200, height=2)
boton.pack()

# Salir del Asistente
boton = tk.Button(menuPrincipal, text="SALIR", command=salir, width=50, height=2)
boton.pack()



# -------------------------------------------------------------------------------

menuPrincipal.mainloop()