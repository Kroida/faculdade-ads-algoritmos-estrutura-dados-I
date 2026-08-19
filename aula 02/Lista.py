from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    # Lista encadeada por ordem de chegada
    def add(self, valor):
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.prox == None:
            self.inicio.prox = nodo
        else:
            aux = self.inicio.prox

            while aux.prox != None:
                aux = aux.prox
            aux.prox = nodo

    def imprimir(self):
        print(("-" * 20) + "Lista encadeada por ordem de chegada" + ("-" * 20))

        if self.inicio == None:
            print("Lista vazia")
        else:
            aux = self.inicio

            while aux:
                print(aux.dado)
                aux = aux.prox
        print("-" * 76)
