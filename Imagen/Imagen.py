#Librerias
from PIL import Image
import argparse
import time


#Funcion escalar imagen
#escala que se quiere x:y
def escalar_imagen(x,y,nombre,t1):

	#t1=time.time()
	imagen=Image.open(nombre)
	tamano=imagen.size

	print(tamano)
	ancho=tamano[0]
	altura=tamano[1]
	ancho=ancho*x//y
	altura=altura*x//y
	print(ancho)
	print(altura)
	escala=imagen.resize((ancho,altura))
	escala.show()
	t2=time.time()-t1
	print('tiempo de ejecucion', t2)



#Parte del argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", help ="factor multiplicativo de la escala", type=int)
parser.add_argument("y", help ="factor que divide la escala", type=int)
parser.add_argument("nombre", help ="nombre de la imagen con .jpg", type=str)
parser.add_argument("--time", default=time.time())
args = parser.parse_args()

funcion = escalar_imagen(args.x, args.y, args.nombre, args.time)







