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
# Programa que permite escalar una imagen de forma general indicando el valor
# de "x" y de "y" para escalar como x:y la imagen

# Librerias
from PIL import Image
import argparse
import time

# Globales
# args / Objeto con los parámetros que se indican al ejecutar el programa
# args.nombre / Dirección del archivo .jpg
# args.x / Cuanto se escala en "x" la imagen
# args.y / Cuanto se escala en "y" la imagen
# args.time / Indica si se reproduce o no el tiempo de ejecución

# Funcion para escalar la imagen
# Parámetros de la función:
# x / Escalado "x" de la imagen
# y / Escalado "y" de la image
# nombre / Nombre del archivo .jpg a escalar
def escalar_imagen(x, y, nombre):
	imagen = Image.open(nombre)  # Se carga la imagen
	tamano = imagen.size  # Se obtiene el array(ancho,altura)
	print(tamano)
	# Se asigna a dos variables los datos del array
	ancho = tamano[0]
	altura = tamano[1]
	# Se escala tanto el ancho como el largo
	ancho = ancho*x//y
	altura = altura*x//y
	print(ancho)
	print(altura)
	# Se le establece las nuevas dimensiones a la imagen
	escala = imagen.resize((ancho, altura))

	# Muestra la imagen en pantalla
	escala.show()


# Parte del argparse
# Se crean las variables que requiere el metodo
parser = argparse.ArgumentParser()
parser.add_argument("x", help="factor multiplicativo de la escala", type=int)
parser.add_argument("y", help="factor que divide la escala", type=int)
parser.add_argument("nombre", help="nombre de la imagen con .jpg", type=str)
parser.add_argument("--time", action='store_true',
					help="Es el tiempo que tarda la ejecucion")
args = parser.parse_args()

if (args.time):
	t1 = time.time()

# Se llama a la funcion escalar imagen
escalar_imagen(args.x, args.y, args.nombre)

# Calcula el tiempo de ejecucion del programa
if (args.time):
	t2 = time.time() - t1
	print('tiempo de ejecucion', t2)
