from setuptools import setup

setup(
    scripts=['tarea3/imagen.py','tarea3/contTexto.py','tarea3/reproductor.py'],
    name='tarea3', 
    version='1.1',
    author='Duran,Gomez,Sanabria,Porras',
    author_email='-',
    description='Paquete con funciones de escalar imagenes, reproducir mp3 y contar palabras de un texto',
    download_url='https://github.com/celimo/Tarea3PorrasGomezSanabriaDuran',
    packages=['tarea3'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent' ],
    python_requires='>=3.7',
    install_requires = ['pillow', 'tabulate'],
    zip_safe=False 
    )
