from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

# Constantes recta lineal
recta = '-5y+30=0'
recta = aux_ordenar_ecuación_final_float(recta) # Primero hay que ordenar
A , B , C = aux_encontrar_constantes_recta(recta) # Ahora recién podemos obtener las constantes

# Constantes recta circunferencia
cia = 'x2+y2+5x-12y-3=0' #x²+y²+5x-12y-3=0
cia = aux_ordenar_ecuación_final_float(cia) # Primero hay que ordenar
h , k , r = cia_encontrar_hkr_cadena(cia) # Luego obtenemos centro y radio
D , E , F = cia_encontrar_constantes_DEF(cia) # Ahora recién podemos obtener las constantes

# Intersección de ambas rectas
a , b , c , d = interseccion_recta_cia(recta , cia)

# Impresiones
print(f"Recta: {recta}")
print(f"Constantes -> A: {A} , B: {B} , C: {C} ")

print(f"\nCircunferencia: {cia}")
print(f"Ubicación -> Centro({h} , {k}) , Radio: {r}")
print(f"Constantes -> D: {D} , E: {E} , F: {F}")

print(f"\nLa intersección de ambas rectas son: ")
print(f'\nPunto 1: {a} , {b}')
print(f'Punto 2: {c} , {d}')
