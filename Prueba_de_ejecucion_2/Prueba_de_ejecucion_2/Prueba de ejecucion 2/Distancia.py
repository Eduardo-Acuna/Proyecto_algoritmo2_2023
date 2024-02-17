from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Para este ejercicio no existe ninguna función en el archivo Funcion_Circunf2.py, si no que existe una operación
dentro de clase Punto() que tiene el cálculo de distancia entre puntos, ahora si estos mismos puntos que van a usarse
para obtener distancia, se quieren usar para otro tipo de operacion que hay en el PDF, deberían de crear otras variables
identicas, variables para usar en otras funciones y variables para usar en distancia. Ya que mezclar una variable de
tipo de dato objeto con tipo de datos funciones, podría ocasionar problemas. Pero como es un ejercicio solo de distancia
(valor numérico), entonces no me vi en la necesidad de crear una función extra. Si no reutilizar lo que ya tenía

Información importante, siempre que quieran saber el tipo de datos de una variable, tiene que hacer lo siguiente

variable = 'Cualquier cosa'
print(f'  { type( variable ) }  ' ) Con eso la terminal le dice el tipo de variable

"""

a , b = 4 , -13
m , n = -5 , -8

punto1 = Punto(a , b)
punto2 = Punto(m , n)

distancia = punto1.distancia_punto(punto2)

print(f'Puntos: {a} , {b} , {type(a)} , {type(b)}')
print(f'Puntos: {m} , {n} , {type(m)} , {type(n)}')

print(f'\nTipo de datos de punto1 y punto2 --> \n{type(punto1)}  , {type(punto2)}')

print(f'\nDistancia: {distancia} , {type(distancia)}')