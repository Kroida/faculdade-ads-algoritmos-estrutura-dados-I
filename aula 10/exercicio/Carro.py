class Carro:
    def __init__(self, modelo = None, placa = None, ano = None):
        if modelo is None:
            self.modelo = input("Digite o modelo: ")
        else:
            self.modelo = modelo
        
        if placa is None:
            self.placa = input("Digite a placa: ")
        else:
            self.placa = placa

        if ano is None:
            self.ano = int(input("Digite o ano: "))
        else:
            self.ano = ano

        self.esq : Carro = None
        self.dir : Carro = None

    def __str__(self):
        txt = "\n===================="
        txt += "\nModelo: " + self.modelo
        txt += "\nAno: " + str(self.ano)
        txt += "\nPlaca: " + self.placa
        txt += "\n===================="

        return txt