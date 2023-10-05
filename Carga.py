from abc import ABC, abstractmethod


class Carga(ABC):
    def __init__(self, con):
        self.contenido = con

    def __str__(self):
        return f'Contenido de la carga: {self.contenido}'

    def getContenido(self):
        return self.contenido

    def setContenido(self, con: str):
        self.contenido = con

    @abstractmethod
    def getPeso(self):
        pass
