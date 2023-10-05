from Caja import Caja
from Packing import Packing
from Bidon import Bidon


def leer_archivos():

    cajas = []
    packings = []
    bidones = []

    with open('Cajas.csv', 'r') as arch_cajas:

        data_cajas = arch_cajas.readlines()[:-1]
        for data in data_cajas:
            datos = data.strip('\n').split(',')
            contenido = datos[0]
            peso = int(datos[1])
            caja = Caja(contenido, peso)
            cajas.append(caja)

    with open('Packing.csv', 'r') as arch_packing:

        data_packing = arch_packing.readlines()[:-1]
        for data in data_packing:
            datos = data.strip('\n').split(',')
            contenido = datos[0]
            pesoPorCaja = int(datos[1])
            cant = int(datos[2])
            est = int(datos[3])
            packing = Packing(contenido, pesoPorCaja, cant, est)
            packings.append(packing)

    with open('Bidones.csv', 'r') as arch_bidones:

        data_bidones = arch_bidones.readlines()[:-1]
        for data in data_bidones:
            datos = data.strip('\n').split(',')
            contenido = datos[0]
            cap = int(datos[1])
            dens = float(datos[2])
            bidon = Bidon(contenido, cap, dens)
            bidones.append(bidon)

    return cajas, packings, bidones
