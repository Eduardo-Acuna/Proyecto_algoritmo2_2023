from clase_geo import*

# Solo admite una ecuación con espacios entre términos y operandos, si no está espaciado, entonces primero
# hay que llamar a otra función que se encarga de espaciar cualquier cadena, pero no ordenar. La que ordena es
# el código de este archivo. Atender con eso

cadena = "y - 15 = 0" # y - 15 = 0
obj_cadena = Recta(cadena)

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
    for caracter in elemento:  # Bucle interno para cada término
        if caracter == '-':
            signo = '-'
        if caracter in '0123456789':
            txt_entero += caracter
        if 'x' in elemento or 'y' in elemento:  # Verificar si 'x' o 'y' está en el término actual
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


print(f"\nEcuación: {cadena}")
print(f"Constantes: {obj_cadena.encontrar_constantes()}")
print(f"\naux: {aux}")
print(f"\nTérminos: {terminos}")
print(f"\n{lista_x}")
print(f"{lista_y}")
print(f"{lista_cte}")
print(f"\nCadena corregida: {cadena_aux}")


    


