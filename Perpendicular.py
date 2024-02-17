from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Primero llamar a una nueva recta_referencia o simplemente actualizar esa variable pero llamando a la función
aux_ordenar_ecuación_final_float() o aux_ordenar_ecuación_final(); NO! convertir la recta_referencia en un objeo de la clase
Recta, tiene que ser distinto a un objeto en este caso. Si quieren obtner la ecuación de la paralela sin espacios, es el
mismo codigo de .replace(' ' , '') que deben de usar


"""

recta_referencia = '2x-4y+56=-7x+7y+16'
recta_referencia = aux_ordenar_ecuación_final_float(recta_referencia)
a , b = 14 , 15

recta_perpendicular = Perpendicular(recta_referencia , a , b)
#recta_perpendicular = Perpendicular(recta_referencia , a , b).replace(' ' , '') # Cadena sin espacios

print(f'Recta referencia: {recta_referencia}')
print(f'Punto donde pasa la paralela: {a} , {b}')
print(f'\nParalela: {recta_perpendicular}')