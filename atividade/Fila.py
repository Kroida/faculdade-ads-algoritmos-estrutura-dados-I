from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def adicionar(self, valor):
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.prox = nodo
            self.fim = nodo

        self.quantidade += 1

    def remover(self):
        if self.inicio is None:
            print("Fila vazia!")
            return None

        aux = self.inicio
        self.inicio = self.inicio.prox

        if self.inicio is None:
            self.fim = None

        self.quantidade -= 1

        return aux.dado

    def imprimir(self):
        print("\n" + "-" * 20 + " Fila de espera " + "-" * 20)

        if self.inicio is None:
            print("Fila vazia!")
        else:
            aux = self.inicio

            while aux:
                print(aux.dado)
                aux = aux.prox

        print("-" * 56)