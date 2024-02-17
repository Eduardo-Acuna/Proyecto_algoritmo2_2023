from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: No importa si el radio se pone como r = 15 o r = -15, la función se encarga de tomar el valor absoluto del radio,
ya que no puede existir una circunferencia con radio negativo, al menos en nuestro nivel de ingenieria. Función sencilla
no hay tantas cosas que atender de él. Mismo caso para cadena sin espacios

"""

def calcular_ecuacion(a,b,radio):
    #a , b = 7 , 5
    #radio = 8

    ecuacion_cia = Circunf1(a , b , radio)

    return ecuacion_cia
#ecuacion_cia = Circunf1(a , b , radio).replace(' ' , '') # Cadena sin espacios

#print(f'Punto: {a} , {b}')
#print(f'Radio: {radio}')
#print(f'Ecuación de CIA: {ecuacion_cia}')