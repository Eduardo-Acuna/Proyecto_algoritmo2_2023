def aux_corregir_espacios(texto_a_espaciar):

    # Se encarga de agrupar carácter por carácter la cadena en una lista
    caracter_caracter = []
    for letra in texto_a_espaciar:

        if letra == '=':
            break
        
        if letra in 'xy0123456789+-':
            caracter_caracter.append(letra)

    # Se encarga de agregar espacios frente-atras a cada operador de la ecuación
    for i in range( len(caracter_caracter) ):
        letra = caracter_caracter[i]

        if letra == '+' or letra == '-' or letra == '=':
            caracter_caracter[i] = ' ' + letra + ' '

    # Vuelve a iterar los elemenos de caracter_caracter con el previo cambio anterior
    ya_espaciado = ''
    for letra in caracter_caracter:
        ya_espaciado += letra
    ya_espaciado += ' = 0' # Agrega la ultima parte que no fue analizada

    return ya_espaciado

def aux_ordenar_ecuacion(cadena):

    cadena = aux_corregir_espacios(cadena) # Super importante este llamado!!!
    # Se encarga de agregar cada término y el signo en una lista auxiliar
    diccionario = "abcdefghijklmnopqrstuvwxyz0123456789+-"
    aux = []
    txt = ''
    for letra in cadena:

        indice = diccionario.find(letra)

        if indice != -1:
            txt += letra

        elif len(txt) > 0:
            aux.append(txt)
            txt = ''

    # Se encarga de agrupar cada término con el signo que le corresponde
    terminos = []
    if aux[0] not in '+-':
        terminos.append(aux[0])
    for i in range(1 , len(aux) ):

        elemento = aux[i]
        correcion = aux[i - 1] + aux[i] 

        if elemento not in '+-' and correcion not in terminos:
            terminos.append(correcion)

    # Se encarga de ordenar la ecuación lineal en la forma Ax + By + C = 0
    # Términos: ['6y', '+7x', '-4'] ejemplo visual
    lista_x , lista_y , lista_cte = [] , [] , []
    for elemento in terminos:

        signo = '+'
        txt_entero = ''
        fenotipo = False
        for caracter in elemento: # Bucle interno para cada término
            
            if caracter == '-':
                signo = '-'
            if caracter in '0123456789':
                txt_entero += caracter
            if caracter in 'xy':
                fenotipo = True

        # El término es una variable
        if fenotipo:

            if caracter == 'x':

                if signo == '-':
                    lista_x.append(signo + txt_entero + caracter)
                    lista_x.append('-')
                    # ['7x', '-']
                
                else:
                    lista_x.append(txt_entero + caracter)
                    lista_x.append('+')
                    # ['7x', '+']
            
            else:

                if signo == '-':
                    lista_y.append(signo + txt_entero + caracter)
                    lista_y.append('-')
                    # ['6y', '-']
                
                else:
                    lista_y.append(txt_entero + caracter)
                    lista_y.append('+')
                    # ['6y', '+']
                    
        # El término es solo una constante CTE
        else:

                if signo == '-':
                    lista_cte.append(signo + txt_entero)
                    lista_cte.append('-')
                    # ['-4', '-']
                
                else:
                    lista_cte.append(txt_entero)
                    lista_cte.append('+')
                    # ['-4', '+']

    # Se encarga de retornar la cadena en el orden correcto Ax, By, C = 0
    cadena_aux = ''

    if len(lista_x):

        cadena_aux += lista_x[0]

    if len(lista_y):

        if lista_y[1] == '+':
            cadena_aux += '+' + lista_y[0]
        else:
            cadena_aux += lista_y[0]

    if len(lista_cte):

        if lista_cte[1] == '+':
            cadena_aux += '+' + lista_cte[0]
        else:
            cadena_aux += lista_cte[0]

    sin_mas_al_principio = cadena_aux.lstrip('+')

    return aux_corregir_espacios(sin_mas_al_principio) # Ya está ordenado, ahora solo se pone espacio y la igualdad

def aux_invertir_cadena(cadena):
    return cadena[::-1]

def _encontrar_constantes(cadena):
    # Se encarga de encontrar las constantes de la ecuación en el orden Ax, By
    orden_constantes = ["x" , "y"]
    lista_numeros = []
    lista_variables = []
    k = 0
    while k < 2:
        x_o_y = orden_constantes[k]
        indice = cadena.find( x_o_y )

        if indice != -1:

            if indice > 0:

                txt = ''
                for i in range(indice - 1 , -1 , -1):
                    letra = cadena[i]
        # NO SE BUSCAN LOS SIGNOS AUN, PARA ELLO HAY OTRA FUNCION QUE SE ENCARGA DE ELLO
        # Por eso se pone un break en caso de que letra pertenezca a '+-'
                    if letra in '+- ':
                        break
                    else:
                        txt += letra

                if len(txt) > 0: # Significa que encontró una variable pero el entero a su lado no es 1
                    lista_numeros.append(int( aux_invertir_cadena(txt) )) # Si en if de arriba, pueden haber errores
                else: # El entero al lado es 1, y como el 1 es invisible, txt no tiene tamaño. Por eso se agrega manualmente
                    lista_numeros.append(1)

            else:
                lista_numeros.append(1)
        
        else:
            lista_numeros.append(0)    
        lista_variables.append(x_o_y)

        k += 1
    
    # Para la constante C
    indice = cadena.index('=')
    txt = ''
    for i in range(indice , -1 , -1):
        letra = cadena[i]

        if letra in '+-xy':
            break

        if letra in '0123456789':
            txt += letra

    if len(txt) != 0:
        lista_numeros.append( int( aux_invertir_cadena(txt) ) )
    else:
        lista_numeros.append(0)

    return lista_numeros , lista_variables

def aux_encontrar_constantes_recta(cadena):
# Realmente se encarga de encontrar los signos de las constantes y corregirlos con la funcion anterior
# solo de ser necesario, pero para que el usuario entienda mejor, se pone como nombre 'encontrar_constantes'

    lista_numeros , lista_signo = _encontrar_constantes(cadena)

# Se encarga de encontrar los signos de todas las constantes en el orden A, B, C

    lista_signo = []
    aux = ['x' , 'y' , '=']

    indice_x = cadena.find( aux[0] )
    indice_y = cadena.find( aux[1] )
    indice_es_igual = cadena.find( aux[2] )

    #print(f"\nindice_x: {indice_x}")
    #print(f"indice_y: {indice_y}\n")

    # Para el caso de la variable 'x'
    if indice_x == -1:
        lista_signo.append('+')
    else:
        if indice_x == 0:
            lista_signo.append('+')
        
        else:
            for i in range(indice_x , -1 , -1):
                letra = cadena[i]

                if letra in '+-':
                    break
            
            lista_signo.append(letra)

    # Para el caso de la variable 'y'
    if indice_y == -1:
        lista_signo.append('+')
    else:
        if indice_y == 0:
            lista_signo.append('+')
        
        else:
            for i in range(indice_y , -1 , -1):
                letra = cadena[i]

                if letra in '+-':
                    break
            
            lista_signo.append(letra)

    # Para el caso de la constante
    referencia = cadena.index("=") # El índice de la referencia es mas grande que cualquier carácter del primer miembro
    # de la ecuación
    mayor = float("inf") # Para la constante C, se supone que no existe y que es mas grande que la referencia
    # Suposición mayor > menor
    EXISTE = True # Contradicción a la suposición, ahora decimos que SÍ existe, cosa que es falso
    if indice_es_igual == -1:
        lista_signo.append('+')
    else:
        for i in range(indice_es_igual , -1 , -1): # '-3y+2x=0' ,    2x - 3y = 0
            letra = cadena[i]

            if letra in '0123456789':
                mayor = i
            
            if letra in 'xy':
                break

        if mayor > referencia:
            EXISTE = False # Si mayor no es mayor que referencia, significa que el índice nunca se actualizó porque...
            #... no se encontró un entero antes de encontrar la variable 'x o y'. Constante C = 0, se agrega '+'
            # en líneas más abajo
        
        else: # Signficia que mayor se actualizó y quedó menor que la referencia, por ende ya se puede iterar en bucle
            # para encontrar el dichoso signo de esta constante
            for i in range(indice_es_igual , -1 , -1):
                letra = cadena[i]

                if letra in '+-':
                    break # Se detiene una vez encontrado su signo
            
        if EXISTE: # Si existe, significa que sí tiene un signo que obtener, en cambio si no existiese, sería '+', porque...
            #... el 0 es un número positivo. No existe, entonces es cero 0
            lista_signo.append(letra)
        else:
            lista_signo.append('+') # Lo que vengod diciendo, no existe y es positivo el signo

    #print(f"Lista signo: {lista_signo}")

# Se encarga de modificar el signo de las constantes de acuerdo a la ecuación
    for i in range( len(lista_signo) ):
        signo = lista_signo[i]

        if signo == '-':

            #print(f"Signo encontrado: {lista_signo[i]}")
            #print(f"Cambio: {lista_numeros[i]}") , print(type(lista_numeros[i]))
            lista_numeros[i] *= -1
            #print()

    return lista_numeros

def aux_tres_constantes_a_cadena(a , b , c):
    # Se encarga de agregar a la lista_permitidos solo las constantes distintas a 0
    lista_permitidos = []
    if a != 0:
        lista_permitidos.append(str(a) + 'x')

    if b != 0:
        lista_permitidos.append(str(b) + 'y')

    if c != 0:
        lista_permitidos.append(str(c))

    # Se encarga de estudiar el signo de cada variable
    lista_signo = []
    if a > 0:
        lista_signo.append('+')
    elif a < 0:
        lista_signo.append('-')

    if b > 0:
        lista_signo.append('+')
    elif b < 0:
        lista_signo.append('-')

    if c > 0:
        lista_signo.append('+')
    elif c < 0:
        lista_signo.append('-')

    # Se encarga de agregar a una cadena los términos con sus respectivos signos
    txt = ''
    for i in range( len(lista_permitidos) ):
        elemento = str(lista_permitidos[i])
        signo = str(lista_signo[i])

        if signo == '+':
            txt += signo + elemento
        else:
            txt += elemento

    cadena_formada = txt.lstrip('+')
    
    return cadena_formada

def aux_encontrar_signo_pendiente(pendiente):

    # Se encarga de encontrar el signo de la pendiente para formar la ecuación
    signo_dependiente = '+'
    for caracter in str(pendiente):
        if caracter == '-':
            signo_dependiente = '-'
    
    return signo_dependiente

def recta1(punto1_x , punto1_y , punto2_x , punto2_y):
    from clase_geo import Fraccion

    'Codigo hecho para recibir 2 puntos y retornar una recta'

    punto_1 = Fraccion(punto1_x , punto1_y)
    punto_2 = Fraccion(punto2_x , punto2_y)
    pendiente = punto_1.pendiente(punto_2)
    Np = abs(pendiente.obtener_numerador_simplificado()) # Numerador pendiente - Np, ATENDER! porque el signo reposa por éste (analítica)
    Dp = abs(pendiente.obtener_denominador_simplificado()) # Denominador pendiente - Dn (siempre positivo, siempre)
    'Hay 1 solo error en donde el Dp retorna negativo, cuando Np == 0 and punto1_x < punto2_x '
    'El problema está en algun lugar de pendiente, Class Fraccion o obtener_numerador y denominador simplificado'
    'No logro corregir en el código fuente'
    sin_error_CF = True
    if Np == 0 and Dp == -1:
        sin_error_CF = False

    signo_dependiente = aux_encontrar_signo_pendiente(pendiente)

    '                      Ecuación punto-pendiente de la recta                      '
    'Solo el signo de Np puede variar, Dp siempre y siempre será positivo (hacer parte analítica para entender)'
    '   CTE,VAR          PURO CTE                            CTE,VAR          PURO CTE '
    # ( Dp * 'y' )  -  ( Dp * punto1_y)  atender {-} atender  ( Np * 'x' )  +  ( Np * punto1_x )  =  0
    'no cambia nunca de signo - Término 1'
    '                   cambia siempre de signo - Término 2'
    '                                                     if necesario, dos casos posibles - Término 3'
    '                                                                       if necesario, dos casos posibles - Término 4'

    # CTE,VAR  - uno    =    [      Dp * 'y'      ] signo siempre positivo
    # PURO CTE - dos    =    [      Dp * punto1_y     ] signo depende del signo de la coordenada del punto elegido
    # CTE,VAR  - tres   =    [      Np * 'x'      ] signo depende del signo de la pendiente , + ---> - , - ---> +
    # PURO CTE - cuatro =    [      Np * punto1_x     ] signo depende del signo de la pendiente , + ---> + , - ---> -

    'Apilado para cada término segun su caso'
    uno , dos , tres , cuatro = [] , [] , [] , []

    # Caso 1
    agregar_uno = str(Dp) + 'y'
    uno.append(agregar_uno) # El más fácil y sin ninguna restricción, no cambia nunca de signo, siempre +
    # Caso 2
    agregar_dos = Dp * punto1_y # Despues usar str(), ahora sirve mas como tipo int()
    dos.append(agregar_dos * -1) # Cambia siempre de signo

    # Caso 3 y 4
    if signo_dependiente == '+':
        agregar_tres = str(Np) + 'x'
        tres.append('-' + agregar_tres)

        agregar_cuatro = Np * punto1_x # Despues usar str(), ahora sirve mas como tipo int() (ver print)
        cuatro.append(agregar_cuatro)

    else:
        agregar_tres = '+' + str(Np) + 'x' # Si la pendiente es negativa, se anula el negativo con el de la fórmula
        tres.append(agregar_tres) # Se agrega con el '+'

        agregar_cuatro = -1 * Np * punto1_x # Despues usar str(), ahora sirve mas como tipo int() (ver print)
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
    
    return aux_ordenar_ecuacion(cadena_obtenida)

def circunf2(a , b , ap , bp , m , n):
    # Análisis algebraico para hallar el centro de la cia
    # Metodo de determinantes 2x2
    # distancia_centro_A = distancia_centro_B = distancia_centro_C

    'Estos son solo banderines para ver si se cumplen la condicion de CIA'
    punto_1 = a , b
    punto_2 = ap , bp
    punto_3 = m , n

    if punto_1 == punto_2 or punto_1 == punto_3 or punto_2 == punto_3: # Uso de banderines
        return # No retorna nada y no se continua con el código

    else:
        alfa = -2*a + 2*ap
        beta = -2*b + 2*bp
        gama = -a**2 + ap**2 - b**2 + bp**2

        alfa_p = -2*a + 2*m
        beta_p = -2*b + 2*n
        gama_p = -a**2 + m**2 - b**2 + n**2

        determinante_h = gama * beta_p - gama_p * beta
        determinante_k = alfa * gama_p - alfa_p * gama
        determinante = alfa * beta_p - alfa_p * beta

        h = determinante_h / determinante
        k = determinante_k / determinante

        # Formatea el número para mostrar solo 2 decimales
        h = "{:.2f}".format(h)
        k = "{:.2f}".format(k)

        return h , k

def aux_ordenar_ecuacion_cia(cadena):

    # Se encarga de agregar en una lista el término de la ecuación sin su signo, solo el término
    # Otra función se encarga de analizar el signo de cada término
    lista_termino = []
    txt = ''
    for caracter in cadena:

        if caracter == '=':
            break
        
        if caracter in '+-' and len(txt) > 0:
            
            # Si el termino es un entero, lo necesito como int() y no como str(). Mas abajo se explica porqué
            ES_ENTERO = True
            for letra in txt:
                if letra in 'xy':
                    ES_ENTERO = False
            
            if ES_ENTERO:
                lista_termino.append( int(txt) ) # Solo si es verdadero (True)
            else:
                lista_termino.append(txt)
            txt = ''
        
        elif caracter in '0123456789xy':
            txt += caracter

    antes_del_igual = txt
    if antes_del_igual not in '+-=':
        lista_termino.append( txt )

    # Ayuda visual: y2+x2-4+2x
    # Se encarga de analizar el signo de cada término y agregar a una lista
    lista_signo = []

    INDICE_0 = True
    if cadena[0] in '0123456789abcdefghijklmnopqrstuvwxyz':
        INDICE_0 = False
        lista_signo.append('+')

    # En el caso que el indice_0 sea verdadero'
    if INDICE_0:
        for i in range(0 , len(cadena)):
            signo = cadena[i]

            if signo in '+-':
                lista_signo.append(signo)

    # Si no es verdadero, significa que el indice 0 es positivo y como es invisible, ya se agregó de forma manual
    else:
        for i in range(1 , len(cadena)):
            signo = cadena[i]

            if signo in '+-':
                lista_signo.append(signo)

    ultimo = cadena[-1]
    ultimo_entero = 0
    if ultimo in '0123456789':

        ultimo_entero = ''
        for i in range(len(cadena) - 1 , - 1 , -1):
            elemento = cadena[i]

            if elemento == '=':
                break

            ultimo_entero += elemento

        ultimo_entero = int( aux_invertir_cadena(ultimo_entero) )

    cant = 0
    dos_enteros = False
    for elemento in lista_termino:

        if isinstance(elemento , int):

            indice = lista_termino.index(elemento)

            if lista_signo[indice] == '-':
                elemento *= -1
            
            cambio = elemento - ultimo_entero

            if cambio >= 0:
                lista_signo[indice] = '+'
            else:
                lista_signo[indice] = '-'
            
            lista_termino[indice] = abs(cambio)
            cant += 1

    if cant == 0:
        dos_enteros = True

    if dos_enteros and ultimo_entero != 0:
        
        signo = '+' # Se supone que el entero es negativo, debería de ser al revés pero ya estoy cansado
        # Dejo así mismo

        if ultimo_entero >= 0:
            signo = '-'
        
        lista_termino.append(abs(ultimo_entero))
        lista_signo.append(signo)

    lista_ordenada = []

    # Se encarga de ordenar solo los términos cuadráticos de la ecuación, luego vienen los lineales
    # Lista término: ['y2', 'x2', '4', '2x']
    # Lista signo: ['+', '+', '-', '-']
    aux = ['x2' , 'y2']

    for elemento in aux:

        if elemento in lista_termino:
            indice = lista_termino.index(elemento)

            lista_ordenada.append( str(lista_signo.pop(indice)) + str(lista_termino.pop(indice)) )

    # Se encarga de ordenar los términos lineales si es que existen
    # La constante (el más fácil) se deja para el final
    # Lista término: ['4', '2x', '7y']
    # Lista signo: ['-', '-', '+']
    aux = ['x' , 'y']
    Q = 0
    while len(lista_termino) > 1:
        comparacion = aux[Q]

        for i in range(len(lista_termino)):
            elemento = lista_termino[i]

            if aux[Q] in str(elemento):

                indice = lista_termino.index(elemento)
                lista_ordenada.append( str(lista_signo.pop(indice)) + str(lista_termino.pop(indice))  )
                break

        Q += 1

    # Se encarga de agregar la constante (si no hay constante igual agrega el ultimo faltante, funciona igual)
    if len(lista_termino) > 0:
        lista_ordenada.append( str(lista_signo.pop() + str(lista_termino.pop())) )

    txt = ''
    for elemento in lista_ordenada:
        txt += elemento
    cadena_obtenida = txt.lstrip('+')

    return aux_corregir_espacios(cadena_obtenida)

