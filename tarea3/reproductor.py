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
# Programa para reproducir un audio indicando la ubicación del
# archivo y la cantidad de veces que se desea reproducir

# Librerias
import argparse
from pygame import mixer
import time

# == Variables ==
# Globales
# args / Objeto con los parámetros que se indican al ejecutar el programa
# args.nombre / Dirección del audio
# args.cant / Indica la cantidad de veces que se reproduce el audio
# args.time / Indica si se reproduce o no el tiempo de ejecución
# Local de la función reproducirAudio
# nombre / Contiene la dirección de la canción a reproducir
# cant / Indica cuantas veces se debe reproducir la canción
# t1 / Indica el tiempo inicial en que se empezó a ejecutar el método
# t2 / Tiempo total de ejecución


# Función para reproducir un sonido
# Parámetros de entrada:
# nombre / Dirección del archivo a reproducir
# cant / Cantidad de veces a reproducir el archivo
# timer / Indica si se imprime el tiempo de ejecución
def reproducirAudio(nombre, cant, timer):
	mixer.init()
	mixer.music.load(nombre)  # Se carga el archivo con la dirección
	mixer.music.play(cant)  # Se inicia la reproducción cierta cantidad
	if(timer):
		t1 = time.time()
	if(cant > 0):  # Siempre que la cantidad sea mayor que cero se reproduce
		while (cant > 0):
			mixer.music.play()  # Se inicia la reproducción cierta cantidad
			while mixer.music.get_busy():  # Evita cerrar el programa
				time.time()
			cant -= 1
	if(timer):
		t2 = time.time() - t1
		print("Tiempo de ejecucion:", t2, "segundos")


# Parte del argparse
parser = argparse.ArgumentParser()
parser.add_argument("nombre", help="Nombre del archivo .mp3", type=str)
parser.add_argument("cant", help="Cantidad de reproducciones de la canción",
type=int)
parser.add_argument("--time", help="Indica si se ocupa el tiempo de ejecucion",
action="store_true")
args = parser.parse_args()

reproducirAudio(args.nombre, args.cant, args.time)
