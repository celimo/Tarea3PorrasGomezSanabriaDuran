La presente tarea busca exponer al grupo de estudiantes a algunas herramientas básicas de programación y distribución de código para el lenguaje Python,
específicamente para python3. Para aproximarse a este reto debidamente se separa la tarea en tres secciones.

Desarrollo de Código
Usted debe de desarrollar los siguientes tres métodos de Python:
1. Presentador de Imágenes: Un método que permite desplegar imágenes en pantalla, debe de permitir al usuario elegir entre una presentación
a escala 1:1, 1:2, 2:1. Debe de operar con solo imágenes de formato jpg.
2. Presentador de sonido: Un método que permite reproducir audio exclusivamente de formato mp3. El usuario debe de poder especificar la
cantidad de veces que quiere escuchar el audio.
3. Analizador de texto: Un método que cuenta cada palabra en un archivo .txt y genera otro archivo txt con una tabla que dice la cantidad
de cada palabra. Las palabras están separadas por un _ y no hay cambios de línea.
Ningún método puede utilizar input, todas las entradas que necesiten deben de ser parámetros del método. Para el punto 3 se recomienda
investigar el módulo tabulate de Python. Se recomienda trabajar cada método en un .py aparte; no obstante, esto no es obligatorio.

Scripting y argparse
En esta sección se busca convertir los tres métodos previos en scripts de Python con recepción de argumentos para su uso en la consola Shell de Linux.
1. Investigue el módulo argparse: https://docs.python.org/3/library/argparse.html
2. Utilizando la herramienta de argparse de Python debe de modificar sus archivos .py de tal forma que se pueda pasar argumentos desde el Shell de Linux y estos argumentos sean luego pasados a los métodos previamente diseñados.
3. En caso de trabajar los tres métodos en un único .py usted va a requerir un argumento para la selección del método específico.
4. Todos los scripts, o el único script en caso de usar un único .py, debe de contar con la bandera --time la cual hace que se imprima el tiempo de ejecución del método.
5. Documente debidamente los argumentos de tal forma que al usar el argumento por defecto “-h” se presente la información suficiente para que un usuario descubra como usar su script.
Para efectos de ejecución su script debe de ser ejecutable de la siguiente forma
Python3 name_of_the_script arg_1 arg_2 arg_3

Paquete de Python
Finalmente debe de convertir su código en un paquete de Python instalable desde github. Para esto se recomienda que los estudiantes verifiquen
la siguiente documentación.
• [Uso de scripts][scripts]
• [Paquetes de Python][packages]
• [Docs Setuptools][setuptools]
Se recomienda utilizar la maquina virtual de la tarea 2 y de ser necesario [crear un ambiente virtual temporal.][venv]
De forma particular para el archivo setup.py se debe tener atención en los siguientes parámetros del objeto setuptools:
• Package_dir
• Packages
• Scripts
• Install_requires
• Python_requires
Se espera poder instalar el paquete de Python de la siguiente forma
pip3 install git+https://github.com/USUARIO/NOMBRE_DE_REPOSITORIO

[La fuente de este proyecto está disponible aquí][src].

[src]: https://github.com/celimo/Tarea3PorrasGomezSanabriaDuran
[scripts]: https://packaging.python.org/guides/distributing-packages-using-setuptools/#scripts
[packages]: https://packaging.python.org/tutorials/packaging-projects/
[setuptools]: https://setuptools.readthedocs.io/en/latest/setuptools.html
[venv]: https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments
