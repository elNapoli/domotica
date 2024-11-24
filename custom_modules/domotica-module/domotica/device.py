import adafruit_dht
import board
from time import sleep
from .thingsboard_mqtt import ThingsBoardMQTT  # Importa la clase
import time

class Device:
    def __init__(self, access_token, pin, host='192.168.1.90'):
        self.access_token = access_token
        self.pin = pin
        self.host = host
        
        # Configurar el cliente MQTT
        self.mqtt_client = ThingsBoardMQTT(self.access_token, host=self.host)
        
        # Configuración del sensor DHT11
        self.dht_device = adafruit_dht.DHT11(self.pin)

    def connect_mqtt(self):
        """Conectar al cliente MQTT"""
        try:
            if self.mqtt_client.connect():
                self.mqtt_client.start()
                print("Conectado a ThingsBoard MQTT.")
            else:
                print("No se pudo conectar al servidor MQTT.")
        except Exception as e:
            print(f"Error al conectar con MQTT: {e}")

    def read_sensor_data(self):
        """Leer los datos del sensor DHT11"""
        try:
            temperature = self.dht_device.temperature
            humidity = self.dht_device.humidity
            
            if temperature is None or humidity is None:
                raise ValueError("No se pudieron leer los datos del sensor.")
            
            return {'temperature': temperature, 'humidity': humidity}
        except Exception as e:
            print(f"Error al leer el sensor: {e}")
            return None

    def publish_data(self, sensor_data):
        """Publicar los datos de temperatura y humedad a ThingsBoard"""
        if sensor_data:
            self.mqtt_client.publish(sensor_data)

    def run(self):
        """Ejecutar la lectura y publicación continua"""
        try:
            while True:
                sensor_data = self.read_sensor_data()
                if sensor_data:
                    self.publish_data(sensor_data)
                time.sleep(10)  # Esperar 10 segundos antes de la siguiente lectura
        except KeyboardInterrupt:
            print("\nInterrupción manual: Deteniendo cliente MQTT.")
        finally:
            self.mqtt_client.stop()
            print("Cliente MQTT detenido.")

