# The MIT License (MIT)
#
# Copyright (c) 2017 Mike McWethy for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
:mod:`adafruit_dhtlib`
======================

CircuitPython support for the DHT11 and DHT22 temperature and humidity devices.

* Author(s): Mike McWethy
"""

import pulseio
import array
import time


class dht_base:
    """ base support for DHT11 and DHT22 devices
    """
        
    hiLev = 51    
    
    def __init__(self, dht11, pin, trigWait):
        """
        :param boolean dht11: devide type.  ==True DHT11 ==False DHT22
        :param ~board.Pin pin: digital pin used for communication 
        :param int trigWait: length of time to hold trigger in LOW state (microseconds)
        """
        self.dht11 = dht11
        self.pin = pin
        self.trigWait = trigWait
        

    def plsToBinary(self,r, s, l):
        """ PulsesToBinary takes r, a list of transition times, and converts
        them to a 1's or 0's.  The r array contains the transition times.
        r starts with a low transition time followed by a high transistion time.
        then a low followed by a high and so on.  The low transition times are 
        ignored.  Only the high transistion times are used.  If the high
        transistion time is greater than hiLev, that counts as a bit=1, if the 
        high transition time is less that hiLev, that counts as a bit=0.

        s is the starting index in r to start converting

        l is the last index + 1 in r to end converting

        Returns an integer containing the converted 1 and 0 bits
        """        
        # humidity 16 bits
        i = 0
        hiSig = False
        for e in range(s,l):
            if hiSig:
                b =0
                if r[e] > self.hiLev:
                    b = 1
                i = i<<1 | b
            hiSig = not hiSig

        return i

    def getPulses(self):
        """ getPulses implements the commumication protcol for
        DHT11 and DHT22 type devices.  It send a start signal
        of a specific length and listens and measures the 
        return signal lengths.

        pin is a board pin connected to the data pin of the device

        trigWait is the amount of time to hold the start signal
        in the low state.  This value varies based on the devide type. 

        return r (array.array uint16) contains alternating high and low
        transition times starting with a low transition time.  Normally
        r will have 81 elements for the DHT11/22 type devices.      
        """
        r = array.array('H')
        t = time.monotonic()

        # create the PulseIn object using context manager
        with pulseio.PulseIn(self.pin,81,True) as pls:

            # The DHT type device use a specialize 1-wire protocol
            # The microprocess first sends a LOW signal for a
            # specific length of time.  Then the device send back a
            # series HIGH and LOW signals.  The length the signals
            # determine the device values.
            pls.pause()
            pls.clear()
            pls.resume(self.trigWait)

            # loop until we get the return pulse we need or
            # time out after 2 seconds
            while True: 
                if len(pls)>=80:
                    break
                if time.monotonic()-t > 2.0: # time out after 2 seconds
                    break
    
            pls.pause()
            while len(pls)>0:
                r.append(pls.popleft())
            pls.resume()

        return r

    def measure(self):
        """ measure runs the communications to the DHT11/22 type device.
            if successful, the class properties tempature and humidity will
            return the reading returned from the device.

            Returns an integer.  ==0 for successful, ==-1 for checksum failure 
            (try again), ==-2 for insuffcient data return from the device (try 
            again)
        """       
        success = None

        r = self.getPulses() 
        ##print(r)

        if len(r)>=80:
            bits = array.array('B')
            for b in range(0,80,16):
                bits.append(self.plsToBinary(r,b,b+16))
            #print(bits)
            
            # humidity 16 bits
            hum = 0
            if self.dht11:
                self.hum = bits[0]
            else:
                self.hum = ((bits[0]<<8) | bits[1]) / 10
        
            # tempature 16 bits
            self.temp = 0
            if self.dht11:
                self.temp = bits[2]
            else:
                self.temp = ((bits[2]<<8) | bits[3]) / 10
            
            # calc  checksum
            ckSum = 0
            for b in bits[0:4]:
                ckSum += b

            if ckSum & 0xff == bits[4]:
                #checksum matches
                # report temp and humidity
                success = 0
                #print("Temp: {} C Humidity: {}% ".format(temp, hum))
                
            else:
                success = -1
                #print("checksum did not match. Temp: {} Hum: {} Checksum:{}".format(temp,hum,bits[4]))
                
        else:
            success = -2
            #print("did not get a full return.  number returned was: {}".format(len(r)))

        return success

    @property
    def temperature(self):
        return self.temp

    @property
    def humidity(self):
        return self.hum

class DHT11(dht_base):
    """ Support for DHT11 device.  

        :param ~board.Pin pin: digital pin used for communication 
    """
    def __init__(self, pin):
        super().__init__(True, pin, 18000)


class DHT22(dht_base):
    """ Support for DHT22 device.  

        :param ~board.Pin pin: digital pin used for communication 
    """
    def __init__(self, pin):
        super().__init__(False, pin, 1000)
