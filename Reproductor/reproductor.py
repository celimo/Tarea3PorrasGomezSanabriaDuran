#Librerias
import argparse
from pygame import mixer


# Función para reproducir un sonido
def reproducirAudio(nombre, cant):
	mixer.init()
	mixer.music.load(nombre)  # Se carga el archivo con la dirección
	mixer.music.play(cant)  # Se inicia la reproducción cierta cantidad
	while mixer.music.get_busy():

# Parte del argparse
parser = argparse.ArgumentParser()
parser.add_argument("nombre", help ="Nombre del archivo .mp3", type=str)
parser.add_argument("cant", help ="Cantidad de reproducciones de la canción", type=int)
args = parser.parse_args()

funcion = reproducirAudio(args.nombre, args.cant)
