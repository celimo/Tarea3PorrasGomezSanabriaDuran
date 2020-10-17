# Programa para reproducir un audio indicando la ubicación del
# archivo y la cantidad de veces que se desea reproducir

# Librerias
import argparse
from playsound import playsound
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
	if(timer):
		t1 = time.time()
	if(cant > 0):  # Siempre que la cantidad sea mayor que cero se reproduce
		while (cant > 0):
			playsound(nombre)
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
