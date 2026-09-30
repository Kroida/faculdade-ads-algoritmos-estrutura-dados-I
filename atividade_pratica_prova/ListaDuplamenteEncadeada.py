from No import No
from Pagina import Pagina

class Lista:
    def __init__(self):
        self.inicio = None
        self.atual = None
        self.fim = None

    def acessarPag(self, url, data_acesso):
        nodo = No(Pagina(url, data_acesso))

        if self.inicio is None:
            self.inicio = nodo
            self.atual = nodo
            self.fim = nodo
        else:
            if nodo.dado.data_acesso < self.inicio.dado.data_acesso:
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
                self.atual = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if nodo.dado < aux.dado:
                        ant.proximo = nodo
                        nodo.proximo = aux
                        nodo.anterior = ant
                        aux.anterior = nodo
                        self.atual = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None:
                    ant.proximo = nodo
                    nodo.anterior = ant
                    self.fim = nodo
                    self.atual = nodo
        
        print(f"Página exibida: {nodo.dado.url}")
    
    def avancar(self):
        if self.inicio == None:
            print("Histórico vazio")
        elif self.atual.proximo == None:
            print("Próximo nó inexistente")
        else:
            ant = self.atual
            aux = self.atual.proximo

            self.atual = aux

            print(f"Avançado para {aux.dado.url}")

    def voltar(self):
        if self.inicio == None:
            print("Histórico vazio")
        elif self.atual.anterior == None:
            print("Próximo nó inexistente")
        else:
            ant = self.atual
            aux = self.atual.anterior

            self.atual = aux

            print(f"Voltado para {aux.dado.url}")

    def pagAtual(self):
        print(f"A página atual é {self.atual.dado.url}")

    def historico(self):
        print("-------- Histórico --------")
        if self.inicio == None:
            print("Histórico vazio")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado.url, aux.dado.data_acesso)
                aux = aux.proximo
        print("---------------------------")
                    
