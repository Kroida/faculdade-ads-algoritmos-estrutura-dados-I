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

    def remover(self, valor):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            removido = False

            if self.inicio.dado == valor:
                aux = self.inicio
                self.inicio = self.inicio.prox
                del(aux)
                removido = True
            else:
                ant = self.inicio
                aux = self.inicio.prox

                while aux:
                    if aux.dado == valor:
                        ant.prox = aux.prox
                        del (aux)
                        removido = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removido:
                print("Item (", valor, ") removido com sucesso!")
            else:
                print("Item (", valor, ") não encontrado!")