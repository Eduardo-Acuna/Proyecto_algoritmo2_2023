from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

# Pueden poner tambien como varibables las cadenas e ingresar como argumento en la función

recta = '8x-4y+5=0' 
parabola = 'y²+4x+8y-70=0'

# La función interseccion_recta_parabola ya hace todo, no hace falta llamar otra función
x1 , x2 , y1 , y2 = interseccion_recta_parabola(recta , parabola)

print(f'Recta: {recta}')
print(f'Parábola: {parabola}')

print(f'\nIntersección')
print(f'\nPunto 1:\nx1: {x1} , y1: {y1}')
print(f'\nPunto 2:\nx2: {x2} , y2: {y2}')
