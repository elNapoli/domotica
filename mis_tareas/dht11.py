
from domotica import Device 
import board  
import time 
if __name__ == "__main__":
    access_token = 'xLNhpHJOqprDFP6Sbkzi' 
    pin = board.D15
    device = Device(access_token, pin, 60)
    device.connect_mqtt()
    device.run()
