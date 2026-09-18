from Livro import Livro
from No import No

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, titulo, autor):
        nodo = Livro( titulo, autor)
        # nodo = No(valor)
        # print(valor.titulo + valor.autor)

        if self.topo:
            nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def imprimir(self):
        print("-------- Pilhas - Lifo --------")
        if self.topo == None:
            print("Pilha vazia")
        else:
            aux = self.topo
            txt = ""
            while aux:
                txt += aux.titulo + " - "
                aux = aux.prox
            print( txt )
        print("---------------------------------------------")
    
    def remover(self, titulo):
        if not self.topo:
            print("Pilha vazia")
        else:
            posicao = 1
            deletado = False
            aux = self.topo
            while aux:
                if aux.titulo == titulo:
                    aux = self.topo.prox
                    self.topo = aux
                    del (aux)
                    deletado = True
                else:
                    posicao += 1
                    aux = self.topo.prox
            if deletado:
                    print(f'Livro {titulo} deletado')
            else:
                print(f'Livro {placa} não encontrado na pilha' )

    def getPosicao(self, titulo):
        if not self.topo:
            print("Pilha vazia")
        else:
            posicao = 1
            encontrou = False
            aux = self.topo
            while aux:
                if aux.titulo == titulo:
                    encontrou = True
                    break
                else:
                    posicao += 1
                    aux = topo.prox
            if encontrou:
                print(f'Livro {titulo} encontrado na posição {posicao}')
            else:
                print(f'Livro {placa} não encontrado na pilha' )