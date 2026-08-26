from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    # Lista encadeada por ordem de crescente
    def add(self, valor):
        nodo = No(valor)

        # ant = self.inicio
        # aux = self.inicio.prox

        if self.inicio is None:
            self.inicio = nodo

        elif self.inicio.prox == None:
            self.inicio.prox = nodo

            ant = self.inicio
            aux = self.inicio.prox

            if ant.dado > aux.dado:
                aux.dado, ant.dado = ant.dado, aux.dado

        else:
            ant = self.inicio
            aux = self.inicio.prox

            while aux.prox != None:
                if nodo.dado < aux.dado:
                    ant.prox = nodo
                    nodo.prox = aux
                    break
                else:
                    ant = aux
                    aux = aux.prox
            
            if aux == None:
                ant.prox = nodo

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