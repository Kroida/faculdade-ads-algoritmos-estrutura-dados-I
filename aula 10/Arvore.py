from Carro import Carro
# from Fila import Fila

class Arvore:
    def __init__(self):
        self.raiz : Carro = None
    
    def add(self, raiz: Carro, new_car : Carro ):
        if raiz is None:
            if self.raiz is None:
                self.raiz = new_car
            return new_car

        if new_car.placa < raiz.placa:
            raiz.esq = self.add(raiz.esq, new_car)
    
        if new_car.placa > raiz.placa:
            raiz.dir = self.add(raiz.dir, new_car)

        return raiz
    
    def imprimir_em_ordem(self, raiz : Carro):
        if raiz != None:
            self.imprimir_em_ordem(raiz.esq)
            print(raiz.placa, end= " - ")
            self.imprimir_em_ordem(raiz.dir)
    
    def imprimir_pre_ordem(self, raiz : Carro):
        if raiz != None:
            print(raiz.placa, end= " - ")
            self.imprimir_pre_ordem(raiz.esq)
            self.imprimir_pre_ordem(raiz.dir)

    def imprimir_pos_ordem(self, raiz : Carro):
        if raiz != None:
            self.imprimir_pos_ordem(raiz.esq)
            self.imprimir_pos_ordem(raiz.dir)
            print(raiz.placa, end= " - ")

    def imprimir_reverso(self, raiz : Carro):
        if raiz != None:
            self.imprimir_reverso(raiz.dir)
            print(raiz.placa, end= " - ")
            self.imprimir_reverso(raiz.esq)

    def imprimirEmNível(self, raiz : Carro):
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