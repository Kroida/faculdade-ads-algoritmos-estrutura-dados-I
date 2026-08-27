from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    # Lista encadeada por ordem de crescente
    def add(self, valor):
        nodo = No(valor)
        
        # Caso 1: Lista vazia ou novo elemento é menor que o primeiro
        if self.inicio == None or nodo.dado < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
            return
        
        # Caso 2: Inserção no meio ou no final da lista
        ant = self.inicio
        aux = self.inicio.prox

        while aux != None and aux.dado < nodo.dado:
            ant = aux
            aux = aux.prox
        
        # Insere o novo nó entre 'ant' e 'aux'
        nodo.prox = aux
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