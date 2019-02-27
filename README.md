# AES-RaspberryPi-DHT11
Implemented SHA256 encryption for securing sensor data communication from Raspberry Pi

This setup focuses on encrypting sensor data from the device/gateway. Using python to extract the data from the DHT11 sensor and encrypt the outgoing data. Added the decryption code so to check the encrypted message as well. 

## Initial steps:
Install pycrypto library:  `pip3 install pycrypto` 

## Programming with Python for DHT11 setup:

Install: `sudo apt-get install git-core`

Steps to access the GPIO pins can be done via installing the BCM module. Below is the link for the setup:
https://www.airspayce.com/mikem/bcm2835/

To install the python Adafruit DHT11 library:

1. Enter this at the command prompt to download the library:
`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
2. Change directories with: `cd Adafruit_Python_DHT`
3. Now enter this: `sudo apt-get install build-essential python-dev`
4. Install the setup.py: 
`sudo python setup.py install`
5. Connect the GPIO like:

![alt text](https://github.com/niladri30/AES-RaspberryPi-DHT11/blob/master/DHT11.png)

6. Open RPi Terminal and check if the sensor is working properly:
Go to the path:  `cd /home/pi/Adafruit_Python_DHT/examples`

7. Execute: `python3 AdafruitDHT.py 11 18`
Result:  Temp=22.0*  Humidity=37.0%  (Sensor readings as per the current area)

After successful testing, run `python3 AesDHT11.py` script to see the output.
