from clase_geo import*
from funcion_geo import*
from Funcion_Circunf2 import*
import random

cadena = '7x+54x-8y=100+25-4-2x' # 63x - 8y - 121 = 0
print(f"Cadena original: {cadena}\n")
cadena = aux_cambiar_variables_exponente(cadena)


# Primero estudiamos la parte izquierda de la =
miembro_1 = aux_terminos_miembro_1(cadena)
signo_1 = aux_signo_miembro_1(cadena)

# Segundo estudiamos la parte derecha de la =
comprobacion = aux_terminos_miembro_2(cadena)
if comprobacion is not None: # Falla si el usuario no escribió el segundo miembro
    miembro_2 = comprobacion
    signo_2 = aux_signo_miembro2(cadena)
    #print(f"Primer miembro: {miembro_1}"    )
    #print(f"Signo miembro1: {signo_1}")
    print(f"\nSegundo miembro: {miembro_2}")
    print(f"Signo miembro2 : {signo_2}\n")
# Si el usuario no puso =, entonces se corrige ese error y continuamos con el código
else:
    cadena += '=0'
    miembro_2 = aux_terminos_miembro_2(cadena)
    signo_2 = aux_signo_miembro2(cadena)
    #print(f"Primer miembro: {miembro_1}")
    #print(f"Signo miembro1: {signo_1}\n")
    print(f"\nSegundo miembro: {miembro_2}")
    print(f"Signo miembro2 : {signo_2}\n")

# Obtenidos los datos, procedemos a operar todos los términos semejantes y traer al primer miembro
#terminos_orden , signos_orden = aux_operacion_entre_terminos(miembro_1 , signo_1 , miembro_2 , signo_2 )

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

#print(f"\nSegundo miembro: {miembro_2}")
#print(f"Signo miembro2: {signo_2}")

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

print(f"En proceso: {terminos_orden}")
print(f"En proceso: {signos_orden}")
# Importante ejecutar este codigo, despues de las CTE del miembro 2 para no tener errores
while len(miembro_2) != 0:
    signo_2 = aux_cambio_signo_miembro_2(signo_2) # Antes de pasar, hay que cambiar de signo

    terminos_orden.append( miembro_2.pop()  )
    signos_orden.append(  signo_2.pop() )

# Lista ordenada: ['17x', '14y', 56, '19x', 13]
# Signo ordenado: ['-', '-', '-', '+', '+']

#print(f"\nSegundo miembro: {miembro_2}")
#print(f"Signo miembro2: {signo_2}")

"""----------------------------------------------------------------------------------------""" 
# Se encarga solo de analizar las CTE del miembro resultado
cte_lista , cte_signos , cte_indice = [] , [] , []
for i in range( len(terminos_orden) ):
    elemento = terminos_orden[ i ]

    if isinstance(elemento , int):
        cte_indice.append( elemento )
        cte_lista.append( elemento )
        cte_signos.append( signos_orden[ i ] )

print(f"\ncte_indice: {cte_indice}")
print(f"cte_lista: {cte_lista}")
print(f"cte_signos: {cte_signos}\n")

if len(cte_lista) > 0:

    # Se encarga de cambiar el signo de la constante en caso de ser necesario
    for k in range( len(cte_signos) ):
        elemento = cte_signos[ k ]
        buscar = cte_indice[ k ]
        eliminar = terminos_orden.index( buscar ) # Es un índice

        if elemento == '-':
            cte_lista[ k ] *= -1

        print(f"Eliminación: {terminos_orden[eliminar]}")
        print(f"Eliminación: {signos_orden[eliminar]}")
        terminos_orden.pop( eliminar )
        signos_orden.pop( eliminar )

    suma = 0
    for elemento in cte_lista:
        suma += elemento
        
    if suma != 0:
        terminos_orden.append( abs( suma ) )
        if suma > 0:
            signos_orden.append('+')
        else:
            signos_orden.append('-')




"""----------------------------------------------------------------------------------------""" 

# Se encarga de operar los terminos semejanes de cada miembro


# Se encarga de traer todas las consntantes del segundo miembro si es que existen al primer miembro (signo cambiado)

#print(f"\nPrimer miembro: {miembro_1}")
#print(f"Signo miembro1: {signo_1}")

#print(f"\nSegundo miembro: {miembro_2}")
#print(f"Signo miembro2: {signo_2}")
#print(f"Super importantes que ya estén vacíos")

print(f"\nLista ordenada: {terminos_orden}")
print(f"Signo ordenado: {signos_orden}")



