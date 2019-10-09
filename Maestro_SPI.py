from time import sleep
#Librería SPI
import spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 250000
pulsador = Raspberry()
inputValue = GPIO.input(4)

try:
	while True:
		if(inputValue == 0):
			#Se envia el numero 0 al Arduino 
     			spi.xfer2(0)
			print "Off"
		
    		if(inputValue == 1):
        		#Se envia el numero 1 al Arduino
        		spi.xfer2(1)
			print "On"


finally:     # run on exit
	spi.close()         # clean up
    	print "All cleaned up."



