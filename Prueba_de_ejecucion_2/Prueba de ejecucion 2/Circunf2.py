from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Como el radio no siempre será un valor entero, y en a lógica aplicada para obtener la cadena llegamos una expresión
como esta --> a , b , c = -2*h , -2*k , h**2 + k**2 - round(r**2 , 4) y es en el último término en donde está un ajuste

- round(r**2 , 4) puede ser tambien simplemente - r**2, pero imagense elevar al cuadrado un número con decimales finitos
dará como resultado un número con más decimales finitos y quedaba feo en la impresión. Por eso obté con el rount()
también en comparación a geogebra, ellos hacen con un redondeo muy preciso, por eso esta función no es 100% igual a 
geogebra, entra en debate de cuandos decimales quieren que tenga la expresión, yo puse 4 y ya

Mismo caso para la cadena sin espacios

"""

a , b = 5 , -7
m , n = -4 , 0
p , q = 8 , 8

ecuacion_cia = Circunf2(a , b , m , n , p , q)

#ecuacion_cia = Circunf2(a , b , m , n , p , q).replace(' ' , '') # Cadea sin espacios

print(f': {a} , {b}')
print(f': {m} , {n}')
print(f': {p} , {q}')
print(f'\nEcuación CIA: {ecuacion_cia}')
