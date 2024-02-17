from clase_geo import*

def invertir_cadena(cadena):
    return cadena[::-1]

def _encontrar_constantes(cadena):
    # Se encarga de encontrar las constantes de la ecuación en el orden Ax, By
    orden_constantes = ["x" , "y"]
    lista_numeros = []
    lista_variables = []
    k = 0
    while k < 2:
        variable_a_buscar = orden_constantes[k]
        indice = cadena.find( variable_a_buscar )

        if indice != -1:

            if indice > 0:

                txt = ''
                for i in range(indice - 1 , -1 , -1):
                    letra = cadena[i]
        # NO SE BUSCAN LOS SIGNOS AUN, PARA ELLO HAY OTRA FUNCION QUE SE ENCARGA DE ELLO
        # Por eso se pone un break en caso de que letra pertenezca a '+-'
                    if letra in '+-':
                        break
                    else:
                        txt += letra            
                lista_numeros.append(int( invertir_cadena(txt) ))
            else:
                lista_numeros.append(1)
        
        else:
            lista_numeros.append(0)    
        lista_variables.append(variable_a_buscar)

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
        lista_numeros.append( int( invertir_cadena(txt) ) )
    else:
        lista_numeros.append(0)
    
    #print(f"Lista de números: {lista_numeros}")
    #print(f"Lista variables: {lista_variables}")

    return lista_numeros , lista_variables

def encontrar_constantes(cadena):
# Realmente se encarga de encontrar los signos de las constantes y corregirlos con la funcion anterior
# solo de ser necesario, pero para que el usuario entienda mejor, se pone como nombre 'encontrar_constantes'

    lista_numeros , lista_signo = _encontrar_constantes(cadena)

# Se encarga de encontrar los signos de todas las constantes en el orden A, B, C

    lista_signo = []
    Q = 0
    aux = ['x' , 'y' , '=']
    while Q < len(lista_numeros):

        indice = cadena.find( aux[Q] )

        if Q == 0:

            if indice == 0:
                lista_signo.append('+')
            
            else:

                POSITIVO = True
                for i in range(indice , -1 , -1):
                    letra = cadena[i]

                    if letra == '-':
                        POSITIVO = False
                        break 

                if POSITIVO:
                    lista_signo.append('+')
                else:
                    lista_signo.append('-')
        
        else:

            for i in range(indice , -1 , -1):
                letra = cadena[i]

                if letra in '+-':
                    break
            lista_signo.append(letra)

        Q += 1

# Se encarga de modificar el signo de las constantes de acuerdo a la ecuación
    for i in range( len(lista_signo) ):
        signo = lista_signo[i]

        if signo == '-':
            #print(f"Signo encontrado: {lista_signo[i]}")
            #print(f"Cambio: {lista_numeros[i]}") , print(type(lista_numeros[i]))
            lista_numeros[i] *= -1
            #print()


    print(f"\nLista de números: {lista_numeros}")
    print(f"Lista signo: {lista_signo}")

    return lista_numeros

cadena = "x + y -15 = 0" # y - 15 = 0

