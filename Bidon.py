from Carga import Carga


class Bidon(Carga):
    def __init__(self, cont, cap, dens):
        super().__init__(cont)
        self.capacidad = cap
        self.densidad = dens

    def __str__(self):
        return f'{super().__str__()}, BIDON Capacidad: {self.capacidad}, densidad: {self.densidad}'

    def peso(self):
        return self.capacidad * self.densidad

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, val):
        self.capacidad = val

    def getDensidad(self):
        return self.densidad

    def setDensidad(self, val):
        self.densidad = val

