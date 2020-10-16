from setuptools import setup

setup(name="Prueba",  # Nombre
    version="1.0",  # Versión de desarrollo
    description="Paquete de prueba",  # Descripción del funcionamiento
    author="Alejo",  # Nombre del autor
    author_email='me',  # Email del autor
    license="MIT",  # Licencia: MIT, GPL, GPL 2.0...
    url="http://ejemplo.com",  # Página oficial (si la hay)
    packages=['Paquetes'],
    scripts=['Paquetes/Imagen/Imagen.py','Paquetes/Reproductor/reproductor.py','Paquetes/Palabras/contTexto.py'],
    install_requires=['PIL','pygame','tabulate'],
)