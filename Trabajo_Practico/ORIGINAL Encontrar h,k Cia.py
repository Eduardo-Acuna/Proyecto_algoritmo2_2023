from clase_geo import*
from funcion_geo import*
from Funcion_Circunf2 import*

cadena = 'x2 + y2 + 8x - 14y - 160' # -x2-y2+56x+56y-84=2x2+2y2+6

# Se encarga de encontrar y separar los terminos en una lista
terminos_lista = aux_terminos_miembro_1(cadena) 
# Se encarga de encontrar y separar los signos de los terminos en una lista
signos_lista = aux_signo_miembro_1(cadena)

"""------------------------------------------------------------------------------"""

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

# Se encarga de corregir el signo de la constante C
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

print(f"Terminos: {terminos_lista}")
print(f"Signos  : {signos_lista}")

print(f"\na: {a} , h: {h}")
print(f"b: {b} , k: {k}")
print(f"c: {c}")
print(f"\nRadio: {radio}")
