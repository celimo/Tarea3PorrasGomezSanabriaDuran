#Librerias
from PIL import Image
import argparse
import time


#Funcion escalar imagen
#escala que se quiere x:y
def escalar_imagen(x,y,nombre):

	
	imagen=Image.open(nombre)#se carga la imagen
	tamano=imagen.size#se obtiene el array(ancho,altura)

	print(tamano)
	#se asigna a dos variables los datos del array 
	ancho=tamano[0]
	altura=tamano[1]
	
	#Se escala tanto el ancho como el largo
	ancho=ancho*x//y
	altura=altura*x//y
	print(ancho)
	print(altura)
	
	#se le establece las nuevas dimensiones a la imagen
	escala=imagen.resize((ancho,altura))
	
	#Muestra la imagen en pantalla
	escala.show()
	
	



#Parte del argparse

# Se crean las variables que requiere el metodo
parser=argparse.ArgumentParser()
parser.add_argument("x", help ="factor multiplicativo de la escala", type=int)
parser.add_argument("y", help ="factor que divide la escala", type=int)
parser.add_argument("nombre", help ="nombre de la imagen con .jpg", type=str)
parser.add_argument("--time", action='store_true', help ="Es el tiempo que tarda la ejecucion")
args=parser.parse_args()

#se llama a la funcion escalar imagen
if args.time:
	t1=time.time()
escalar_imagen(args.x, args.y, args.nombre)

#Calcula el tiempo de ejecucion del programa
if args.time:
	t2=time.time()-t1
	print('tiempo de ejecucion', t2)





