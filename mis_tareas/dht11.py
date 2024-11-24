
from domotica import Device 
import board  
import time 

def main():
    print("ejecutando....")
    access_token = 'xLNhpHJOqprDFP6Sbkzi' 
    pin = board.D15
    device = Device(access_token, pin, 10)
    device.connect_mqtt()
    device.run()
