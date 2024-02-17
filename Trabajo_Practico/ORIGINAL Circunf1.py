from clase_geo import*
from funcion_geo import*
from Funcion_Circunf2 import*

h , k , r = 25 , -13 , 15

a , b , c = -2*h , -2*k , h**2 + k**2 - r**2
#c *= -1

# Se encarga de agregar las constantes y sus signos en diferentes listas
constantes , signos , terminos = [a , b , c] , [] , []
for i in range( len(constantes) ):
    elementos = constantes[ i ]

    if elementos >= 0:
        signos.append('+')
    else:
        signos.append('-')

# Se encarga de agregar las constantes con sus respectivas variables y signos 
for i in range( len(constantes) ):
    elementos = constantes[ i ]

    if i == 0:
        if signos[ i ] == '+':
            terminos.append( '+' + str(constantes[i]) + 'x' )
        else:
            terminos.append( str(constantes[i]) + 'x' )
    
    elif i == 1:
        if signos[ i ] == '+':
            terminos.append( '+' + str(constantes[i]) + 'y' )
        else:
            terminos.append( str(constantes[i]) + 'y' )
    
    elif i == 2:

        if constantes[ i ] > 0:
            terminos[i - 1] += '+' # Se le pone el más al final del terminos anterior, porque o si no habrá problemas
            # con las funciones creadas para cónicas y sus análisis. Ya que la igualdad = es un punto de referencia
            # de la constante C, y si el usuario no lo pone, entonces habrá problemas. Por eso este análisis
            terminos.append( constantes[ i ] )
        elif constantes[ i ] == 0:
            terminos.append( 0 )
        else:
            terminos.append( constantes[ i ] )

# Se encarga de pasar a cadena los términos ya trabajados
txt = ''
for elementos in terminos:
    txt += str(elementos)

# Cadena final sin espacios y ordenada
cadena = 'x2+y2' + txt + '=0'
cadena = aux_corregir_espacios(cadena)


print(f"Constantes: {constantes}")
print(f"Signos: {signos}")
print(f"Terminos: {terminos}")
print(f"\nCadena: {cadena}")
