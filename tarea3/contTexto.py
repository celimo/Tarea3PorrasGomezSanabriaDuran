# Programa para leer un archivo de texto sin importar si contiene saltos de
# linea o no y cuenta la cantidad de palabras que contiene

# Librerias
import argparse
import time
from tabulate import tabulate

# == Variables ==
# Globales
# args / Objeto con los parámetros que se indican al ejecutar el programa
# args.nombre / Dirección del archivo de texto
# args.time / Indica si se reproduce o no el tiempo de ejecución
# palabra / Lista que va a contener las palabas del archivo que se selecciona
# cantElementos / Lista que contiene el número de repetición de las palabras
# ordenPalabra / Lista que contiene todas las palabras del archivo
# Local de la funcion leerArchivo
# nombre / Dirección del archivo .txt a leer
# tiempo / Booleana para indicar si se indica o no el tiempo de ejecución
# archivo / Objeto donde se almacena la información del archivo
# palabra / Lista temporal donde se almacena una palabra por elemento de lista
# cantPalabras / Permite indicar si ya se analizaron todas las palabras
# del archivo y salir de un ciclo while
# numPalabra / Variable temporal para almacenar el número de repeticiones
# de una palabra en la lista palabra
# t1 / Almacena el tiempo inicial de ejecución
# t2 / Almacena el tiempo final de ejecución

palabra = list()
cantElementos = list()
ordenPalabra = list()


# Funcion encargada de leer el archivo contar las palabras en el archivo
# y luego imprimirlas como una tabla con su respectiva frecuencia
# Parámetros de entrada:
# nombre / Dirección del archivo .txt a analizar
# tiempo / Indica si se imprime el tiempo de ejecución
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
parser.add_argument("-t", "--time", help="Indica si se ocupa el tiempo de ejecucion",
                    action="store_true")
args = parser.parse_args()

# Inicio del programa
leerArchivo(args.nombre, args.time)
