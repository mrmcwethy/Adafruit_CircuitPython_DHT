


# example of reading temperature and humidity from a DHT device
# and displaying results to the serial port and a 8 digit 7-segment display
import time
import dht
from board import D2

from  adafruit_max7219 import bcddigits
from board import TX, RX, A2
import busio
import digitalio

clk = RX
din = TX
cs = digitalio.DigitalInOut(A2)
spi = busio.SPI(clk, MOSI=din)
display = bcddigits.BCDDigits(spi, cs, nDigits=8)
display.brightness(5)
print(D2)
device = dht.DHT22(D2)

while True:
    success = device.measure()

    if success == 0:
        print("Temp: {:.1f} F Humidity: {}% ".format(device.temperature*9/5+32, device.humidity))
        display.clear_all()
        display.show_str(0,'{:5.1f}{:5.1f}'.format(device.temperature*9/5+32,device.humidity))
        display.show()
    elif success == -1:
        print("The data checksum did not validate.  Try again.")
    elif success == -2:
        print("The device did not return enough data. Try again.")
    else:
        print("Something else bad happened: Error {}".format(success))

    if success == 0:
        time.sleep(2.0) 
    else:
        time.sleep(0.4)



    