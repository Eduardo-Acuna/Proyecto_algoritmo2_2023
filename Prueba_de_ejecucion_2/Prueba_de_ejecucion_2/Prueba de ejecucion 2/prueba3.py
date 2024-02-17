#from clase_geo import*
from clase_geo_Gral import*
#from funcion_geo import*
from funcion_geo_Gral import*
#from Funcion_Circunf2 import*
from Funcion_Gral import*
from fractions import Fraction

def para_x_directriz_p_negativa(k , p):

    # Se encarga de formar la ecuación de la directriz de la parábola
    parte_numerica_directriz = abs(k) - abs(p / 2) # El parámetro de mi código es 2 veces el real

    if parte_numerica_directriz >= 0:
        directriz =  f'y + {parte_numerica_directriz} = 0' 
    else:
        directriz =  f'y - { abs(parte_numerica_directriz) } = 0' 
    
    return directriz

def para_x_directriz_p_positiva(k , p):

    # Se encarga de formar la ecuación de la directriz de la parábola
    parte_numerica_directriz = abs(k) - abs(p / 2) # El parámetro de mi código es 2 veces el real

    if parte_numerica_directriz >= 0:
        directriz =  f'y - {parte_numerica_directriz} = 0' 
    else:
        directriz =  f'y + { abs(parte_numerica_directriz) } = 0' 

    return directriz

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


