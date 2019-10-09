import time
import threading
#Libreria para comunicacion I2C con arduino.
import smbus
#Configurando I2C como master
bus = smbus.SMBus(1)
#Asignamos la direccion 0x04 que es la misma direccion del Arduino
direccion1 = 0x38
#Interrupcion por hardware
def pinkCall(channel):
    pulsador = Raspberry()
    inputValue = GPIO.input(4)
    
    if(inputValue == True):
        #Apagamos el led desde el pulsador
        GPIO.output(4, 0)
        #Se envia el numero 0 al Arduino via I2C
        bus.write_byte(direccion1, 0)

    if(inputValue == False):
        #Encendemos el led desde el pulsador
        GPIO.output(4, 1)
        #Se envia el numero 1 al Arduino via I2C
        bus.write_byte(direccion1, 1)
