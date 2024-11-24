from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete encargado de gestionar clases de domotica'
LONG_DESCRIPTION = 'Paquete encargado de gestionar clases en domotica'

setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="domotica", 
        version=VERSION,
        author="Baldomero Aguila",
        author_email="<baldomero.napoli@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "adafruit-circuitpython-dht",
            "paho-mqtt"
        ],
        keywords=['python', 'domotica'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
