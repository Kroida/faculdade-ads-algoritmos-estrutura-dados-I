class myArray:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho

    def adicionar(self, indice, valor):
        self.dados[indice] = valor

    def acessar(self, indice):
        return self.dados[indice]

    def imprimir(self):
        for i, n in enumerate(self.dados):
            print(i, n)

    def remover(self, indice):
        valor = self.dados[indice]
        self.dados[indice] = None

        return valor