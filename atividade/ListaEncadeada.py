from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def adicionar(self, valor):
        nodo = No(valor)

        # Lista vazia ou novo elemento possui
        # uma vaga menor que a primeira
        if (
            self.inicio is None
            or nodo.dado.vaga < self.inicio.dado.vaga
        ):
            nodo.prox = self.inicio
            self.inicio = nodo
            self.quantidade += 1
            return

        ant = self.inicio
        aux = self.inicio.prox

        while (
            aux is not None
            and aux.dado.vaga < nodo.dado.vaga
        ):
            ant = aux
            aux = aux.prox

        nodo.prox = aux
        ant.prox = nodo

        self.quantidade += 1

    def remover(self, id):
        if self.inicio is None:
            print("A lista está vazia!")
            return None

        if self.inicio.dado.id == id:
            removido = self.inicio.dado
            self.inicio = self.inicio.prox
            self.quantidade -= 1

            print(f"Apartamento {id} removido com sucesso!")

            return removido

        ant = self.inicio
        aux = self.inicio.prox

        while aux:
            if aux.dado.id == id:
                removido = aux.dado
                ant.prox = aux.prox
                self.quantidade -= 1

                print(f"Apartamento {id} removido com sucesso!")

                return removido

            ant = aux
            aux = aux.prox

        print(f"Apartamento {id} não encontrado!")

        return None

    def imprimir(self):
        print(
            "\n"
            + "-" * 20
            + " Lista de apartamentos "
            + "-" * 20
        )

        if self.inicio is None:
            print("Lista vazia")
        else:
            aux = self.inicio

            while aux:
                print(aux.dado)
                aux = aux.prox

        print("-" * 64)
        print(f"Total: {self.quantidade}")