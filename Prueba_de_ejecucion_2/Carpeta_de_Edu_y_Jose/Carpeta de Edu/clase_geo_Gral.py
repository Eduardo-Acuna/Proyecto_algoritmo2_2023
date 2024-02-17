from funcion_geo_Gral import*
from Funcion_Gral import*

class SegundoGrado:

    def __init__ (self , A , B , C):
        self.A = A
        self.B = B
        self.C = C
    
    def hallar_raices (self):
        determinante = self.B ** 2 - 4 * self.A * self.C
        raiz_1 = (-self.B + (determinante) ** 0.5 ) / ( 2 * self.A )
        raiz_2 = (-self.B - (determinante) ** 0.5 ) / ( 2 * self.A )

        return raiz_1 , raiz_2
    
    def determinante(self):
        return self.B ** 2 - 4 * self.A * self.C

    def impresion (self):
        if self.A == 1:
            imprimir = f"Ecuación de la forma x² + {self.B}x + {self.C} = 0"
        elif self.A == -1:
            imprimir = f"Ecuación de la forma -x² + {self.B}x + {self.C} = 0"
        else:
            imprimir = f"Ecuación de la forma {self.A}x² + {self.B}x + {self.C} = 0"
        return(imprimir)

class Fraccion:

    def __init__(self , numerador , denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self , otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + \
                          otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador , nuevo_denominador)
        resultado.simplificar()
        return(resultado)

    def __sub__(self , otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador - \
                          otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador , nuevo_denominador)
        resultado.simplificar()
        return(resultado)

    def __mul__(self , otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador , nuevo_denominador)
        resultado.simplificar()
        return(resultado)

    def  __truediv__(self , otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        resultado = Fraccion(nuevo_numerador , nuevo_denominador)
        resultado.simplificar()
        return(resultado)

    @staticmethod
    def calcular_mcd(a: int, b: int):
        if a < b:
            a, b = b, a

        if a == 0:
            return abs(b)
        
        elif b == 0:
            return abs(a)

        while True:
            r = a % b
            if r == 0:
                return(b)
            else:
                a, b = b, r

    def simplificar(self):

        if self.denominador != 0:
            mcd = self.calcular_mcd(self.numerador , self.denominador)
            self.numerador = self.numerador // mcd
            self.denominador = self.denominador // mcd

        else:
            return None

    def obtener_numerador_simplificado(self):
        
        self.simplificar()  # Asegurarse de que la fracción esté simplificada
        return self.numerador

    def obtener_denominador_simplificado(self):

        self.simplificar()  # Asegurarse de que la fracción esté simplificada
        return self.denominador

    def pendiente(self , otra_fraccion):
        nuevo_numerador = self.denominador - otra_fraccion.denominador
        nuevo_denominador = self.numerador - otra_fraccion.numerador
        resultado = Fraccion(nuevo_numerador , nuevo_denominador)
        resultado.simplificar()

        return resultado

    def __str__(self):
        if (self.numerador > 0 and self.denominador < 0) or \
            (self.numerador < 0 and self.denominador > 0):
            return f"-{abs(self.numerador)}/{abs(self.denominador)}"
        else:
            return f"{self.numerador}/{self.denominador}"
        
class Punto:

    def __init__(self , x , y):
        self.x = x
        self.y = y

    def punto_medio(self , otro_punto):

        medio_x = (self.x + otro_punto.x) / 2
        medio_y = (self.y + otro_punto.y) / 2

        return medio_x , medio_y
    
    def distancia_punto(self , otro_punto):
        distancia = ( (self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2 ) ** 0.5
        return(distancia)
    
    def __str__(self):
        return {self.x} , {self.y}

class Recta:

    def __init__(self, *args):
        if len(args) == 3 and all(isinstance(arg, (int, float)) for arg in args):
            # Si se proporcionan 3 argumentos y son números (int o float),
            # asumimos que son A, B y C.
            a , b , c = args
            self.cadena = aux_ordenar_ecuación_final_float( aux_tres_constantes_a_cadena(a , b , c) )

        elif len(args) == 1 and isinstance(args[0], str):
            # Si se proporciona una cadena, la usamos directamente.
            self.cadena = aux_ordenar_ecuación_final( args[0] )

        else:
            raise ValueError("Parámetros inválidos")

    def encontrar_constantes(self):
        return aux_encontrar_constantes_recta_float(self.cadena)

    def __str__(self):
        return self.cadena

class Circunferencia:

    def __init__(self, *args):
        if len(args) == 3 and all(isinstance(arg , (int, float)) for arg in args):
            # Si se proporcionan 3 argumentos y son números (int o float),
            # asumimos que son A, B y C.
            a , b , c = args
            self.cadena = aux_ordenar_ecuación_final( Circunf1(a , b , c) )

        elif len(args) == 1 and isinstance(args[0] , str):
            # Si se proporciona una cadena, la usamos directamente.
            self.cadena = aux_ordenar_ecuación_final( args[0] )

        else:
            raise ValueError("Parámetros inválidos")

    def encontrar_constantes(self):
        return cia_encontrar_constantes_DEF(self.cadena)

    def encontrar_ubicacion(self):
        h , k , r = cia_encontrar_hkr_cadena(self.cadena)
        return h , k , r

    def __str__(self):
        return self.cadena

class Parabola:

    def __init__(self, *args):
        if len(args) == 3 and all(isinstance(arg , (int, float)) for arg in args):
            # Si se proporcionan 3 argumentos y son números (int o float),
            # asumimos que son A, B y C.
            a , b , c = args
            self.cadena = aux_ordenar_ecuación_final( Circunf1(a , b , c) )

        elif len(args) == 1 and isinstance(args[0] , str):
            # Si se proporciona una cadena, la usamos directamente.
            self.cadena = aux_ordenar_ecuación_final( args[0] )

        else:
            raise ValueError("Parámetros inválidos")

    def encontrar_constantes(self):
        return cia_encontrar_constantes_DEF(self.cadena)

    def encontrar_ubicacion(self):
        h , k , r = cia_encontrar_hkr_cadena(self.cadena)
        return h , k , r

    def __str__(self):
        return self.cadena
