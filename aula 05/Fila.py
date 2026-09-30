class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, carro):
        if self.inicio is None:
            self.inicio = carro
        else:
            self.fim.prox = carro
        self.fim = carro
        print(f'\n> {carro.modelo} adicionado à Fila! :)\n')
        self.imprimir()

    def imprimir(self):
        print("\n ------ Fila Lavagem ------\n")
        if self.inicio is None:
            print("\n> Fila vazia! :(\n")
        else:
            aux = self.inicio
            c = 1
            while aux:
                print(f'{c}º - Placa: {aux.placa} | modelo: {aux.modelo}\n')
                c += 1
                aux = aux.prox

    def remover(self):
        if self.inicio is None:
            print("\n> Fila vazia! :(\n")
        else:
            aux = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print(f'\n> {aux.modelo} removido da Fila! :)\n')
            del aux
        self.imprimir()

    def getPosicao(self, placa):
        if self.inicio == None :
            print( "Fila Vazia" )
        else:
            cont = 1
            encontrou = False
            aux = self.inicio
            while aux != None:
                if aux.placa == placa:
                    encontrou = True
                    break
                else:
                    cont += 1
                    aux = aux.prox
            if  encontrou:
                print(f'Placa: {placa} encontrada na posição {cont}')
            else:
                print(f'Placa: {placa} não encontrada na fila' )
            