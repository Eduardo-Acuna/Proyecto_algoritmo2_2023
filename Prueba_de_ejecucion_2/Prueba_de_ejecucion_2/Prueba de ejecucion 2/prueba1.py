#from clase_geo import*
from clase_geo_Gral import*
#from funcion_geo import*
from funcion_geo_Gral import*
#from Funcion_Circunf2 import*
from Funcion_Gral import*
from fractions import Fraction

def obtener_signo_pendiente(pendiente):
    # Se encarga de obtener el signo_pendiente de la pendiente
    signo_pendiente = '+'
    for caracter in pendiente:
        if caracter == '-':
            signo_pendiente = '-'
            break
    
    return signo_pendiente

def obtener_partes_pendiente(pendiente):
    # Se encarga de obtener el numerador y denominador en valor absoluto
    txt_num , txt_den = '' , ''

    if '/' in pendiente:
        separador = pendiente.index('/')

        for i in range(0 , separador):
            txt_num += pendiente[ i ]

        for k in range(separador + 1 , len(pendiente)):
            txt_den += pendiente[ k ]

    else:
        txt_num = pendiente
        txt_den = '1'

    return int(txt_num.lstrip('-')) , int(txt_den)

def obtener_cte_directriz_p_negativa(k , p):

    # Se encarga de formar la ecuación de la directriz de la parábola
    parte_numerica_directriz = abs(k) - abs(p / 2) # El parámetro de mi código es 2 veces el real

    if parte_numerica_directriz >= 0:
        directriz =  f'y + {parte_numerica_directriz} = 0' 
    else:
        directriz =  f'y - { abs(parte_numerica_directriz) } = 0' 
    
    return parte_numerica_directriz

def para_y_directriz_p_negativa(h , p):

    # Se encarga de formar la ecuación de la directriz de la parábola
    parte_numerica_directriz = abs(h) - abs(p / 2) # El parámetro de mi código es 2 veces el real

    if parte_numerica_directriz >= 0:
        directriz =  f'x + {parte_numerica_directriz} = 0' 
    else:
        directriz =  f'x - { abs(parte_numerica_directriz) } = 0' 
    
    return directriz

def para_y_directriz_p_positiva(h , p):

    # Se encarga de formar la ecuación de la directriz de la parábola
    parte_numerica_directriz = abs(h) - abs(p / 2) # El parámetro de mi código es 2 veces el real

    if parte_numerica_directriz >= 0:
        directriz =  f'x - {parte_numerica_directriz} = 0' 
    else:
        directriz =  f'x + { abs(parte_numerica_directriz) } = 0'
    
    return directriz

cadena = 'x²-4x-8y+44=0' # x2-4x-8y+44=0 , y2-4y+4=-3x-21 , 7x² - 14x + 56y - 8 = 0
h , k , p , fx , fy , bandera = Foco_parabola(cadena)
usuario_x , usuario_y = 10 , 13

if bandera == 'x2':

    if p < 0:

        # Se encarga de formar la ecuación de la directriz de la parábola
        parte_numerica_directriz = abs(k) - abs(p / 2) # El parámetro de mi código es 2 veces el real

        if parte_numerica_directriz >= 0:
            directriz =  f'y + {parte_numerica_directriz} = 0' 
        else:
            directriz =  f'y - { abs(parte_numerica_directriz) } = 0' 

    else:

        # Se encarga de formar la ecuación de la directriz de la parábola
        parte_numerica_directriz = abs(k) - abs(p / 2) # El parámetro de mi código es 2 veces el real

        if parte_numerica_directriz >= 0:
            directriz =  f'y - {parte_numerica_directriz} = 0' 
        else:
            directriz =  f'y + { abs(parte_numerica_directriz) } = 0' 
    
    # Se crea una recta auxiliar y perpendicular a la directriz en el punto dado por el usuario
    recta_aux = Perpendicular(directriz , usuario_x , usuario_y)
    interseccion_abs , interseccion_ord = interseccion_recta_recta(directriz , recta_aux)

    # Se encarga de encontar el punto medio entre la intersección creada y el foco
    medio_absica , medio_ordenada = (fx + interseccion_abs) / 2 , (fy + interseccion_ord) / 2

    # Ahora se puede obtener la ecuación de la recta tangente en el punto dado
    recta_tangente = recta1(usuario_x , usuario_y , medio_absica , medio_ordenada)

else:

    if p < 0:

        # Se encarga de formar la ecuación de la directriz de la parábola
        parte_numerica_directriz = abs(h) - abs(p / 2) # El parámetro de mi código es 2 veces el real

        if parte_numerica_directriz >= 0:
            directriz =  f'x + {parte_numerica_directriz} = 0'
        else:
            directriz =  f'x - { abs(parte_numerica_directriz) } = 0'

    else:

        # Se encarga de formar la ecuación de la directriz de la parábola
        parte_numerica_directriz = abs(h) - abs(p / 2) # El parámetro de mi código es 2 veces el real

        if parte_numerica_directriz >= 0:
            directriz =  f'x - {parte_numerica_directriz} = 0' 
        else:
            directriz =  f'x + { abs(parte_numerica_directriz) } = 0' 

    # Se crea una recta auxiliar y perpendicular a la directriz en el punto dado por el usuario
    recta_aux = Perpendicular(directriz , usuario_x , usuario_y)
    interseccion_abs , interseccion_ord = interseccion_recta_recta(directriz , recta_aux)

    # Se encarga de encontar el punto medio entre la intersección creada y el foco
    medio_absica , medio_ordenada = (fx + interseccion_abs) / 2 , (fy + interseccion_ord) / 2

    # Ahora se puede obtener la ecuación de la recta tangente en el punto dado
    recta_tangente = recta1(usuario_x , usuario_y , medio_absica , medio_ordenada)

print(
        f'Cadena: {aux_ordenar_ecuación_final_float(cadena)}'
        f' , Tipo: {bandera}'
)

print(f'\nVértice --> h: {h} , k: {k}')
print(f'Foco --> fx: {fx} , fy: {fy}')
print(f'Parámetro: {p}')

print(f'\nParte entera directriz: {parte_numerica_directriz}')
print(f'Directriz: {directriz}')

print(f'\nAux perpendicular: {recta_aux}')
print(f'Interseccion Directriz/Aux \nabsica: {interseccion_abs} , ordenada: {interseccion_ord}')

print(f'\nPunto medio --> mx: {medio_absica} , my: {medio_ordenada}')


print(f'\nEcuación tangente: {recta_tangente} ')