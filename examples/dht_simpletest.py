import time
import adafruit_dht
from board import D2

#initial the dht device
dhtDevice = adafruit_dht.DHT22(D2)

while True:
    try:
        # show the values to the serial port
        temperature = dhtDevice.temperature*9/5+32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F Humidity: {}% ".format(temperature, humidity))

    except RuntimeError as error:
        print(error.args)

    time.sleep(2.0)
