from funcion_geo import*
from clase_geo import*
import random

# Valores ingresados por el usuario
a , b = random.randint(-50,50) , random.randint(-50,50)
ap , bp = random.randint(-50,50) , random.randint(-50,50)
m , n = random.randint(-50,50) , random.randint(-50,50)

punto_1 = a , b
punto_2 = ap , bp
punto_3 = m , n

if punto_1 == punto_2 or punto_1 == punto_3 or punto_2 == punto_3:
    print(f"Error al elegir los puntos\
        \nNo se puede formar la circunferencia")

else:

    # Análisis algebraico para hallar el centro de la cia
    # Metodo de determinantes 2x2
    # distancia_centro_A = distancia_centro_B = distancia_centro_C

    alfa = -2*a + 2*ap
    beta = -2*b + 2*bp
    gama = -a**2 + ap**2 - b**2 + bp**2

    alfa_p = -2*a + 2*m
    beta_p = -2*b + 2*n
    gama_p = -a**2 + m**2 - b**2 + n**2

    determinante_h = gama * beta_p - gama_p * beta
    determinante_k = alfa * gama_p - alfa_p * gama
    determinante = alfa * beta_p - alfa_p * beta

    h = determinante_h / determinante
    k = determinante_k / determinante

    #"Puntos: ({a} , {b}) , ({ap} , {bp}) , ({m} , {n})")
    #"h: {h} , k: {k}")
    #

