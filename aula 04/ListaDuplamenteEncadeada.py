from No import No
# Lista Duplamente Encadeada
class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None

    # Lista Duplamente Encadeada por ordem CRESCENTE
    def add(self, valor):
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if nodo.dado < aux.dado:
                        ant.proximo = nodo
                        nodo.proximo = aux
                        nodo.anterior = ant
                        aux.anterior = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None:
                    ant.proximo = nodo
                    nodo.anterior = ant
                    self.fim = nodo 
        self.imprimir()

    def imprimir(self):
        print("-------- Lista Duplamente Encadeada por ordem de chegada --------")
        if self.inicio == None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.proximo
        print("------------------------------------------------------")

    def imprimirReverso(self):
            print("-------- Lista Duplamente Encadeada Reversa --------")
            if self.fim == None:
                print("Lista Vazia")
            else:
                aux = self.fim
                while aux:
                    print( aux.dado )
                    aux = aux.anterior
            print("------------------------------------------------------")
            
    def remover(self, valor):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            removido = False
            if self.inicio.dado == valor:
                aux = self.inicio
                self.inicio = self.inicio.proximo
                if self.inicio is None:
                    self.fim = None
                else:
                    self.inicio.anterior = None
                del( aux )
                removido = True
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                        if aux.proximo is None:
                            self.fim = ant
                        else:
                            aux.proximo.anterior = aux.anterior
                        del( aux )
                        removido = True
                        break
                    else: 
                        ant = aux
                        aux = aux.proximo

            if removido:
                print( "Item (",valor, ") removido com sucesso!")
            else: 
                print( "Item (",valor, ") não encontrado!")

            self.imprimir()
                    
