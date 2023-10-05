from Lector import leer_archivos
from Camion import Camion


def main():
    camion = Camion('BDM 226', 'disponible', 10000)
    cajas, packings, bidones = leer_archivos()
    camion.listoParaSalir()
    camion.subirCarga(cajas[0])
    camion.subirCarga(packings[0])
    camion.subirCarga(bidones[0])
    print(f'El total de cargas del camion es de: ', camion.cantidadCargas())
    print(f'Cargas\n {camion.cargasEnOrden()}')


if __name__ == '__main__':
    main()
