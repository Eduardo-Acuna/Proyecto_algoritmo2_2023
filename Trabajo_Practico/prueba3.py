from clase_geo import*
from funcion_geo import*
from Funcion_Circunf2 import*

def Recta2(a , b , mx , my):
    # Solamente el mx puede ser negativo, por eso este cambio de ser necesario
    if mx > 0 and my < 0:
        mx *= -1
        my *= -1

    # Se encarga de encontrar el signo de la pendiente
    signo_pendiente = recta_signo_pendiente(mx , my)

    # Función auxiliar
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

    # Se encarga de separar todos los términos con sus respectivos signos
    terminos , signos = encontrar_terminos_recta(a , b , mx , my , signo_pendiente)

    # Se encarga de encontrar la ecuación formada, ordenada pero sin espacios. Otra función hace eso
    cadena = ''
    for i in range( len(terminos) ):
        cadena += str(signos[ i ]) + str(terminos[ i ])

    return aux_ordenar_ecuación_final(cadena)

print(f"Ecuación: {Recta2(14,-5,-11,29)}")