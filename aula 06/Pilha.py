from Livro import Livro
from No import No

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, titulo, autor, qtdPag):
        nodo = Livro( titulo, autor, qtdPag)

        if self.topo:
            nodo.prox = self.topo
        self.topo = nodo
        print("Livro inserido com sucesso!")

    def imprimir(self):
        print("-------- Pilhas - Lifo --------")
        if self.topo == None:
            print("Pilha vazia")
        else:
            aux = self.topo
            txt = ""
            while aux:
                txt += "Título: " + aux.titulo + ", autor: " + aux.autor + ", qtd de páginas: " + str(aux.qtdPag) + "\n"
                aux = aux.prox
            print( txt )
        print("---------------------------------------------")
    
    def remover(self):
        if not self.topo:
            print("Pilha vazia")
        else:
            aux = self.topo
            self.topo = aux.prox
            print(f'Livro {aux.titulo} deletado')
            del (aux)

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
                    aux = aux.prox
            if encontrou:
                print(f'Livro {titulo} encontrado na posição {posicao}')
            else:
                print(f'Livro {titulo} não encontrado na pilha' )
    
    def getPosicaoAutor(self, autor):
        if not self.topo:
            print("Pilha vazia")
        else:
            posicao = 1
            encontrou = False
            aux = self.topo
            while aux:
                if aux.autor == autor:
                    encontrou = True
                    break
                else:
                    posicao += 1
                    aux = aux.prox
            if encontrou:
                print(f'O autor {autor} possui livros nas posições: {posicao}')
            else:
                print(f'Autor {autor} não encontrado na pilha' )