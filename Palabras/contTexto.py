# 

# Librerias
import argparse
import time
from tabulate import tabulate

palabra = list()
cantElementos = list()
ordenPalabra = list()


def leerArchivo(nombre, tiempo):
    if(tiempo):
        t1 = time.time()
    archivo = open(nombre, "r")
    for lineas in archivo:
        palabra.extend(lineas.split())
    for i in range(len(palabra)):
        palabra[i] = palabra[i].replace(",", "")
        palabra[i] = palabra[i].replace(".", "")
        palabra[i] = palabra[i].lower()
    cantPalabras = len(palabra)
    while (cantPalabras > 0):
        delPalabra = palabra[0]
        numPalabra = palabra.count(palabra[0])
        cantElementos.append(numPalabra)
        ordenPalabra.append(palabra[0])
        for i in range(numPalabra):
            palabra.remove(delPalabra)
        cantPalabras = len(palabra)
    print(tabulate({"Palabra": ordenPalabra, "Frecuencia": cantElementos},
          headers="keys"))
    if (tiempo):
        t2 = time.time() - t1
        print("Tiempo de ejecucion:", t2, "segundos")


# Parte del argparse
parser = argparse.ArgumentParser()
parser.add_argument("nombre", help="Nombre del archivo .txt", type=str)
parser.add_argument("--time", help="Indica si se ocupa el tiempo de ejecucion",
                    action="store_true")
args = parser.parse_args()

leerArchivo(args.nombre, args.time)
