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
