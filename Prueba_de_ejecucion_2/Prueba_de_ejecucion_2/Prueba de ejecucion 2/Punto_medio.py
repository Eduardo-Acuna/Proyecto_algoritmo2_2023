from clase_geo_Gral import*
from funcion_geo_Gral import*
from Funcion_Gral import*

# Obs: Modifique la clase para que de vuelva el valor del punto medio en dos variables, una para la x y otra para las y
# Si o si cuando le llamas a punto_medio tiene que estar igualado en dos variables entre comas, luego esas variables
# Pueden poner en su grafica para que dibuje correctamente

a , b = 7 , -4
m , n = -15 , 22

punto1 = Punto(a , b)
punto2 = Punto(m , n)

mx , my = punto1.punto_medio(punto2)

print(f'mx: {mx} , my: {my}')

# No hacer print(punto1) , si no print(a , b) , print(m , n)