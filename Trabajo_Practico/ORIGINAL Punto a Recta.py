from clase_geo import*
from funcion_geo import*

"""Codigo hecho para ingresar dos puntos y te retorne una recta sin ordenar, con la clase de Recta
se ordena por sí solo de forma automática. 2 puntos = 1 recta"""

# Ver caso cuando -1y , 1y , -1x , 1x. Casos especiales
n1_x , n1_y = -10 , -1
n2_x , n2_y = -15 , 14

punto_1 = Fraccion(n1_x , n1_y)
punto_2 = Fraccion(n2_x , n2_y)
pendiente = punto_1.pendiente(punto_2)
Np = abs(pendiente.obtener_numerador_simplificado()) # Numerador pendiente - Np, ATENDER! porque el signo reposa por éste (analítica)
Dp = abs(pendiente.obtener_denominador_simplificado()) # Denominador pendiente - Dn (siempre positivo, siempre)
'Hay 1 solo error en donde el Dp retorna negativo, cuando Np == 0 and n1_x < n2_x '
'El problema está en algun lugar de pendiente, Class Fraccion o obtener_numerador y denominador simplificado'
'No logro corregir en el código fuente'
sin_error_CF = True
if Np == 0 and Dp == -1:
    sin_error_CF = False
aux_encontrar_signo_pendiente(pendiente)

'                      Ecuación punto-pendiente de la recta                      '
'Solo el signo de Np puede variar, Dp siempre y siempre será positivo (hacer parte analítica para entender)'
'   CTE,VAR          PURO CTE                            CTE,VAR          PURO CTE '
# ( Dp * 'y' )  -  ( Dp * n1_y)  atender {-} atender  ( Np * 'x' )  +  ( Np * n1_x )  =  0
'no cambia nunca de signo - Término 1'
'                   cambia siempre de signo - Término 2'
'                                                     if necesario, dos casos posibles - Término 3'
'                                                                       if necesario, dos casos posibles - Término 4'

# CTE,VAR  - uno    =    [      Dp * 'y'      ] signo siempre positivo
# PURO CTE - dos    =    [      Dp * n1_y     ] signo depende del signo de la coordenada del punto elegido
# CTE,VAR  - tres   =    [      Np * 'x'      ] signo depende del signo de la pendiente , + ---> - , - ---> +
# PURO CTE - cuatro =    [      Np * n1_x     ] signo depende del signo de la pendiente , + ---> + , - ---> -

'Apilado para cada término segun su caso'
uno , dos , tres , cuatro = [] , [] , [] , []

# Caso 1
agregar_uno = str(Dp) + 'y'
uno.append(agregar_uno) # El más fácil y sin ninguna restricción, no cambia nunca de signo, siempre +
# Caso 2
agregar_dos = Dp * n1_y # Despues usar str(), ahora sirve mas como tipo int()
dos.append(agregar_dos * -1) # Cambia siempre de signo

# Caso 3 y 4
if aux_encontrar_signo_pendiente == '+':
    agregar_tres = str(Np) + 'x'
    tres.append('-' + agregar_tres)

    agregar_cuatro = Np * n1_x # Despues usar str(), ahora sirve mas como tipo int() (ver print)
    
    cuatro.append(agregar_cuatro)

else:
    agregar_tres = '+' + str(Np) + 'x' # Si la pendiente es negativa, se anula el negativo con el de la fórmula
    tres.append(agregar_tres) # Se agrega con el '+'

    agregar_cuatro = -1 * Np * n1_x # Despues usar str(), ahora sirve mas como tipo int() (ver print)
    cuatro.append(agregar_cuatro)

CTE = dos[0] + cuatro[0]
if CTE >= 0:
    CTE = '+' + str(CTE)

ecuacion_formada = uno + tres
ecuacion_formada.append(CTE)


# Se encarga de analizar cada término de la lista ecuacion_formada y corregir todos los errores posibles
for i in range( len(ecuacion_formada) - 1 ):

    termino = ecuacion_formada[i]

    BANDERA = True # Bandera para corroborar si se modificará o el término de la lista
    while True:

        agregar = ''

        txt_signo = '+'
        txt_entero = ''
        txt_variable = False

        # Se encarga de analizar todos los carácteres de cada término de la ecuación
        for caracter in str(termino):

            if caracter in '+-':
                txt_signo = caracter

            elif caracter in '0132456789':
                txt_entero += caracter
            
            elif caracter == 'x' or caracter == 'y':
                txt_variable = caracter

        if sin_error_CF:

            if txt_signo in '+-' and i != 0:
                agregar += txt_signo

        if len(txt_entero) > 0: # txt_entero es de tipo cadena

            if int(txt_entero) == 0:
                BANDERA = False
                break # Esto detiene el while True

            elif int(txt_entero) > 1:
                agregar += txt_entero

        if txt_variable:
            agregar += txt_variable

        break
    
    if BANDERA:
        ecuacion_formada[i] = agregar
    
    else:
        ecuacion_formada.pop(i)

# Solo en el caso del error del codigo fuente, aquí se soluciona el último término
if sin_error_CF == False:

    if ecuacion_formada[-1] != 0:
        ecuacion_formada[-1] = ecuacion_formada[-1] * -1
    
    else:
        indice = len(ecuacion_formada) - 1
        ecuacion_formada.pop(indice)

# Itera todos los elementos de lista ecuacion_formada en una cadena
cadena_obtenida = ''
for elemento in ecuacion_formada:
    cadena_obtenida += str(elemento)


# Impresiones
print(f"punto_1: {punto_1}")
print(f"punto_2: {punto_2}")

print(f"\nPendiente: {pendiente} , {type(pendiente)}")
print(f"Signo_dependiente: {aux_encontrar_signo_pendiente}")

print(f"\nNumerador_pendiente  : {Np}")
print(f"Denominador_pendiente: {Dp}")

print(f"\nUno:    {uno}  -  {type(uno[0])}")
print(f"Dos:    {dos}  -  {type(dos[0])}")
print(f"Tres:   {tres}  -  {type(tres[0])}")
print(f"Cuatro: {cuatro}  -  {type(cuatro[0])}")

print(f"\nLista ecuación: {ecuacion_formada} , CTE: {CTE}")
print(f"\nCadena sin terminar: {cadena_obtenida}")

a , b , c = aux_encontrar_constantes_recta(aux_ordenar_ecuación_final(cadena_obtenida))
recta_objeto = Recta(a , b , c)
print(f"\nEcuación final: {recta_objeto}")

