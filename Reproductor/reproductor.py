# Programa para reproducir un audio indicando la ubicación del archivo y la cantidad de veces que se desea reproducir

#Librerias
import argparse
from pygame import mixer
import time

# Variables
# Globales
# args / Objeto con los parámetros que se indican al ejecutar el programa
# Local de la función reproducirAudio
# nombre / Contiene la dirección de la canción a reproducir
# cant / Indica cuantas veces se debe reproducir la canción
# t1 / Indica el tiempo inicial en que se empezó a ejecutar el método

# Función para reproducir un sonido
def reproducirAudio(nombre, cant, t1):
	mixer.init()
	mixer.music.load(nombre)  # Se carga el archivo con la dirección
	mixer.music.play(cant)  # Se inicia la reproducción cierta cantidad
	if(cant > 0):  # Siempre que la cantidad sea mayor que cero se reproduce
		while (cant > 0): 
			mixer.music.play()  # Se inicia la reproducción cierta cantidad
			while mixer.music.get_busy():  # Solo sirve para que no se cierre el programa
				time.time()
			cant -= 1
	t2=time.time() - t1
	print("Tiempo de ejecucion:", t2, "segundos")

# Parte del argparse
parser = argparse.ArgumentParser()
parser.add_argument("nombre", help ="Nombre del archivo .mp3", type=str)
parser.add_argument("cant", help ="Cantidad de reproducciones de la canción", type=int)
parser.add_argument("--time", default=time.time())
args = parser.parse_args()

reproducirAudio(args.nombre, args.cant, args.time)
