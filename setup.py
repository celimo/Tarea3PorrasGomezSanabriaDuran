from setuptools import setup

setup(name="Prueba",  # Nombre
    version="1.0",  # Versión de desarrollo
    description="Paquete de prueba",  # Descripción del funcionamiento
    author="PorrasGomezSanabriaDuran",  # Nombre del autor
    author_email='me',  # Email del autor
    license="MIT",  # Licencia: MIT, GPL, GPL 2.0...
    url="https://github.com/celimo/Tarea3PorrasGomezSanabriaDuran",  # Página oficial (si la hay)
    packages=['Paquetes'],
    scripts=['Paquetes/Imagen.py','Paquetes/reproductor.py','Paquetes/contTexto.py'],
    install_requires=['PIL','pygame','tabulate']
)
