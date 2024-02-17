from clase_geo import*
from funcion_geo import*
from Funcion_Circunf2 import*

a , b = -10 , -1 # Punto
mx , my = -15 , 14

signo_pendiente = recta_signo_pendiente(mx , my)

if b >= 0:
    signo_b = '+'
else:
    signo_b = '-'

'                      Ecuación punto-pendiente de la recta                      '
'Solo el signo de Np puede variar, Dp siempre y siempre será positivo (hacer parte analítica para entender)'
'   CTE,VAR          PURO CTE                            CTE,VAR          PURO CTE '
# ( my * 'y' )  -  ( my * b)  atender {-} atender  ( mx * 'x' )  +  ( mx * a )  =  0
'no cambia nunca de signo - Término 1'
'                   cambia siempre de signo - Término 2'
'                                                     if necesario, dos casos posibles - Término 3'
'                                                                       if necesario, dos casos posibles - Término 4'

# CTE,VAR  - uno    =    [      my * 'y'      ] signo siempre positivo
# PURO CTE - dos    =    [      my * b     ] signo depende del signo de la coordenada del punto elegido
# CTE,VAR  - tres   =    [      mx * 'x'      ] signo depende del signo de la pendiente , + ---> - , - ---> +
# PURO CTE - cuatro =    [      mx * a     ] signo depende del signo de la pendiente , + ---> + , - ---> -

# Primer término - VARIABLE y
uno , signo_uno = f"{ str( abs(my) ) + 'y'  }" , '+'

# Segundo término - CONSTANTE
if signo_b == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
    dos , signo_dos = (my * b) * -1 , '-'
else:
    dos , signo_dos = abs(my * b) , '+'

# Tercer término - VARIABLE x
if signo_pendiente == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
    tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '-'
else:
    tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '+'

# Cuarto término - CONSTANTE
if mx * a >= 0:
    cuatro , signo_cuatro = abs(mx * a) , '+'
else:
    cuatro , signo_cuatro = mx * a , '-'

terminos , signos = [] , []

'Las siguientes funciones analizan solo la parte entera de una variable'

if aux_operando_x(tres) != 0: # Si el entero de x (tres) no es 0, entonces se agrega a la lista
    terminos.append(tres)
    signos.append(signo_tres)

if aux_operando_y(uno) != 0: # Si el entero de y (uno) no es 0, entonces se agrega a la lista
    terminos.append(uno)
    signos.append(signo_uno)

if dos + cuatro != 0:
    terminos.append( abs(dos + cuatro) )

    if dos + cuatro > 0:
        signos.append('+')
    else:
        signos.append('-')

# Se encarga de encontrar la ecuación formada, ordenada pero sin espacios. Otra función hace eso
cadena = ''
for i in range( len(terminos) ):
    cadena += str(signos[ i ]) + str(terminos[ i ])


print(f"uno    : {signo_uno}{uno}  , {type(uno)}")
print(f"dos    : {signo_dos}{dos}  , {type(dos)}") # ENTERO
print(f"tres   : {signo_tres}{tres} , {type(tres)}")
print(f"cuatro : {signo_cuatro}{cuatro}   , {type(cuatro)}") # ENTERO

print(f"\nTérminos: {terminos}")
print(f"Signos  : {signos}")

print(f"\nCadena: {cadena}")
print(f"\nEcuación formada: {aux_ordenar_ecuación_final(cadena)}")

