from Torre import Torre


class Apartamento:
    def __init__(
        self,
        id: int,
        numero: str,
        torre: Torre,
        vaga: int = None
    ):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga

    def __str__(self):
        if self.vaga is None:
            return f"{self.id} - {self.numero} - {self.torre} - Sem vaga"

        return f"{self.id} - {self.numero} - {self.torre} - Vaga {self.vaga}"