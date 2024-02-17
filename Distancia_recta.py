from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Siempre llamar a la función aux_ordenar_ecuación_final_float() o aux_ordenar_ecuación_final() de forma de actualizar
la recta obtenida o crear una nueva variable de recta ya ordenada y corregida, no esperen que le usuario ponga de forma
comoda un recta con la cual se pueda trabajar, por eso hay que corregir la cadena antes de obtener la distancia

No hay mucho que saber sobre esta función, es lógica sencilla. No usar metodos de clases para obtener la cadena, solo
llamada de funcion de ordenacion que son 2

"""

a , b = -14 , 8
recta = '15x-12y+27-3+x=-4x+2y+50'
recta = aux_ordenar_ecuación_final_float(recta)

distancia_punto_recta = Distancia_recta(a , b , recta)

print(f'Punto: {a} , {b}')
print(f'Recta: {recta}')
print(f'Distancia: {distancia_punto_recta}')

