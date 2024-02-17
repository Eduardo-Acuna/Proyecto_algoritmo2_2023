"""   --- FUNCIONES PARA ORDENAR, SEPARAR Y OPERAR TERMINOS DE CUALQUIER TIPO DE ECUACIÓN ---   """

def aux_invertir_cadena(cadena):
    return cadena[::-1]

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

def aux_cambiar_variables_exponente(cadena):
    cadena_sin_espacios = cadena.replace(" ", "")
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

    return cadena_sin_espacios + "@"

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

def aux_comprobacion_entero(cadena):
    ES_ENTERO = True
    for letra in cadena:
        if letra in 'abcdefghijklmnopqrstuvwxyzXY':
            ES_ENTERO = False
    
    if ES_ENTERO:
        return True
    else:
        return False

def aux_true_false_lista(lista):
    for elemento in lista:

        if isinstance(elemento, int):
            return True
    
    return False

def aux_indice_entero_lista(lista):

    for i in range( len(lista) ):
        elemento = lista[i]

        if isinstance(elemento, int):
            return i
    
    return None

def aux_cambio_signo_miembro_2(lista):
    
    for i in range( len(lista) ):
        signo_a_cambiar = lista[ i ]

        if signo_a_cambiar == '+':
            lista[ i ] = '-'
        else:
            lista[ i ] = '+'

    return lista

def aux_correcion_miembro_2(cadena):

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

def aux_terminos_miembro_1(cadena):

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
            # Si el termino es un entero, lo necesito como int() y no como str(). Mas abajo se explica porqué
            if ES_ENTERO: # Solo si es verdadero (True)
                lista_termino.append( int(txt) )
            else:
                lista_termino.append(txt)
            txt = ''
        
        elif caracter in '0123456789abcdefghijklmnopqrstuvwxyzXY':
            txt += caracter

    antes_del_igual = txt
    if antes_del_igual not in '+-=':
        lista_termino.append( txt )
    
    return lista_termino

def aux_terminos_miembro_2(cadena):

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
                # Si el termino es un entero, lo necesito como int() y no como str(). Mas abajo se explica porqué
                if ES_ENTERO: # Solo si es verdadero (True)
                    lista_termino.append( int(txt) )
                else:
                    lista_termino.append(txt)
                txt = ''
            
            elif caracter in '0123456789abcdefghijklmnopqrstuvwxyzXY':
                txt += caracter
        
        return lista_termino

def aux_signo_miembro_1(cadena):

    # Se encarga de analizar el signo de cada término y agregar a una lista
    lista_signo = []
    if cadena[0] in '0123456789abcdefghijklmnopqrstuvwxyzXY':
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

def aux_signo_miembro2(cadena):

    if aux_terminos_miembro_2(cadena) == None or len( aux_terminos_miembro_2(cadena) ) == 0:
        return

    else:

        txt = ''
        indice = cadena.index('=')

        for i in range(indice , len(cadena)):
            caracter = cadena[i]
            txt += caracter
        nueva_cadena = txt.lstrip('=')

        # Se encarga de analizar el signo de cada término y agregar a una lista
        lista_signo = []
        if nueva_cadena[0] in '0123456789abcdefghijklmnopqrstuvwxyzXY':
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

def aux_operando_x2(cadena):
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'X':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return int(constante)

def aux_operando_y2(cadena):
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'Y':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return int(constante)

def aux_operando_x(cadena):
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'x':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return int(constante)

def aux_operando_y(cadena):
    constante = ''

    # Itera a través de los caracteres de la cadena
    EXISTE_VARIABLE = False
    for caracter in cadena:
        if caracter in 'y':

            EXISTE_VARIABLE = True
            break
            # Si se encuentra un signo, se detiene la extracción

        elif caracter in '0123456789':
            constante += caracter

    # Si no se encontró ninguna constante, establece un valor predeterminado
    if EXISTE_VARIABLE and not constante:
        constante = '1'
    
    return int(constante)

def aux_existe_en_lista(lista , elemento):

    for posicion in range( len(lista) ):
        buscado = lista[ posicion ]

        if elemento in str( buscado ):
            return posicion

    return -1

def aux_operacion_entre_miembros(cadena):

    # Creación de la parte izquierda de la ecuación
    miembro_1 , signo_1 = aux_terminos_miembro_1(cadena) , aux_signo_miembro_1(cadena)

    # Creación de la parte derecha de la ecuación
    miembro_2 , signo_2 = aux_correcion_miembro_2(cadena)

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
            #print(f"operacion: {operacion}\n")

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
                terminos_orden.append( str(abs(operacion)).lstrip("1") + referencia  )


        elif not posicion_1 or not posicion_2 :

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

    # Importante ejecutar este codigo, despues de las CTE del miembro 2 para no tener errores
    while len(miembro_2) != 0:
        signo_2 = aux_cambio_signo_miembro_2(signo_2) # Antes de pasar, hay que cambiar de signo

        terminos_orden.append( miembro_2.pop()  )
        signos_orden.append(  signo_2.pop() )
    
    a , b = aux_operacion_entre_terminos(terminos_orden , signos_orden) 
    return a , b

def aux_operacion_entre_terminos(terminos_orden , signos_orden):

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
    for i in range( len(terminos_orden) ):
        elemento = terminos_orden[ i ]

        if isinstance(elemento , int):
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

    return terminos_orden , signos_orden

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
    terminos_orden , signos_orden = aux_operacion_entre_miembros(cadena)
    cadena_obtenida = aux_obtener_cadena_semi(terminos_orden , signos_orden)

    return aux_corregir_espacios(cadena_obtenida)

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

def recta_signo_pendiente(mx , my):
    if mx * my > 0:
        signo_pendiente = '+'
    elif mx * my < 0:
        signo_pendiente = '-'
    elif mx * my == 0:
        signo_pendiente = '+'
    
    return signo_pendiente

"""   --- FUNCIONES PARA CIRCUNFERENCIAS ---   """

def cia_encontrar_hk_3_puntos(a , b , ap , bp , m , n): # Devuelve centro h, k

    punto_1 = a , b
    punto_2 = ap , bp
    punto_3 = m , n

    if punto_1 == punto_2 or punto_1 == punto_3 or punto_2 == punto_3:
        print(f"Error al elegir los puntos\
            \nNo se puede formar la circunferencia")

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
        #"h: {h} , k: {k}")
        #

        return h , k

def cia_encontrar_hk_cadena(cadena): # Devuelve puntos h, k y r
    terminos_lista , signos_lista = aux_terminos_miembro_1(cadena) , aux_signo_miembro_1(cadena)
    # Se encarga de encontrar los valores a y b de la ecuación de la circunferencia
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
    if isinstance( ultimo , int):

        if signos_lista[ -1 ] == '-':
            c = ultimo * -1
        else:
            c = ultimo

    else:

        if 'x' in terminos_lista[ -1 ] or 'y' in terminos_lista[ -1 ]:
            c = 0
        else:

            if signos_lista[ -1 ] == '+':
                c = int(ultimo)
            else:
                c = int(ultimo) * -1

    radio = 0.5 * (a**2 + b**2 - 4*c) ** 0.5

    h , k = a / (-2) , b / (-2) # Coordenadas del centro de la

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

    #c *= -1
    # Se encarga de pasar a cadena los términos ya trabajados
    txt = ''
    for elementos in terminos:
        txt += str(elementos)

    # Cadena final sin espacios y ordenada
    cadena = 'x2+y2' + txt

    return aux_corregir_espacios(cadena)



def encontrar_terminos_recta(a , b , mx , my , signo_pendiente):

    if b >= 0:
        signo_b = '+'
    else:
        signo_b = '-'

    # Primer término - VARIABLE y
    uno , signo_uno = f"{ str( abs(my) ) + 'y'  }" , '+'

    # Segundo término - CONSTANTE
    if signo_b == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
        dos = (my * b) * -1
    else:
        dos = abs(my * b)

    # Tercer término - VARIABLE x
    if signo_pendiente == '+': # Tiene que cambiar porque antes le opera un signo - de la fórmula punto-pendiente
        tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '-'
    else:
        tres , signo_tres = f"{ str( abs(mx) ) + 'x' }" , '+'

    # Cuarto término - CONSTANTE
    if mx * a >= 0:
        cuatro = abs(mx * a)
    else:
        cuatro = mx * a

    terminos , signos = [] , []

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

    return terminos , signos