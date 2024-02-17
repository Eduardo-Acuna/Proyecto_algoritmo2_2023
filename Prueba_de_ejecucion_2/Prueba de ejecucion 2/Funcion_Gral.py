"""   --- FUNCIONES PARA ORDENAR, SEPARAR Y OPERAR TERMINOS DE CUALQUIER TIPO DE ECUACIÓN (sin denominador) ---   """
def mcd(A , B):
    if A > B:
        A , B = B , A
    if A == B:
        MCD = 1
    else:
        for i in range(A , -1, -1):
            if A % i == 0 and B % i == 0:
                MCD = i
                break

    return(MCD)

def aux_invertir_cadena(cadena): # Invierte de orden una cadena (correcion de entero 726 --> 627)
    return cadena[::-1]

def aux_corregir_espacios(texto_a_espaciar): # Espacia la cadena para una mejor visualización

    # Se encarga de agrupar carácter por carácter la cadena en una lista
    caracter_caracter = []
    for letra in texto_a_espaciar:

        if letra == '=':
            break
        
        if letra in 'xy0123456789+-.':
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

def aux_corregir_espacios_float(texto_a_espaciar): # Espacia la cadena para una mejor visualización

    # Se encarga de agrupar carácter por carácter la cadena en una lista
    caracter_caracter = []
    for letra in texto_a_espaciar:

        if letra == '=':
            break
        
        if letra in 'xy0123456789+-.':
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

def aux_cambiar_variables_exponente(cadena): # Pone en mayúsculas las variables con exponentes 2 (x² , y²)
    # Nunca el primer miembro puede tener solo un término, por eso se agrega una CTE vacía
    if cadena[0] == '-':
        cadena = '@' + cadena
    else:
        cadena = '@+' + cadena

    cadena_sin_espacios = cadena.replace(" ", "").replace('²','2').replace('^2' , '2')
    variables = set()  # Usamos un conjunto para evitar duplicados

    for indice in range(len(cadena_sin_espacios)):
        actual = cadena_sin_espacios[indice]

        if actual == '2' and indice != 0:
            anterior = cadena_sin_espacios[indice - 1]

            if anterior.isalpha():
                agregar = anterior + actual
                variables.add(agregar.upper())  # Usamos "add" en lugar de "append" para un conjunto

    if variables:
        for variable in variables:
            cadena_sin_espacios = cadena_sin_espacios.replace(variable.lower(), variable.upper())
    #print(f"Prueba: {cadena_sin_espacios + '0'}")
    return cadena_sin_espacios + "@"

def aux_comprobacion_entero(cadena): # Comprueba si la cadena obtenida es un entero
    ES_ENTERO = True
    for letra in cadena:
        if letra in 'abcdefghijklmnopqrstuvwxyzXY': # NO PONER . (punto) AQUI, SUPER IMPORTANTE
            ES_ENTERO = False

    if ES_ENTERO:
        return True
    else:
        return False

def aux_true_false_lista(lista): # Devuelve True o False de un número si existe en la lista
    for elemento in lista:

        if isinstance(elemento, float or int):
            return True
    
    return False

def aux_indice_entero_lista(lista): # Devuelve el índice de los enteros CTE de la ecuación

    for i in range( len(lista) ):
        elemento = lista[i]

        if isinstance(elemento, float or int):
            return i
    
    return None

def aux_cambio_signo_miembro_2(lista): # Cambia todos los signos para traer al miembro 1
    
    for i in range( len(lista) ):
        signo_a_cambiar = lista[ i ]

        if signo_a_cambiar == '+':
            lista[ i ] = '-'
        else:
            lista[ i ] = '+'

    return lista

def aux_correcion_miembro_2(cadena): # Crea un segundo miembro si no los hay, si hay solo analiza

    # Segundo estudiamos la parte derecha de la =
    comprobacion = aux_terminos_miembro_2(cadena)
    if comprobacion is not None: # Falla si el usuario no escribió el segundo miembro
        miembro_2 = comprobacion
        signo_2 = aux_signo_miembro2(cadena)

    # Si el usuario no puso =, entonces se corrige ese error y continuamos con el código
    else:
        cadena += '=0'
        miembro_2 = aux_terminos_miembro_2(cadena)
        signo_2 = aux_signo_miembro2(cadena)
    
    return miembro_2 , signo_2

def aux_terminos_miembro_1(cadena): # Obtiene los términos del miembro 1

    if '=' in cadena:
        nueva_cadena = ''
        for letra in cadena:
            if letra in '=':
                break
            else:
                nueva_cadena += letra
        nueva_cadena += '@'
    
    else:
        nueva_cadena = cadena
    # Se encarga de agregar en una lista el término de la ecuación sin su signo, solo el término
    # Otra función se encarga de analizar el signo de cada término
    lista_termino = []
    txt = ''
    for caracter in nueva_cadena:

        if caracter == '=':
            break

        if caracter in '+-@' and len(txt) > 0:

            ES_ENTERO = aux_comprobacion_entero(txt)
            # Si el termino es un entero, lo necesito como float() y no como str(). Mas abajo se explica porqué
            if ES_ENTERO: # Solo si es verdadero (True)
                lista_termino.append( float(txt) )
                #print(f'Se ingresa elemento: {txt}\n')
            else:
                lista_termino.append(txt)
            txt = ''
        
        elif caracter in '0123456789abcdefghijklmnopqrstuvwxyzXY.':
            txt += caracter

    antes_del_igual = txt
    if antes_del_igual not in '+-=':
        lista_termino.append( txt )
    
    return lista_termino

def aux_terminos_miembro_2(cadena): # Obtiene los términos del miembro 2

        if '=' not in cadena:
            return
        
        nueva_cadena = ''
        indice = cadena.index('=')

        for i in range(indice , len(cadena)):
            nueva_cadena += cadena[i]

        nueva_cadena += '@'
        lista_termino = []
        txt = ''
        for caracter in nueva_cadena:
            
            if caracter in '+-@' and len(txt) > 0:
                
                ES_ENTERO = aux_comprobacion_entero(txt)
                # Si el termino es un entero, lo necesito como float() y no como str(). Mas abajo se explica porqué
                if ES_ENTERO: # Solo si es verdadero (True)
                    lista_termino.append( float(txt) )

                else:
                    lista_termino.append(txt)
                txt = ''
            
            elif caracter in '0123456789abcdefghijklmnopqrstuvwxyzXY.':
                txt += caracter
        
        return lista_termino

def aux_signo_miembro_1(cadena): # Obtiene los signos del miembro 1

    # Se encarga de analizar el signo de cada término y agregar a una lista
    lista_signo = []
    if cadena[0] in '0123456789abcdefghijklmnopqrstuvwxyzXY.':
        lista_signo.append('+')

        for i in range(1 , len(cadena)):
            signo = cadena[i]

            if signo == '=':
                break

            if signo in '+-':
                lista_signo.append(signo)

    else:

        for i in range(0 , len(cadena)):
            signo = cadena[i]

            if signo == '=':
                break

            if signo in '+-':
                lista_signo.append(signo)
    
    return lista_signo

def aux_signo_miembro2(cadena): # Obtiene los signos del miembro 2

    if aux_terminos_miembro_2(cadena) == None or len( aux_terminos_miembro_2(cadena) ) == 0:
        return None

    else:

        txt = ''
        indice = cadena.index('=')

        for i in range(indice , len(cadena)):
            caracter = cadena[i]
            txt += caracter
        nueva_cadena = txt.lstrip('=')

        # Se encarga de analizar el signo de cada término y agregar a una lista
        lista_signo = []
        #Dprint(f'Nueva cadena (proceso): {nueva_cadena}\n')
        if nueva_cadena[0] in '0123456789abcdefghijklmnopqrstuvwxyzXY.':
            lista_signo.append('+')

            for i in range(1 , len(nueva_cadena)):
                signo = nueva_cadena[i]

                if signo in '+-':
                    lista_signo.append(signo)

        else:

            for i in range(0 , len(nueva_cadena)):
                signo = nueva_cadena[i]

                if signo in '+-':
                    lista_signo.append(signo)
        
        return lista_signo

def aux_operando_x2(cadena): # Devuelve la constante de la variable x²
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'X':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_operando_y2(cadena): # Devuelve la constante de la variable y²
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'Y':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_operando_x(cadena): # Devuelve la constante de la variable x
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'x':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_operando_x_float(cadena): # Devuelve la constante de la variable x
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'x':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_operando_y(cadena): # Devuelve la constante de la variable y
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'y':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_operando_y_float(cadena): # Devuelve la constante de la variable y
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'y':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789.':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return float(constante)

def aux_existe_en_lista(lista , elemento): # Devuelve posision o -1 de un número

    for posicion in range( len(lista) ):
        buscado = lista[ posicion ]

        if elemento in str( buscado ):
            return posicion

    return -1

def aux_operacion_entre_miembros(cadena): # Opera términos semejantes 2 miembros

    # Creación de la parte izquierda de la ecuación
    reducir_miembro_1 , reducir_signo_1 = aux_terminos_miembro_1(cadena) , aux_signo_miembro_1(cadena)
    miembro_1 , signo_1 = aux_operacion_entre_terminos(reducir_miembro_1 , reducir_signo_1)  

    #print(f'Miembro 1 terminos: {miembro_1}')
    #print(f'Miembro 1 signos: {signo_1}\n')

    # Creación de la parte derecha de la ecuación
    reducir_miembro_2 , reducir_signo_2 = aux_correcion_miembro_2(cadena)
    miembro_2 , signo_2 = aux_operacion_entre_terminos(reducir_miembro_2 , reducir_signo_2) 

    #print(f'Miembro 2 terminos: {miembro_2}')
    #print(f'Miembro 2 signos: {signo_2}\n')

    terminos_orden , signos_orden = [] , []
    operandos = ['X2' , 'Y2' , 'x' , 'y']
    lista_de_funcion = [aux_operando_x2 , aux_operando_y2 , aux_operando_x , aux_operando_y]
    Q = 0

    while Q < len(operandos):
        referencia = operandos[Q] # 'x2'

        posicion_1 = aux_existe_en_lista(  miembro_1 , referencia  )
        posicion_2 = aux_existe_en_lista(  miembro_2 , referencia  )
        #print(f"Posicion 1: {posicion_1}")
        #print(f"Posicion 2: {posicion_2}\n")

        if posicion_1 != -1 and posicion_2 != -1:

            constante_1 = lista_de_funcion[ Q ]( miembro_1[ posicion_1 ] )
            constante_2 = lista_de_funcion[ Q ]( miembro_2[ posicion_2 ] )

            if signo_1[  posicion_1  ] == '-':
                constante_1 *= -1

            if signo_2[  posicion_2  ] == '-':
                constante_2 *= -1

            operacion = constante_1 - constante_2

            #print(f"constante_1: {constante_1}")
            #print(f"constante_2: {constante_2}")
            #print(f"Operacion: {operacion}\n")

            if operacion >= 0:
                signos_orden.append( '+' )
            else:
                signos_orden.append( '-' )

            miembro_1.pop(  posicion_1  )
            signo_1.pop(  posicion_1  )

            miembro_2.pop(  posicion_2  )
            signo_2.pop(  posicion_2  )

            if abs(operacion) > 1:
                terminos_orden.append(  str(abs(operacion)) + referencia  )
            
            elif abs(operacion) == 1:
                terminos_orden.append( str(abs(operacion)).lstrip("1.0") + referencia  )


        elif not posicion_1 or not posicion_2 : # Aqui ocurre un error cuando hay 1 solo término
            # en el miembro 1. Revisar caso
            # Error se corrige en la línea 35 en def aux_cambiar_variables_exponente(cadena):

            agregar_termino = miembro_1.pop(  posicion_1  )
            agregar_signo = signo_1.pop(  posicion_1  )

            terminos_orden.append( agregar_termino )
            signos_orden.append( agregar_signo )

        Q += 1

    # Se encarga de pasar todos los terminos que quedaron sin modifiacion (operando nulo)
    while len(miembro_1) != 0:

        terminos_orden.append( miembro_1.pop()  )
        signos_orden.append(  signo_1.pop() )

    # Se encarga de pasar solo las constantes del miembro 2 si es que existen
    while aux_true_false_lista(miembro_2): # Esta función devuelve True o False, por eso es obligarorio el...
        #...pop() de abajo. Porque va quitando los enteros que hacen posible el True, así se detendrá el while

        indice = aux_indice_entero_lista(miembro_2) # Esta función es igual que la anterio, pero en vez de devolver
        #print(f"\n\nIndice usado: {indice}\n\n")
        # True o False, retorna el indice del elemento en cuestión (entero)

        if signo_2[ indice ] == '+':
            signo_2[ indice ] = '-'
        else:
            signo_2[ indice ] = '+'

        terminos_orden.append( miembro_2.pop( indice ) )
        signos_orden.append( signo_2.pop( indice ) )

    #print(f'Terminos (proceso): {terminos_orden}')
    #print(f'Signos (proceso): {signos_orden}\n')

    # Importante ejecutar este codigo, despues de las CTE del miembro 2 para no tener errores
    while len(miembro_2) != 0:
        signo_2 = aux_cambio_signo_miembro_2(signo_2) # Antes de pasar, hay que cambiar de signo

        terminos_orden.append( miembro_2.pop()  )
        signos_orden.append(  signo_2.pop() )
    

    return terminos_orden , signos_orden

def aux_operacion_entre_terminos(terminos_orden , signos_orden): # Opera términos semejantes de 1 miembro

    operandos = ['X2' , 'Y2' , 'x' , 'y']
    lista_de_funcion = [aux_operando_x2 , aux_operando_y2 , aux_operando_x , aux_operando_y]
    Q = 0

    while Q < len( operandos ):
        referencia = operandos [ Q ]
        
        lista_semejantes = []
        signos_semejantes = []
        lista_indices = []
        recorrido = 0
        suma = 0

        cant = 0
        for indice in range( len(terminos_orden) ):
            elemento = terminos_orden[ indice ]

            if referencia in str(elemento):
                #print(f"Elemento: {elemento}") #, print(type(elemento))

                lista_semejantes.append( elemento )
                signos_semejantes.append( signos_orden[ indice ] )
                lista_indices.append( elemento )
                cant += 1
        
        if cant > 1:
            while recorrido < len((lista_semejantes)):
                #print(f"\nReferencia: {referencia}")
                #print(f"Lista indices: {lista_indices}")
                #print(f"Q: {Q}")
                #print(f'Lista semejantes: {lista_semejantes}')
                #print(f'Signos semejantes: {signos_semejantes}\n')



                if signos_semejantes[ recorrido ] == '-':
                    lista_semejantes[ recorrido ] = lista_de_funcion[ Q ]( lista_semejantes[ recorrido ] ) * -1
                else:
                    lista_semejantes[ recorrido ] = lista_de_funcion[ Q ]( lista_semejantes[ recorrido ] )

                #print(f"\nLista semejantes: {lista_semejantes}")
                #print(f"Signos semejantes: {signos_semejantes}")
                suma += lista_semejantes[ recorrido ]
                recorrido += 1

            # Se encarga de eliminar los terminos que se usaron para operarse
            for i in range( len(lista_indices )):
                buscar = lista_indices[i]

                eliminar = terminos_orden.index( buscar )

                terminos_orden.pop( eliminar )
                signos_orden.pop( eliminar )

            # Agrega de forma correcta el resultado y el signo correspondiente
            if suma > 1:
                terminos_orden.append( str( abs(suma) ) + referencia)
                signos_orden.append('+')
            elif suma == 1:
                terminos_orden.append(referencia)
                signos_orden.append('+')
            elif suma < 0:
                terminos_orden.append( str( abs(suma) ) + referencia)
                signos_orden.append('-')

            #print(f"\nSuma: {suma}\n")
            #print(f"Lista semejantes: {terminos_orden}")
            #print(f"Signos semejantes: {signos_orden}")

        Q += 1
    """----------------------------------------------------------------------------------------""" 
    # Se encarga solo de analizar las CTE del miembro resultado
    cte_lista , cte_signos , cte_indice = [] , [] , []
    #print(f'Terminos orden (proceso): {terminos_orden}\n')
    for i in range( len(terminos_orden) ):
        elemento = terminos_orden[ i ]

        if isinstance(elemento , float or int):
            #print(f'Elemento (proceso): {elemento}\n')
            cte_indice.append( elemento )
            cte_lista.append( elemento )
            cte_signos.append( signos_orden[ i ] )

    if len(cte_lista) > 0:

        # Se encarga de cambiar el signo de la constante en caso de ser necesario
        for k in range( len(cte_signos) ):
            elemento = cte_signos[ k ]
            buscar = cte_indice[ k ]
            eliminar = terminos_orden.index( buscar )

            if elemento == '-':
                cte_lista[ k ] *= -1

            terminos_orden.pop( eliminar )
            signos_orden.pop( eliminar )

        suma = 0
        for elemento in cte_lista:
            suma += elemento

        if suma != 0: # Importante que sea != 0 y no > 0 como estaba, causa errores
            #print(f"\nLa suma es: {suma}\n")
            terminos_orden.append( abs(suma) )
            #print(f"\nLa suma es: {suma}\n")
            if suma > 0:
                signos_orden.append('+')
            else:
                signos_orden.append('-')

    """----------------------------------------------------------------------------------------""" 
    #print(f"\nTerminos (proceso): {terminos_orden}")
    #print(f"Signos (proceso): {signos_orden}\n")
    return terminos_orden , signos_orden

def aux_arreglo_de_terminos_signos(terminos , signos):
    # Se encarga de ordenar la ecuación como la lista de arriba en caso de que se pueda
    terminos_arreglo , signos_arreglo = [] , []
    aux = ['X2' , 'x2' , 'y2' , 'Y2' , 'x' , 'y']
    recorrido = 0
    while recorrido < len(aux):

        referencia = aux[ recorrido ]

        for i in range( len(terminos) ):

            if referencia in str(terminos[i]) and str(terminos[i]) not in terminos_arreglo:
                terminos_arreglo.append( terminos[ i ] )
                signos_arreglo.append( signos[ i ])

        recorrido += 1

    # Agrega la constante en caso de existir como último
    for i in range( len(terminos) - 1 , -1 , -1  ): # Para ahorrar trabajo de cpu

        if isinstance(terminos[i] , float or int):
            #print(f'Terminos arreglo (p): {terminos_arreglo}')
            #print(f'Signos arreglo (p): {signos_arreglo}\n')

            #print(f'Terminos (p): {terminos}')
            #print(f'Signos (p): {signos}\n')
            terminos_arreglo.append( terminos[ i ] )
            signos_arreglo.append( signos[ i ] )
            #print(f'Terminos (p): {terminos}')
            #print(f'Signos (p): {signos}\n')
            

    if signos_arreglo[0] == '-':

        for i in range( len(signos_arreglo) ):

            if signos_arreglo[i] == '-':
                signos_arreglo[i] = '+'
            else:
                signos_arreglo[i] = '-'

    return terminos_arreglo , signos_arreglo

def aux_obtener_cadena_semi(terminos_orden , signos_orden):
    txt = ''
    k = 0
    while k < len(terminos_orden):

        txt += signos_orden[k] + str(terminos_orden[k])

        k += 1
    cadena_obtenida = txt.lstrip('+').lower()
    return cadena_obtenida

def aux_ordenar_ecuación_final(cadena): # Devuelve la ecuación ya corregida
    cadena = aux_cambiar_variables_exponente(cadena)
    a , b = aux_operacion_entre_miembros(cadena)
    terminos_orden , signos_orden = aux_arreglo_de_terminos_signos(a , b)
    cadena_obtenida = aux_obtener_cadena_semi(terminos_orden , signos_orden)

    return aux_corregir_espacios(cadena_obtenida).replace(' ' , '')

def aux_ordenar_ecuación_final_float(cadena): # Devuelve la ecuación ya corregida
    cadena = aux_cambiar_variables_exponente(cadena)
    semejantes_terminos , semejantes_signos = aux_operacion_entre_miembros(cadena)
    #print(f'Termino (semejantes_terminos): {semejantes_terminos}')
    #print(f'Signo (semejantes_signos): {b}\semejantes_signos')
    terminos_orden , signos_orden = aux_arreglo_de_terminos_signos(semejantes_terminos , semejantes_signos)
    cadena_obtenida = aux_obtener_cadena_semi(terminos_orden , signos_orden)    

    return aux_corregir_espacios_float(cadena_obtenida).replace(' ' , '')

"""   --- FUNCIONES PARA RECTAS ---   """

def aux_tres_constantes_a_cadena(a , b , c): # Devuelve cadena corregida, pide 3 parámetros
    # Se encarga de agregar a la lista_permitidos solo las constantes distintas a 0
    lista_permitidos = []
    if a != 0:

        if a == 1:
            lista_permitidos.append('x')
        elif a == -1:
            lista_permitidos.append('-x')
        else:
            lista_permitidos.append(str(a) + 'x')

    if b != 0:

        if b == 1:
            lista_permitidos.append('y')
        elif b == -1:
            lista_permitidos.append('-y')
        else:
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

def aux_ordenar_ecuacion(cadena):

    cadena = aux_corregir_espacios(cadena) # Super importante este llamado!!!
    # Se encarga de agregar cada término y el signo en una lista auxiliar
    diccionario = "abcdefghijklmnopqrstuvwxyz0123456789+-."
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
            if caracter in '0123456789.':
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
                    lista_numeros.append(float( aux_invertir_cadena(txt) )) # Si en if de arriba, pueden haber errores
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

        if letra in '0123456789.':
            txt += letra

    if len(txt) != 0:
        lista_numeros.append( float( aux_invertir_cadena(txt) ) )
    else:
        lista_numeros.append(0)

    return lista_numeros , lista_variables

def aux_encontrar_constantes_recta(cadena): # Devuelve las constantes A, B y C
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

            if letra in '0123456789.':
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
    lista_numeros

    return lista_numeros

def aux_encontrar_signo_pendiente(pendiente): # Devuelve signo de pendiente

    # Se encarga de encontrar el signo de la pendiente para formar la ecuación
    signo_dependiente = '+'
    for caracter in str(pendiente):
        if caracter == '-':
            signo_dependiente = '-'
    
    return signo_dependiente

def Recta1(punto1_x , punto1_y , punto2_x , punto2_y): # Devuelve cadena corregida
    from clase_geo_Gral import Fraccion

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
    agregar_dos = Dp * punto1_y # Despues usar str(), ahora sirve mas como tipo float()
    dos.append(agregar_dos * -1) # Cambia siempre de signo

    # Caso 3 y 4
    if signo_dependiente == '+':
        agregar_tres = str(Np) + 'x'
        tres.append('-' + agregar_tres)

        agregar_cuatro = Np * punto1_x # Despues usar str(), ahora sirve mas como tipo float() (ver print)
        cuatro.append(agregar_cuatro)

    else:
        agregar_tres = '+' + str(Np) + 'x' # Si la pendiente es negativa, se anula el negativo con el de la fórmula
        tres.append(agregar_tres) # Se agrega con el '+'

        agregar_cuatro = -1 * Np * punto1_x # Despues usar str(), ahora sirve mas como tipo float() (ver print)
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

                if float(txt_entero) == 0:
                    BANDERA = False
                    break # Esto detiene el while True

                elif float(txt_entero) > 1:
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

def Recta2(a , b , mx , my):

    def para_variable_y(my):
        # Primer término - VARIABLE y
        uno , signo_uno = f"{ str( abs(my) ) + 'y'  }" , '+'

        return uno , signo_uno

    def para_variable_CTE1(my , b) :
        # Segundo término - CONSTANTE

        if b >= 0:
            signo_b = '+'
        else:
            signo_b = '-'

        if signo_b == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
            dos , signo_dos = (my * b) * -1 , '-'
        else:
            dos , signo_dos = abs(my * b) , '+'
        
        return dos , signo_dos

    def para_variable_x(mx):

        # Tercer término - VARIABLE x
        if signo_pendiente == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
            tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '-'
        else:
            tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '+'

        return tres , signo_tres

    def para_variable_CTE2(a , mx , signo_pendiente):
        # Cuarto término - CONSTANTE
        if mx * a >= 0:
            cuatro , signo_cuatro = abs(mx * a) , '+'
        else:
            cuatro , signo_cuatro = mx * a , '-'
        
        return cuatro , signo_cuatro

    def obtener_terminos_y_signos(uno , dos , tres , cuatro , signo_uno , signo_tres):
        terminos , signos = [] , []

        'Las siguientes funciones analizan solo la parte entera de una variable'

        if aux_operando_x_float(tres) != 0: # Si el entero de x (tres) no es 0, entonces se agrega a la lista
            terminos.append(tres)
            signos.append(signo_tres)

        if aux_operando_y_float(uno) != 0: # Si el entero de y (uno) no es 0, entonces se agrega a la lista
            terminos.append(uno)
            signos.append(signo_uno)

        if dos + cuatro != 0:
            terminos.append( abs(dos + cuatro) )

            if dos + cuatro > 0:
                signos.append('+')
            else:
                signos.append('-')

        return terminos , signos

    def obtener_cadena(terminos , signos):

        # Se encarga de encontrar la ecuación formada, ordenada pero sin espacios. Otra función hace eso
        cadena = ''
        for i in range( len(terminos) ):
            cadena += str(signos[ i ]) + str(terminos[ i ])

        return cadena

    SI_EXISTE_MX , SI_EXISTE_MY = False , False

    if mx != 0:
        SI_EXISTE_MX = True
    if my != 0:
        SI_EXISTE_MY = True

    # Sin estos if, la ecuación será incorrecta
    if mx < 0 and my > 0:
        mx *= -1 # Obligatorio
    
    elif mx > 0 and my < 0:
        my *= -1 # Obligatorio
    
    elif mx < 0 and my < 0:
        mx *= -1 # Podrías ser también aplicado para my
    
    elif mx > 0 and my > 0:
        mx *= -1 # Podrías ser también aplicado para my

    if SI_EXISTE_MX and SI_EXISTE_MY:

        signo_pendiente = recta_signo_pendiente(mx , my)

        uno , signo_uno = para_variable_y(my)

        dos , signo_dos = para_variable_CTE1(my , b)

        tres , signo_tres = para_variable_x(mx)

        cuatro , signo_cuatro = para_variable_CTE2(a , mx , signo_pendiente)

        terminos , signos = obtener_terminos_y_signos(uno , dos , tres , cuatro , signo_uno , signo_tres)

        cadena = obtener_cadena(terminos , signos)

        
    elif SI_EXISTE_MX and not SI_EXISTE_MY:
        
        if a >= 0:
            cadena = f'x-{a}=0'
        else:
            cadena = f'x+{ abs(a) }=0'
    
    elif not SI_EXISTE_MX and SI_EXISTE_MY:

        if b >= 0:
            cadena = f'y-{b}=0'
        else:
            cadena = f'y+{b}=0'
            #print(f'b (proceso): {b}')
    
    elif not SI_EXISTE_MX and not SI_EXISTE_MY:

        cadena = None

    #print(f'(proceso) a: {a} , b: {b}\n')
    return aux_ordenar_ecuación_final_float(cadena)

def recta_signo_pendiente(nx , ny): # Devuelve el signo de la pendiente A / B
    if nx * ny > 0:
        signo_pendiente = '+'
    elif nx * ny < 0:
        signo_pendiente = '-'
    elif nx * ny == 0:
        signo_pendiente = '+'
    
    return signo_pendiente

def encontrar_terminos_recta(a , b , nx , ny , signo_pendiente):

    if b >= 0:
        signo_b = '+'
    else:
        signo_b = '-'

    # Primer término - VARIABLE y
    uno , signo_uno = f"{ str( abs(ny) ) + 'y'  }" , '+'

    # Segundo término - CONSTANTE
    if signo_b == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
        dos = (ny * b) * -1
    else:
        dos = abs(ny * b)

    # Tercer término - VARIABLE x
    if signo_pendiente == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
        tres , signo_tres = f"{ str( abs(nx) ) + 'x' }" , '-'
    else:
        tres , signo_tres = f"{ str( abs(nx) ) + 'x' }" , '+'

    # Cuarto término - CONSTANTE
    cuatro = nx * a

    terminos , signos = [] , []

    if aux_operando_x_float(tres) != 0: # Si el entero de x (tres) no es 0, entonces se agrega a la lista
        terminos.append(tres)
        signos.append(signo_tres)

    if aux_operando_y_float(uno) != 0: # Si el entero de y (uno) no es 0, entonces se agrega a la lista
        terminos.append(uno)
        signos.append(signo_uno)

    if dos + cuatro != 0:
        terminos.append( abs(dos + cuatro) )

        if dos + cuatro > 0:
            signos.append('+')
        else:
            signos.append('-')

    return terminos , signos

def Distancia_recta(a , b , cadena): # Devuelve valor numérico
    from clase_geo_Gral import Recta

    recta = Recta(cadena)
    A , B , C = recta.encontrar_constantes()

    comprobacion = A*a + B*b + C

    if comprobacion != 0:
        distancia = abs(comprobacion) / (A**2 + B**2)**0.5

        return distancia

    else:

        return comprobacion

def Paralela(cadena , a , b):

    A , B , C = aux_encontrar_constantes_recta( aux_ordenar_ecuación_final(cadena)  )

    mx , my = A , B

    if mx != 0 and my != 0:
        cadena = Recta2(a , b , mx , my)

    elif mx != 0 and my == 0: # my = 0
        if a >= 0:
            cadena = f'x-{a}=0'
        else:
            cadena = f'x+{ abs(a) }=0'
    
    elif mx == 0 and my != 0: # mx = 0
        if b >= 0:
            cadena = f'y-{b}=0'
        else:
            cadena = f'y+{ abs(b) }=0'
    
    elif mx == 0 and my == 0:

        cadena = None
    
    return aux_ordenar_ecuación_final_float(cadena)

def Perpendicular(cadena , a , b):

    A , B , C = aux_encontrar_constantes_recta( aux_ordenar_ecuación_final(cadena)  )
    #print(f'A: {A} , B: {B}\n')

    mx , my = -B , A # Si el B no tiene el menos, no funciona. Super importante

    return Recta2(a , b , mx , my)

"""   --- FUNCIONES PARA CIRCUNFERENCIAS ---   """

def Circunf2(a , b , ap , bp , m , n): # Devuelve centro h, k
    from clase_geo_Gral import Punto

    """ Muy importante que la funcion Circunf1 del final le llame a la función
    aux_corregir_espacios_float() y no a aux_corregir_espacios() porque el usuario no va a ingresar puntos
    que necesariamente me dé una ecuación de constantes enteras, por eso en ejercios en donde la cadena depende de
    puntos hay que llamar al de tipo float() si o si """

    punto_1 = a , b
    punto_2 = ap , bp
    punto_3 = m , n

    if punto_1 == punto_2 or punto_1 == punto_3 or punto_2 == punto_3:
        return None , None , None

    else:

        # Análisis algebraico para hallar el centro de la cia
        # Metodo de determinantes 2x2
        # distancia_centro_A = distancia_centro_B = distancia_centro_C

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

        #"Puntos: ({a} , {b}) , ({ap} , {bp}) , ({m} , {n})")
        print(f'h: {h} , k: {k}')
        #

        primero = Punto(a , b)
        segundo = Punto(h , k)

        #print(f"Punto1: {primero}")
        #print(f"Punto2: {segundo}")

        r = primero.distancia_punto(segundo)

        return Circunf1(h , k , round(r , 3))

def cia_encontrar_hkr_cadena(cadena): # Devuelve puntos h, k y r
    terminos_lista , signos_lista = aux_terminos_miembro_1(cadena) , aux_signo_miembro_1(cadena)
    # Se encarga de encontrar los valores a y b de la ecuación de la circunferencia
    #print(terminos_lista)
    #print(signos_lista)

    a , b = 0 , 0 # En caso de que no existan sus variables, entonces se quedan en 0
    for i in range( len(terminos_lista) ):
        elementos = terminos_lista[ i ]

        if 'x' in str(elementos) and 'x2' not in str(elementos):

            if signos_lista[ i ] == '-':
                a = aux_operando_x(elementos) * -1
            else:
                a = aux_operando_x(elementos)
        
        if 'y' in str(elementos) and 'y2' not in str(elementos):

            if signos_lista[ i ] == '-':
                b = aux_operando_x(elementos) * -1
            else:
                b = aux_operando_x(elementos)

    ultimo = terminos_lista[ -1 ]
    if isinstance( ultimo , float or int):

        if signos_lista[ -1 ] == '-':
            c = ultimo * -1
        else:
            c = ultimo

    else:

        if 'x' in terminos_lista[ -1 ] or 'y' in terminos_lista[ -1 ]:
            c = 0
        else:

            if signos_lista[ -1 ] == '+':
                c = float(ultimo)
            else:
                c = float(ultimo) * -1

    radio = 0.5 * (a**2 + b**2 - 4*c) ** 0.5

    #print(f'a: {a}')
    #print(f'b: {b}')
    #print(f'c: {c}')

    h , k = a / (-2) , b / (-2) # Coordenadas del centro de la cia

    if h == 0:
        h = abs(h)

    if k == 0:
        k = abs(k)

    return h , k , radio

def Circunf1(h , k , r): # Devuelve cadena corregida

    # Se encarga de agregar las constantes y sus signos en diferentes listas
    a , b , c = -2*h , -2*k , h**2 + k**2 - r**2

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

    #print(f'Términos (proceso): {terminos}')

    #c *= -1
    # Se encarga de pasar a cadena los términos ya trabajados
    txt = ''
    for elementos in terminos:
        txt += str(elementos)

    # Cadena final sin espacios y ordenada
    cadena = 'x2+y2' + txt

    return aux_corregir_espacios_float(cadena)

def cia_encontrar_constantes_DEF(cadena): # Devuelve constantes Dx , Ey , F

    h , k , r = cia_encontrar_hkr_cadena( aux_ordenar_ecuación_final(cadena) )

    D , E , F = float(-2*h) , float(-2*k) , float(h**2 + k**2 - r**2)

    return D , E , F

"""   --- FUNCIONES PARA PARABOLA ---   """

def Foco_parabola(cadena): # Devuelve h , k , p , fx , fy , bandera
    'ax² + by² + cx + dy + e = 0 Cónicas en general'

    def para_A_B( terminos_lista , signos_lista):

        terminos_lista = cuadraticos_a_mayusculas(terminos_lista) # Sin este no funciona nada, atender
        a , b = 0 , 0

        for i in range( len(terminos_lista) ):
            elementos = terminos_lista[ i ]

            if 'X2' in str(elementos):

                if signos_lista[ i ] == '-':
                    a = aux_operando_x2(elementos) * -1
                else:
                    a = aux_operando_x2(elementos)
            
            if 'Y2' in str(elementos):

                if signos_lista[ i ] == '-':
                    b = aux_operando_y2(elementos) * -1
                else:
                    b = aux_operando_y2(elementos)

        return a , b

    def para_C_D(terminos_lista , signos_lista):
        
        c , d = 0 , 0

        # Se encarga de encontrar los valores de los coeficientes de x e y
        for i in range( len(terminos_lista) ):
            elementos = terminos_lista[ i ]

            if 'x' in str(elementos) and 'x2' not in str(elementos):

                if signos_lista[ i ] == '-':
                    c = aux_operando_x(elementos) * -1
                else:
                    c = aux_operando_x(elementos)
            
            if 'y' in str(elementos) and 'y2' not in str(elementos):

                if signos_lista[ i ] == '-':
                    d = aux_operando_y(elementos) * -1
                else:
                    d = aux_operando_y(elementos)

        return c , d

    def para_E(terminos_lista , signos_lista):
        e = 0

        ultimo = terminos_lista[ -1 ]
        if isinstance( ultimo , float or int):

            if signos_lista[ -1 ] == '-':
                e = ultimo * -1
            else:
                e = ultimo

        else:

            if 'x' in terminos_lista[ -1 ] or 'y' in terminos_lista[ -1 ]:
                e = 0
            else:

                if signos_lista[ -1 ] == '+':
                    e = float(ultimo)
                else:
                    e = float(ultimo) * -1
        
        return e

    def cuadraticos_a_mayusculas(terminos_lista):

        for i in range( len(terminos_lista) ):
            elemento = terminos_lista[ i ]

            if isinstance(elemento , str):

                if 'x2' in elemento:
                    terminos_lista[ i ] = terminos_lista[ i ].upper()
                
                elif 'y2' in elemento:
                    terminos_lista[ i ] = terminos_lista[ i ].upper()
        
        return terminos_lista

    def banderin_x2(terminos_lista):

        for elemento in terminos_lista:
            
            if 'X2' in str(elemento).upper():
                return True

        return False

    def banderin_y2(terminos_lista):

        for elemento in terminos_lista:
            
            if 'Y2' in str(elemento).upper():
                return True
        
        return False

    cadena = aux_ordenar_ecuación_final(cadena)
    terminos_lista = aux_terminos_miembro_1(cadena)
    signos_lista = aux_signo_miembro_1(cadena)

    a , b = para_A_B(terminos_lista , signos_lista)
    c , d = para_C_D(terminos_lista , signos_lista)
    e = para_E(terminos_lista , signos_lista)

    ES_X2 = banderin_x2(terminos_lista)
    ES_Y2 = banderin_y2(terminos_lista)

    #print(f'Terminos (proceso): {terminos_lista}\n')
    #print(f'a - x²  : {a}')
    #print(f'b - y²  : {b}')
    #print(f'c - x   : {c}')
    #print(f'd - y   : {d}')
    #print(f'e - cte : {e}\n')

    if b == 0: # Para (x - h)² = 4p(y - k)
        h = -c / (2*a)
        p = -d / (4*a)
        k = ( (4*a*e - (c**2)) / (4*a*d) )*-1
        
        if p > 0:
            
            #if ES_X2:
            fx , fy = h , k + p
            #elif ES_Y2:
                #fx , fy = h + p , k

        else:

            #if ES_X2:
            fx , fy = h , k - abs(p) # Por si k es negativo para que no se sume en la resta
            #elif ES_Y2:
                #fx , fy = h - abs(p) , k # Por si h es negativo para que no se sume en la resta


        #print(f'Proceso: {  (e - a*(h**2)) / (4*a*k)  }')

    elif a == 0: # Para (y - k)² = 4p(x - h)

        k = -d / (2*b)
        p = ( c / (4*b))*-1
        h = ( (4*b*e - (d**2)) / (4*c*b) )*-1
        
        if p > 0:
            fx , fy = h + p , k
        else:
            fx , fy = h - abs(p) , k

    if ES_X2:
        return round(h , 7) , round(k , 7) , p*2 , fx , fy , 'x2'
    
    elif ES_Y2:
        return round(h , 7) , round(k , 7) , p*2 , fx , fy , 'y2'

"""   --- INTERSECCIONES ---   """

def interseccion_recta_recta(cadena1 , cadena2):
    from clase_geo_Gral import Recta
    objeto1 = Recta(cadena1)
    objeto2 = Recta(cadena2)

    if cadena1 != cadena2:

        a , b , c = objeto1.encontrar_constantes()
        ap , bp , cp = objeto2.encontrar_constantes()

        determinante = a*bp - ap*b
        determinante_x = cp*b - c*bp
        determinante_y = ap*c - a*cp

        x1 , x2 = (determinante_x / determinante) , (determinante_y / determinante)

        return x1 , x2

    else:
        return 0 , 0

def interseccion_recta_cia(recta , cia): # Devuelve puntos de intersección
    from clase_geo_Gral import SegundoGrado

    a , b , c = aux_encontrar_constantes_recta(recta)
    D , E , F = cia_encontrar_constantes_DEF(cia)

    if a != 0:
        primero = a**2 + b**2
        segundo = 2*b*c - a*b*D + (a**2)*E
        tercero = c**2 - a*c*D + (a**2)*F

        ecuacion_cuadratica = SegundoGrado(primero , segundo , tercero)
        paray1 , paray2 = ecuacion_cuadratica.hallar_raices()
        y1 , y2 = round(paray1 , 2) , round(paray2 , 2)

        parax1 , parax2 = (-b*paray1 - c) / a , (-b*paray2 - c) / a
        x1 , x2 = round(parax1 , 2) , round(parax2 , 2)

        return x1 , y1 , x2 , y2

    else:

        primero = b**2
        segundo = (b**2)*D
        tercero = c**2 - b*c*E + (b**2)*F

        #print(f"Primero (proceso): {primero}")
        #print(f"Segundo(proceso): {segundo}")
        #print(f"Tercero (proceso): {tercero}")

        ecuacion_cuadratica = SegundoGrado(primero , segundo , tercero)
        parax1 , parax2 = ecuacion_cuadratica.hallar_raices()
        x1 , x2 = round(parax1 , 2) , round(parax2 , 2)

        y1 , y2 = -c / b , -c / b # Son iguales, misma altura

        return x1 , y1 , x2 , y2


