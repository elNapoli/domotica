# thingsboard_mqtt.py
import paho.mqtt.client as mqtt
import json
import random  # Para generar valores aleatorios de temperatura y humedad

class ThingsBoardMQTT:
    def __init__(self, access_token, host='192.168.1.90'):
        self.host = host  # Valor predeterminado para el host
        self.access_token = access_token
        self.client = mqtt.Client()
        self.client.username_pw_set(self.access_token)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    # Callback para cuando el cliente recibe la respuesta de conexión (CONNACK)
    def on_connect(self, client, userdata, flags, reason_code):
        print(f"Conectado con código de resultado {reason_code}")

    # Callback para cuando el cliente recibe un mensaje PUBLISH
    def on_message(self, client, userdata, msg):
        print(f"Mensaje recibido en el tema {msg.topic}: {str(msg.payload)}")

    # Método para publicar datos de temperatura y humedad
    def publish(self, sensor_data):
        # Aseguramos que los datos sean un diccionario
        if isinstance(sensor_data, dict):
            try:
                # Publicamos los datos en el tópico de ThingsBoard
                self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
                print(f"Datos publicados: {sensor_data}")
            except Exception as e:
                print(f"Error al publicar los datos: {e}")
        else:
            print("El parámetro 'sensor_data' debe ser un diccionario.")

    # Método para conectar al broker de ThingsBoard
    def connect(self):
        try:
            self.client.connect(self.host, 1883, 60)
        except Exception as e:
            print(f"Error al conectar al broker: {e}")
            return False
        return True

    # Método para iniciar el loop MQTT
    def start(self):
        self.client.loop_start()

    # Método para detener la conexión y el loop
    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

