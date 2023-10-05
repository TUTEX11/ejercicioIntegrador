from Carga import Carga


class Camion:
    def __init__(self, pat, est, cMax):
        self.patente = pat
        self.estado = est
        self.cargaMaxima = cMax
        self.cargas = []

    def __str__(self):
        aux = ''
        for carga in self.cargas:
            aux = str(carga)+'\n'
        return (f'Pantente: {self.patente}, Estado: {self.estado}, Carga Maxima: {self.cargaMaxima}'
                f'\nCargas:\n{aux}')

    def cantidadCargas(self):
        if self.cargas is not None:
            return len(self.cargas)
        return False

    def pesoCargas(self):
        return sum(carga.getPeso() for carga in self.cargas)

    def subirCarga(self, carga: Carga):
        if (self.pesoCargas() + carga.getPeso()) < self.cargaMaxima:
            self.cargas.append(carga)
            return True
        return False

    def bajarCarga(self, carga: Carga):
        if (self.estado == 'disponible') and (carga not in self.cargas):
            return False
        self.cargas.remove(carga)
        return True

    def aReparacion(self):
        self.estado = 'reparacion'

    def saleReparado(self):
        self.estado = 'disponible'

    def enViaje(self):
        self.estado = 'viaje'

    def deRegreso(self):
        self.estado = 'disponible'

    def listoParaSalir(self):
        if self.estado == 'disponible' and (self.pesoCargas() < (self.cargaMaxima * 0.75)):
            return True
        return False

    def cargasEnOrden(self):
        cargasOrdenadas = sorted(self.cargas, key=lambda carga1: carga1.getPeso())
        aux = ''
        for carga in cargasOrdenadas:
            aux += f'{str(carga)}\n'
        return aux
