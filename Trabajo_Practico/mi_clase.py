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
        while True:
            r = a % b
            if r == 0:
                return(b)
            else:
                a, b = b, r
    
    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador , self.denominador)
        self.numerador = self.numerador // mcd
        self.denominador = self.denominador // mcd
    
    def __str__(self):
        if (self.numerador > 0 and self.denominador < 0) or \
            (self.numerador < 0 and self.denominador > 0):
            return f"-{abs(self.numerador)}/{abs(self.denominador)}"
        else:
            return f"{self.numerador}/{self.denominador}"

class Rectangulo:

    def __init__(self , largo , ancho):
        self.largo = largo
        self.ancho = ancho
    
    def rectangulo_perimetro(self):
        perimetro = (self.largo + self.ancho) * 2
        return(perimetro)
    
    def rectangulo_area(self):
        area = self.largo * self.ancho
        return(area)

    def rectangulo_diagonal(self):
        diagonal = ( self.largo ** 2 + self.ancho ** 2) ** 0.5
        return(diagonal)

    def __str__(self):
        perimetro = self.rectangulo_perimetro()
        area = self.rectangulo_area()
        diagonal = self.rectangulo_diagonal()
        return(
                f"Largo: {self.largo}"
                f"\vAncho: {self.ancho}"
                f"\vPerimetro: {perimetro}"
                f"\vÁrea: {area}"
                f"\vDiagonal: {diagonal}"
                )

class Punto2D:

    def __init__ (self , x , y):
        self.x = x
        self.y = y
    
    def distancia_punto(self , otro_punto):
        distancia = ( (self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2 ) ** 0.5
        return(distancia)
    
    def __str__ (self):
        return(f"Punto: ({self.x} , {self.y})")

class SegundoGrado:

    def __init__ (self , A , B , C):
        self.A = A
        self.B = B
        self.C = C
    
    def hallar_raices (self):
        determinante = self.B ** 2 - 4 * self.A * self.C
        raiz_1 = (-self.B + (determinante) ** 0.5 ) / ( 2 * self.A )
        raiz_2 = (-self.B - (determinante) ** 0.5 ) / ( 2 * self.A )
        return f"x1: {raiz_1}\vx2: {raiz_2}"
    
    def impresion (self):
        if self.A == 1:
            imprimir = f"Ecuación de la forma x² + {self.B}x + {self.C} = 0"
        elif self.A == -1:
            imprimir = f"Ecuación de la forma -x² + {self.B}x + {self.C} = 0"
        else:
            imprimir = f"Ecuación de la forma {self.A}x² + {self.B}x + {self.C} = 0"
        return(imprimir)

class NumeroPrimo:

    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def es_primo(numero):
        if numero <= 1:
            return False

        if numero == 2:
            return True

        if numero % 2 == 0:
            return False

        for divisor in range(3, int(numero**0.5) + 1, 2):
            if numero % divisor == 0:
                return False

        return True
    
    def __str__(self):
        if self.es_primo(self.numero):
            return f"{self.numero} = Primo"
        else:
            return f"{self.numero} = ---"

"""   --- CLASE DE ARBOLES ---   """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor): # agregar valor al árbol
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.derecha)

    def eliminar(self, valor): # eliminar valor al árbol
        if self.raiz is not None:
            self.raiz = self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                temp = nodo_actual.derecha
                nodo_actual = None
                return temp
            elif nodo_actual.derecha is None:
                temp = nodo_actual.izquierda
                nodo_actual = None
                return temp
            temp = self._encontrar_min(nodo_actual.derecha)
            nodo_actual.valor = temp.valor
            nodo_actual.derecha = self._eliminar(temp.valor, nodo_actual.derecha)
        return nodo_actual

    def _encontrar_min(self, nodo_actual):
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def modificar(self, valor, nuevo_valor): # reemplazar valor por nuevo_valor
        self.eliminar(valor)
        self.agregar(nuevo_valor)

    def imprimir(self): # imprimir arbol ordenado
        if self.raiz is not None:
            self._imprimir(self.raiz)

    def _imprimir(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir(nodo_actual.izquierda)
            print(str(nodo_actual.valor))
            self._imprimir(nodo_actual.derecha)

    def inorden(self): # recorrido inorden imprimiendo los nodos visitados
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden(nodo_actual.izquierda)
            print(str(nodo_actual.valor))
            self._inorden(nodo_actual.derecha)

    def preorden(self): # recorrido preorden imprimiendo los nodos visitados
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(str(nodo_actual.valor))
            self._preorden(nodo_actual.izquierda)
            self._preorden(nodo_actual.derecha)

    def postorden(self): # recorrido postorden imprimiendo los nodos visitados
        if self.raiz is not None:
            self._postorden(self.raiz)

    def _postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden(nodo_actual.izquierda)
            self._postorden(nodo_actual.derecha)
            print(str(nodo_actual.valor))

"""   --- CLASE DE LISTAS ---   """

class Lista:

    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista
    
    @ staticmethod
    def particion(lista , menor , mayor):

        pivote = lista[menor]
        izq = menor + 1
        der = mayor

        while True:

            while izq <= der and lista[izq] <= pivote:
                izq += 1
            
            while izq <= der and lista[der] >= pivote:
                der -= 1
            
            if der < izq:
                break
            else:
                lista[izq] , lista[der] = lista[der] , lista[izq]

        lista[menor] , lista[der] = lista[der] , lista[menor]

        return der

    def quicksort_hoare(self , menor , mayor):

        if menor < mayor:
            pivote = self.particion(self.lista , menor , mayor)
            self.quicksort_hoare(menor , pivote - 1)
            self.quicksort_hoare(pivote + 1 , mayor)

    def ordenar(self):
        self.quicksort_hoare(0 , len(self.lista) - 1)

    def suma_total(self):

        suma = 0
        for e in self.lista:
            suma += e
        return suma

    def elemento_mayor(self):

        if not self.lista:
            return None
        mayor = float("-inf")
        for e in self.lista:
            if e > mayor:
                mayor = e
        return mayor

    def elemento_menor(self):

        if not self.lista:
            return None
        menor = float("inf")
        for e in self.lista:
            if e < menor:
                menor = e
        return menor

    def agregar(self , elemento):
        self.lista.append(elemento)
    
    def sacar_pila(self):
        self.lista.pop()
    
    def sacar_cola(self):
        self.lista.pop(0)

    def tamano(self):
        return len(self.lista)
    
    def __add__(self , otra_lista):
        return self.lista + otra_lista
    
    def convertir_a_lista(self):
        return list(self.lista)

    def __str__(self):
        return str(self.lista)
