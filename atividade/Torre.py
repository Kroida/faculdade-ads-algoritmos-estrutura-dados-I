class Torre:
    def __init__(self, id: int, nome: str, endereco: str):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"{self.id} - {self.nome}"