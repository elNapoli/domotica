# Usamos una imagen base de Python 3.9 Slim
FROM python:3.9-slim

# Instala las herramientas de compilación necesarias y libgpiod
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    vim \
    libffi-dev \
    libssl-dev \
    python3-rpi.gpio \
    libgpiod2 && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo la carpeta `app` al directorio de trabajo del contenedor
COPY ./app /app
COPY ./custom_modules /custom_modules/

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instala RPi.GPIO para controlar GPIOs
RUN pip install RPi.GPIO

# Comando por defecto para ejecutar el script
CMD ["python", "main.py"]

