class Arbol:
    def __init__(self):
        self.raiz = None

    def existe(self, busqueda):
        return self.existe(self.raiz, busqueda)

    def existe(self, n, busqueda):
        if n == None:
            return False
        if n.valorNodo() == busqueda:
            return True
        elif busqueda < n.valorNodo():
            return self.existe(n.GetSubarbolIzdo(), busqueda)
        else:
            return self.existe(n.GetSubarbolDcho(), busqueda)

    def insertar(self, dato):
        if self.raiz == None:
            self.raiz = Nodo(dato)
        else:
            self.insertar(self.raiz, dato)

    def insertar(self, padre, dato):
        if dato > padre.valorNodo():
            if padre.GetSubarbolDcho() == None:
                padre.SetRamaDcho(Nodo(dato))
            else:
                self.insertar(padre.GetSubarbolDcho(), dato)
        else:
            if padre.GetSubarbolIzdo() == None:
                padre.SetRamaIzdo(Nodo(dato))
            else:
                self.insertar(padre.GetSubarbolIzdo(), dato)