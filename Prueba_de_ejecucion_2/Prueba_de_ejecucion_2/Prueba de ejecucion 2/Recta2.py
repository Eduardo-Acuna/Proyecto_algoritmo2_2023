from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: En esta función hay un pequeño problema, la fórmula de pendiente es - A / B y ese - (menos) de la fórmula
está calculada dentro de la función, que quiere decir, que si tu intención es poner una pendiente negativa, solo tienes
que poner la pendiente en su forma positiva y la función se encarga de poner en negativa. Pero si tu idea es poner una
pendiente positiva, entonces deberías de poner una pendiente negativa y la función se encarga de pasar a positiva

usuario ingresa pendiente positiva -----> función pasa a negativa --> 2/3 ingresado --> -2/3 final
usuario ingresa pendiente negativa -----> función pasa a positiva --> 14/-13 ingresado --> 14/13 final

"""

a , b = 5 , -7
mx , my = 3 , -4

ecuacion = Recta2(a , b , mx , my)
#ecuacion = Recta2(a , b , mx , my).replace(' ' , '') # Cadena sin espacios


print(f'Punto: {a} , {b}')
print(f'Pendiente: - ( {mx}/{my} )')
print(f'\nEcuación formada: {ecuacion}')
