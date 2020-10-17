from setuptools import setup

setup(
    scripts=['bin/imagen','bin/contTexto','bin/reproductor'],
    name='tarea3', 
    version='1.2',
    author='Duran,Gomez,Sanabria,Porras',
    author_email='armando11duran@estudiantec.cr,alegove03@estudiantec.cr, jorgesanabriag@estudiantec.cr, celimojosepa@estudiantec.cr',
    description='Paquete con funciones de escalar imagenes, reproducir mp3 y contar palabras de un texto',
    download_url='https://github.com/celimo/Tarea3PorrasGomezSanabriaDuran',
    packages=['tarea3'],
    classifiers=['Escalador de imagen','Reproductor','MP3','Contador de texto','Python3'],
    python_requires='>=3.7',
    install_requires = ['pillow', 'tabulate','playsound'],
    zip_safe=False 
    )
