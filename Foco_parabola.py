from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

"""
Obs: Función extremadamente dificil de entender y crear, fue la función que mas tiempo de programación me llevó,
tiene mucha información que antender

Parabolas para prueba:

Vertical: x2-2y=-24 , 5x2-30x+72y-720=0 , 7=2x-4y+5 , x2-2x+6y-5=0 , 4x2 - x + 6y + 5 = 0
Horizontal: y2 - 2y + 6x - 5 = 0 , 3y2 - x + 6y - 5 = 0 , 4y2 - y + 6x + 5 = 0 , y2 - 2y - 6x + 7 = 0

Si o si cuando le llamas a la funcion Foco_parabola tiene que estar igualado con 6 variables, si no hacen eso
te dará un error de cantidad de arguementos no disponibles

h , k ---> son el par ordenado del vértice de la parábola
p ---> es el parámetro de la parábola, te dará positivo o negativo dependiente de donde apunte el arco
fx , fy ---> son el par ordenado del foco de la parábola
bandera ---> te dice el tipo de parábola que es, ya sea de forma veritical u horizonal
x2 es para los verticales e y2 es para los horizontales

Mi código no admite parábola en rotación, solo en translación. No importa como ponga el usuario, vertical u horizontal
te ordena todo.

Puse 6 variables a retornar porque no sé exactamente que te pide la interfaz para dibujar un parábola, usen las
variables que le sean de utilidad.

Mismo caso para los espacios --> .replace(' ' , '')


"""

ecuacion_parabola = '5x2-30x+72y-720=0'
ecuacion_parabola = aux_ordenar_ecuación_final_float(ecuacion_parabola)
#ecuacion_parabola = aux_ordenar_ecuación_final_float(ecuacion_parabola).replace(' ' , '') # Sin espacios

h , k , p , fx , fy , bandera = Foco_parabola(ecuacion_parabola)

print(f'Ecuación parábola: {ecuacion_parabola}')

print(f'\nVértice --> h: {h} , k: {k}')
print(f'Parámetro: {p}')
print(f'Foco --> fx: {fx} , fy: {fy}')

print(f'\nTipo de parábola: {bandera}')

