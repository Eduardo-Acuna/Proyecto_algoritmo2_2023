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


num = 1.125
den = -2.4375
division = num / den
pendiente = str( Fraction(division).limit_denominator() )

# Se encarga de obtener el signo_pendiente de la pendiente
signo_pendiente = obtener_signo_pendiente(pendiente)

# Se encarga de obtener el valor absoluto del numerador/denominador de la pendiente
numerador_final , denominador_final = obtener_partes_pendiente(pendiente)


print(f'pendiente: {pendiente} , {type(pendiente)}')
print(f'Signo pendiente: {signo_pendiente}')

print(f'\nNumerador: {numerador_final} , {type(numerador_final)}')
print(f'Denominador: {denominador_final} , {type(denominador_final)} ')

# Creación de los datos de la pendiente, datos que después se usarán para calcular la perpendicular'
'Perpendicular entre el punto medio y el punto ingresado por el usuario'
'Dicha recta perpendicular es la tangente de la parábola en el punto dado, ver imagen'
division = num / den
pendiente = str( Fraction(division).limit_denominator() )

# Se encarga de obtener el signo_pendiente de la pendiente
signo_pendiente = obtener_signo_pendiente(pendiente)

# Se encarga de obtener el valor absoluto del numerador/denominador de la pendiente
numerador_final , denominador_final = obtener_partes_pendiente(pendiente)
if signo_pendiente == '-':
    numerador_final *= -1 # También se puede usar el denominador_final para esto, es lo mismo


print(f'Pendiente: {pendiente}')
print(f'Signo pendiente: {signo_pendiente}')
print(f'Numerador pendiente: {numerador_final}')
print(f'Denominador pendiente: {denominador_final}')