class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is not None:
                self._insertar(valor, nodo.izquierda)
            else:
                nodo.izquierda = Nodo(valor)
        else:
            if nodo.derecha is not None:
                self._insertar(valor, nodo.derecha)
            else:
                nodo.derecha = Nodo(valor)

    def existe(self, valor):
        if self.raiz is not None:
            return self._existe(valor, self.raiz)
        else:
            return False

    def _existe(self, valor, nodo):
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izquierda != None:
            return self._existe(valor, nodo.izquierda)
        elif valor > nodo.valor and nodo.derecha != None:
            return self._existe(valor, nodo.derecha)
        return False


arbol = Arbol()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)
print(arbol.existe(5))
print(arbol.existe(3))
print(arbol.existe(123455))
print("fin de la Ejecucion")
