
from domotica import Device 
import board  
import time 
if __name__ == "__main__":
    access_token = 'xLNhpHJOqprDFP6Sbkzi' 
    pin = board.D15
    device = Device(access_token, pin)
    device.connect_mqtt()
    sensor_data = device.read_sensor_data()
    if sensor_data:
        device.publish_data(sensor_data)

