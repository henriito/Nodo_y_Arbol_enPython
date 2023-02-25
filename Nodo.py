class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.izdo = None
        self.dcho = None

    def __init__(self, ramaIzdo, valor, ramaDcho):
        self.dato = valor
        self.izdo = ramaIzdo
        self.dcho = ramaDcho

    def valorNodo(self):
        return self.dato

    def GetSubarbolIzdo(self):
        return self.izdo

    def GetSubarbolDcho(self):
        return self.dcho

    def nuevoValor(self, d):
        self.dato = d