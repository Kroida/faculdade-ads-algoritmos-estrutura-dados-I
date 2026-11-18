class ListaVetores:
    def __init__(self):
        self.vetor = []

    # Adiciona um valor na bosta da lista
    def add(self, valor):
        self.vetor.append(valor)

    # Função para imprimir uau
    def imprimir(self):
        print("-------- Lista de vetores --------")

        if len(self.vetor) == 0:
            print("Lista vazia")
        else:
            for valor in self.vetor:
                print(valor)

        print("-----------------------------------")

    # Busca sequencial - ela itera
    def busca_sequencial(self, valor):
        for i in range(len(self.vetor)):
            if self.vetor[i] == valor:
                print("-------- Busca Sequencial --------")
                print(f"Valor encontrado na posição {i + 1}")
                print("-----------------------------------")
                return

        print("-------- Busca Sequencial --------")
        print("Valor não encontrado na lista")
        print("-----------------------------------")

    # Busca binária - tem cálculo
    def busca_binaria(self, valor):
        lista_vetores_ordenada = sorted(self.vetor)

        tamanho = len(lista_vetores_ordenada)

        inicio = 0
        fim = tamanho - 1

        while inicio <= fim:
            indice_central = (inicio + fim) // 2
            posicao_central = lista_vetores_ordenada[indice_central]

            if valor == posicao_central:
                print("-------- Busca Binária --------")
                print(f"Valor encontrado na posição {indice_central + 1}")
                print("-----------------------------------")
                return
            elif valor < posicao_central:
                fim = indice_central - 1
            else:
                inicio = indice_central + 1

        print("-------- Busca Binária --------")
        print("Valor não encontrado na lista")
        print("-----------------------------------")