from Carga import Carga


class Packing(Carga):
    def __int__(self, cont, peXca, cant, pe_es):
        super().__init__(cont)
        self.pesoPorCaja = peXca
        self.cantidad = cant
        self.peso_estructura = pe_es

    def __str__(self):
        return (f'{super().__str__()}, PACKING Peso x caja: {self.pesoPorCaja}, '
                f'cant: {self.cantidad}, peso estructura: {self.peso_estructura}')

    def getPesoxCarga(self):
        return self.pesoPorCaja

    def setPesoxCarga(self, val):
        self.pesoPorCaja = val

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, val):
        self.cantidad = val

    def getPesoEstructura(self):
        return self.peso_estructura

    def setPesoEstructura(self, val):
        self.peso_estructura = val

    def peso(self):
        return self.peso_estructura + (self.pesoPorCaja * self.cantidad)
