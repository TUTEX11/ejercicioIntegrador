from Carga import Carga


class Caja(Carga):
    def __init__(self, cont, pes):
        super().__init__(cont)
        self.peso = pes

    def __str__(self):
        return f'{super().__str__()}, CAJA peso: {self.peso}'

    @property
    def peso(self):
        return self.peso

    @peso.setter
    def peso(self, value):
        self.peso = value
