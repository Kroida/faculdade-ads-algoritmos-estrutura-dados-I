from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    # Fila 
    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("-------- Fila - FIFO --------")
        if self.inicio == None:
            print("Fila Vazia")
        else:
            aux = self.inicio
            txt = ""
            while aux:
                txt += aux.dado + " - "
                aux = aux.prox
            print( txt )
        print("---------------------------------------------")
            
    def remover(self):
        if self.inicio is None:
            print("A fila está vazia")
        else:
            aux = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            del( aux )
            self.imprimir()
                    
