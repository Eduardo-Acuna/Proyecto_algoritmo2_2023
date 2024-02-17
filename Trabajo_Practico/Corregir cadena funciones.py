def terminos_en_lista_auxiliar(cadena):
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
    
    return aux

def agrupacion_de_terminos(cadena):

    aux = terminos_en_lista_auxiliar(cadena)

    # Se encarga de agrupar cada término con el signo que le corresponde
    terminos = []
    if aux[0] not in '+-':
        terminos.append(aux[0])
    for i in range(1 , len(aux) ):

        elemento = aux[i]
        correcion = aux[i - 1] + aux[i] 

        if elemento not in '+-' and correcion not in terminos:
            terminos.append(correcion)
    
    return terminos

def tres_listas_auxiliares(cadena):
 
    terminos = agrupacion_de_terminos(cadena)

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

    return lista_x , lista_y , lista_cte

def ordenar_cadena(cadena):

    lista_x , lista_y , lista_cte = tres_listas_auxiliares(cadena)

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

    return cadena_aux

# def ordenar_constantes(cadena) = def ordenar_cadena(cadena) + def tres_listas_auxiliares(cadena) \
# + def agrupacion_de_terminos(cadena) + def terminos_en_lista_auxiliar(cadena)

""" OBS: Todas estas funciones fueron copiadas y pegadas dentro de una sola funcion en funcion_geo
La función resultante se llama def ordenar_ecuación(cadena)
Pero es de aquí de donde salió toda la lógica de programación """