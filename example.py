


# Example of reading temperature and humidity from a DHT device
# Display data on a 8 digit 7-segment display as well as printing the  results
# The DHT device data-wire is connected to board.D2
import time
import adafruit_dhtlib
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

#initial the dht device
dhtDevice = adafruit_dhtlib.DHT22(D2)

while True:
    # call measure() and hope for the best
    success = dhtDevice.measure()

    if success == 0:
        # show the values to the serial port
        print("Temp: {:.1f} F Humidity: {}% ".format(dhtDevice.temperature*9/5+32, dhtDevice.humidity))

        # now show the values on the 8 digit 7-segment display
        display.clear_all()
        display.show_str(0,'{:5.1f}{:5.1f}'.format(dhtDevice.temperature*9/5+32,dhtDevice.humidity))
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
        time.sleep(0.5)



    