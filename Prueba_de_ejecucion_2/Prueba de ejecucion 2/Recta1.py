from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Solo tienen que imprimir ecuacion sin agregar ningun tipo de funcion ni nada, dentro de Recta1 ya está todo hecho,
ahora si quieren que le retorne la ecuacion sin espacios, dejo debajo de ecuacion su segunda forma de obtener. El compañero
había dicho que si la cadena no tiene espacios, se generán problemas

"""


a , b = 7 , -4
m , n = -5 , 8

ecuacion = Recta1(a , b , m , n)
#ecuacion = Recta1(a , b , m , n).replace(' ' , '') # Cadena sin espacios

print(f'Punto 1: {a} , {b}')
print(f'Punto 2: {m} , {n}')
print(f'\nEcuación formada: {ecuacion}')
