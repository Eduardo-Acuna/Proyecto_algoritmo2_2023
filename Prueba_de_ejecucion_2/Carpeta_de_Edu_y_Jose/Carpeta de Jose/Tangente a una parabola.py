#from clase_geo import*
from clase_geo_Gral import*
#from funcion_geo import*
from funcion_geo_Gral import*
#from Funcion_Circunf2 import*
from Funcion_Gral import*
from fractions import Fraction

# Importante que los puntos que vayan a probar tiene que ser un punto que pertenezca a la parábola
# Caso contratio, el codigo no funcionará
# El caso cuando el punto sea exterior voy a poner un None o False com resultado el día de mañana

parabola = 'y²-4x+8y+44=0'
parabola = aux_ordenar_ecuación_final_float(parabola)
a , b = 11 , -8
tangente = Tangente_parabola(parabola , a , b)

print(f'Parábola: {parabola}')
print(f'Punto sobre parábola --> a: {a} , b: {b}')

print(f'\nEcuación tangente a punto (a , b):\n{tangente} ')