from No import No
from Fila import Fila

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def add(self, raiz: No, valor):
        if raiz is None:
            nodo = No(valor)
            if self.raiz is None:
                self.raiz = nodo
            return nodo

        if valor < raiz.dado:
            raiz.esq = self.add(raiz.esq, valor)
    
        if valor > raiz.dado:
            raiz.dir = self.add(raiz.dir, valor)

        return raiz
    
    def imprimir_em_ordem(self, raiz : No):
        if raiz != None:
            self.imprimir_em_ordem(raiz.esq)
            print(raiz.dado, end= " - ")
            self.imprimir_em_ordem(raiz.dir)
    
    def imprimir_pre_ordem(self, raiz : No):
        if raiz != None:
            print(raiz.dado, end= " - ")
            self.imprimir_pre_ordem(raiz.esq)
            self.imprimir_pre_ordem(raiz.dir)

    def imprimir_pos_ordem(self, raiz : No):
        if raiz != None:
            self.imprimir_pos_ordem(raiz.esq)
            self.imprimir_pos_ordem(raiz.dir)
            print(raiz.dado, end= " - ")

    def imprimir_reverso(self, raiz : No):
        if raiz != None:
            self.imprimir_reverso(raiz.dir)
            print(raiz.dado, end= " - ")
            self.imprimir_reverso(raiz.esq)

    def imprimirEmNível(self, raiz : No):
        if raiz == None:
            print("Árvore vazia!")
            return

        fila = Fila()
        fila.add(raiz)

        while fila.inicio != None:
            tam = fila.tamanho
            for _ in range(tam):
                atual = fila.remover()
                print(atual.dado, end = " - ")
                if atual.esq != None:
                    fila.add(atual.esq)
                if atual.dir != None:
                    fila.add(atual.dir)
            print()