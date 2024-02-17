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

recta = '4x+5=0' # Ax + By + C = 0
parabola = 'y²+4x+4y-20=0' # ax² + by² + cx + dy + e = 0 , con (a=0 o b=0)

noseusa , noseusa , noseusa , noseusa , noseusa , bandera = Foco_parabola(parabola) # Solo importa bandera

# Datos sacados de recta lineal
recta = aux_ordenar_ecuación_final_float(recta)
A , B , C = aux_encontrar_constantes_recta_float(recta)

# Datos sacados de la parábola
parabola = aux_ordenar_ecuación_final(parabola)
c , d , e = para_encontrar_constantes_CDE(parabola)

# Algoritmo de solución para ambos casos de parábola
if bandera == 'x2':

    a = aux_operando_x2( coeficiente_cuadratica(parabola).upper() )

    if A != 0 and B != 0:
        
        # Ecuación cuadrática (primero)x² + (segundo)x + (tercero) = 0
        primero = a*B
        segundo = c*B - d*A
        tercero = e*B - C*d
        ecuacion = SegundoGrado(primero , segundo , tercero)

        # Calculo de las ráices de los puntos de intersección
        x1 , x2 = ecuacion.hallar_raices()
        y1 , y2 = (A*x1 + C)*-1 / B , (A*x2 + C)*-1 / B

    elif A == 0 and B != 0:
        
        # Ecuación cuadrática (primero)x² + (segundo)x + (tercero) = 0
        primero = a
        segundo = c
        tercero = e - (C/B)
        ecuacion = SegundoGrado(primero , segundo , tercero)

        # Calculo de las ráices de los puntos de intersección
        x1 , x2 = ecuacion.hallar_raices()
        y1 , y2 = -(C/B) , -(C/B)
    
    elif A != 0 and B == 0:

        x1 , x2 = -(C/A) , None
        y1 , y2 = (a*(C**2) - c*A*C + e*(A**2)) / -(d*(A**2)) , None

    else:

        x1 , x2 , y1 , y2 = None , None , None , None

elif bandera == 'y2':

    b = aux_operando_y2( coeficiente_cuadratica(parabola).upper() )

    if A != 0 and B != 0:

        # Ecuación cuadrática (primero)y² + (segundo)y + (tercero) = 0
        primero = A*b
        segundo = A*d - c*B
        tercero = A*e - c*C

        ecuacion = SegundoGrado(primero , segundo , tercero)

        y1 , y2 = ecuacion.hallar_raices()
        x1 , x2 = -(B*y1 + C) / A , -(B*y2 + C) / A

    elif A == 0 and B != 0:

        x1 , x2 = (b*(C**2) - d*B*C + e*(B**2)) / -(c*(B**2)) , None
        y1 , y2 = -(C/B) , None

    elif A != 0 and B == 0:

        # Ecuación cuadrática (primero)y² + (segundo)y + (tercero) = 0
        primero = b
        segundo = d
        tercero = e - ((c*C) / A)

        ecuacion = SegundoGrado(primero , segundo , tercero)
        y1 , y2 = ecuacion.hallar_raices()
        x1 , x2 = -(C/A) , -(C/A)

    else:

        x1 , x2 , y1 , y2 = None , None , None , None

print(
f'Recta: {recta}'
f'\nConstantes --> A:{A} , B: {B} , C: {C} '
      )

print(
f'\nParábola: {parabola}'
f'\nConstantes:\nc:{c}\nd: {d}\ne: {e} '
      )

print(f'\nPunto 1:\nx1: {x1} , y1: {y1}')
print(f'\nPunto 2:\nx2: {x2} , y2: {y2}')