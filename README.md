# Protocolos de comunicaciones para intercomunicar dispositivos IoT

Luego de aprender acerca de los diferentes tipos de protocolos usados en la industria para envio de datos, llevamos a cabo el siguiente taller con el fin de afianzar los conocimientos obtenidos en clase.

Objetivos requeridos
===========
- Afianzar los conceptos básicos asociados a Internet de las Cosas (IoT).
- Familiarizarse con los protocolos típicos de comunicaciones entre dispositivos IoT vía cables.
- Desarrollar dos aplicaciones sencillas para transferir comandos entre dos Raspberry Pi para encender y apagar un actuador LED utilizando I2C y SPI.
- Presentar las aplicaciones funcionando correctamente.

Materiales utilizados
===========
- 1 PC
- 1 Raspberry Pi
-1 Arduino UNO
- 1 actuador LED
- 1 protoboard y cables.
- 1 resistor de 330 ohmios.
- 1 pulsador

Cuadro comparativo entre I2C y SPI
===========
Con el fin de familiarizarnos mejor con las ventajas entre estos dos tipos de protocolos realizamos la siguiente tabla

![I2C vs SPI](https://user-images.githubusercontent.com/54821299/66438797-5ee68080-e9f3-11e9-82f9-0bab8edae915.png)

Configurar I2C en Raspberry PI
=
Estos pasos solo son validos para Raspbian, revisa el SO que estas utilizando ya que hay unos que vienen listos para usar el I2C, de cualquier manera se recomienda actualizar la versión del SO que se este utilizando. Para comenzar abrimos la terminal y escribimos el siguiente comando:

``
sudo nano /etc/modules
``

se abrirá un archivo, tenemos que añadir estas 2 lineas de código al final del archivo:

``
i2c-bcm2708
i2c-dev
``

Una vez agregadas las lineas previamente mencionadas, procedemos a guardar el archivo y a reiniciar la raspberry pi.
Para poder usar instrucciones de i2c es necesario instalar las siguientes instancias, esto lo haremos escribiendo en la terminal:

``
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
``

posteriormente vamos a escribir:

``
sudo nano /etc/modprobe.d/raspi-blacklist.conf
``

y comentamos las 2 lineas, tiene que quedar asi:

``
#blacklist spi-bcm2708
#blacklist i2c-bcm2708
``

Para guardar y salir podemos usar CTRL-x y Y.
Una vez que se hayan realizado los pasos previos podemos escribir en la terminal:

``
sudo i2cdetect -y 1
``

Esta instrucción, realizara un barrido de las direcciones y desplegara la misma una vez encuentre algún dispositivo. OJO! si no te funciona prueba con un «-y 0» envés de «-y 1», esto significa que tienes una revisión pasada de la rapsberry pi, en la nueva revisión se usa el puerto I2C 1 del hardware.

``
pi@raspberrypi ~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- 04 -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
``

Configurar I2C en Arduino UNO
=
Vamos a tener que cargar un código al que hace de esclavo (slave). Haremos uso de la librería Wire, que nos proporcionará todos los métodos y propiedades para poder utilizar el protocolo I2C de una forma sencilla.
Lo primero que hay que destacar es que tendremos un evento que se disparará cuando reciba un dato del  dispositivo master. La primera parte leerá un entero (int) y la segunda parte leerá un carácter (char). Dependiendo de si el carácter es H o L pondrá en estado alto (H) o bajo (L).

````
#include <Wire.h>
void setup() {
  // Unimos este dispositivo al bus I2C
  Wire.begin();
}

byte pin[] = {2, 3, 4, 5, 6};
byte estado = 0;

void loop() {
  for (int i = 0; i < 5; i++)
  {
    // Comenzamos la transmisión al dispositivo 1
    Wire.beginTransmission(1);

    // Enviamos un byte, será el pin a encender
    Wire.write(pin[i]);

    // Enviamos un byte, L pondrá en estado bajo y H en estado alto
    Wire.write(estado);

    // Paramos la transmisión
    Wire.endTransmission();

    // Esperamos 1 segundo
    delay(1000);
  }

  // Cambiamos el estado
  if (estado == 0)
  {
    estado = 1;
  }
  else
  {
    estado = 0;
  }
}
````

Configurar SPI en Raspberry PI
=
A continuación mostraremos una forma de configurar el protocolo SPI en la Raspberry PI desde Python, para eso, abrimos el terminal y escribiremos los siguientes comandos:

```
sudo apt get-update
sudo apt get-upgrade
sudo apt get-install python-dev python3-devcd ~
git clone https: //github.com/doceme/py-spidev.git
cd py-spidev
make
sudo make install
```

Luego de esto procederemos a cargar el codigo SPI que leera los datos recibidos del esclavo. Para esto nos dirigimos a Programming y luego a Python 3 y copiamos y pegamos el siguiente código:

```
import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 0b11
try:
while True:
resp = spi.readbytes(3)
if (resp[0] != 255):
print(resp)
value = resp[1] + resp[2]
print(value)
byte1 = bin(resp[0])[2:].rjust(8,'0')
byte2 = bin(resp[1])[2:].rjust(8,'0')
byte3 = bin(resp[2])[2:].rjust(8,'0')
bits = byte1 + byte2 + byte3
print(byte)
time.sleep(0.1)
except KeyboardInterrupt:
spi.close()
```

Configurar SPI en Arduino UNO
=
En esta sección, aprenderá a usar la interfaz SPI para enviar y recibir datos en serie para interactuar con sensores y otros dispositivos.

```
#include 

int slaveSelect = 2;

int delayTime = 50;

void setup() {
  pinMode(slaveSelect, OUTPUT);
  SPI.begin();
  SPI.setBitOrder(LSBFIRST);   
}

void loop() {
  for (int i; i < 256; i++)        //For loop to set data = 0 then increase it by one for every iteration of the loop, when the counter reaches the condition (256) it will be reset
  {
    digitalWrite(slaveSelect, LOW);            //Write our Slave select low to enable the SHift register to begin listening for data
    SPI.transfer(i);                     //Transfer the 8-bit value of data to shift register, remembering that the least significant bit goes first
    digitalWrite(slaveSelect, HIGH);           //Once the transfer is complete, set the latch back to high to stop the shift register listening for data
    delay(delayTime);                             //Delay
  }
}
```

Implementación del protocolo I2C
=
Abreviatura de Inter-IC (inter integrated circuits), un tipo de bus diseñado por Philips Semiconductors a principios de los 80s, que se utiliza para conectar circuitos integrados (ICs). El I2C es un bus con múltiples maestros, lo que significa que se pueden conectar varios chips al mismo bus y que todos ellos pueden actuar como maestro, sólo con iniciar la transferencia de datos. 

Al ser uno de los protocolos seriales más conocidos, es muy importante que aprendamos su uso. Luego de haber seguido los pasos de `Configurar I2C en Raspberry PI` y `Configurar I2C en Arduino UNO` procederemos a realizar las conexiones, en este caso, encenderemos un LED conectado al Arduino UNO enviando la orden desde la Raspberry PI.

- Diagrama de bloques implementado:

El diagrama de bloques implementado para la solución fue el siguiente:

![Diagrama I2C](https://user-images.githubusercontent.com/54821299/66440357-5e041d80-e9f8-11e9-90a9-3ae4c05e0c55.jpg)

- Criterios de diseño:

Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo I2C y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

- Esquematico del circuito:

Para el esquematico del circuito decidimos utilizar la herramienta Fritzing. Las conexiónes quedaron de la siguiente manera:

![I2C](https://user-images.githubusercontent.com/54821299/66438634-e1bb0b80-e9f2-11e9-9dff-9c4a8765625c.jpg)

- Evidencias:

![I2C_evidence](https://user-images.githubusercontent.com/54821299/66445459-84cc4f00-ea0c-11e9-80d3-0fc095cb5dfc.jpg)

- Código utilizado:

Maestro:

```
import smbus
import time
bus = smbus.SMBus(1)
address = 0x04


def Leer():
	Temp = bus.read_byte(address)
return Temp

Temp = Leer()
print "La temperatura es: ", Temp

def Escribir(value):
	if(Temp > 26):
		Led = bus.write_byte(address, 1)
	if(Temp <= 26):
		Led = bus.write_byte(address, 0)
time.sleep(1)	

```

Esclavo:

```
#include <Wire.h>
#include <DallasTemperature.h>
#define address = 0x04
int Led = 3;
int stateLed = 0;
OneWire ourWire(2);
DallasTemperature sensors(&ourWire);
void setup() {
  delay(1000);
  Serial.begin(9600);
  pinMode(Led, OUTPUT)
  sensors.begin(); // Revisar 
  Wire.begin(address)
  Wire.onReceive(Leer);
  Wire.onRequest(Escribir);
  Serial.println("Ready");
}

void loop() {
  sensors.requestTemperatures();
  float Temp = sensors.getTempCByIndex(0);
  Serial.print("Temperatura= ");
  Serial.print(Temp);
  delay(100);
}

void Leer(int byteCount){
  while(Wire.available()){
    stateLed = Wire.read();
    if(stateLed == 1){
      digitalWrite(Led, HIGH);
    }
    if(stateLed == 0){
      digitalWrite(Led, LOW);
    }
  }
}

void Escribir(){
  Wire.write(Temp);
}

```

Implementación del protocolo SPI
=
SPI es un acrónimo para referirse al protocolo de comunicación serial Serial Peripherical Interface. Este protocolo nace casi a principios de 1980 cuando Motorola lo comienza a introducir y desarrollar en el primer microcontrolador derivado de la misma arquitectura del microcontrolador 680000. SPI se ha convertido es uno de los más populares protocolos para trabajar con comunicación serial debido a su velocidad de transmisión, simplicidad, funcionamiento y también gracias a que muchos dispositivos en el mercado como pantallas LCD, sensores, microcontroladores pueden trabajar con el.

Al ser uno de los protocolos seriales más conocidos, es muy importante que aprendamos su uso. Luego de haber seguido los pasos de `Configurar SPI en Raspberry PI` y `Configurar SPI en Arduino UNO` procederemos a realizar las conexiones, en este caso, encenderemos un LED conectado al Arduino UNO enviando la orden desde la Raspberry PI.

- Diagrama de bloques implementado:

El diagrama de bloques implementado para la solución fue el siguiente:

![Diagrama SPI](https://user-images.githubusercontent.com/54821299/66440346-59d80000-e9f8-11e9-8978-d4beb1342c99.jpg)

- Criterios de diseño:

Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo SPI y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

- Esquematico del circuito:

Para el esquematico del circuito decidimos utilizar la herramienta Fritzing. Las conexiónes quedaron de la siguiente manera:

![SPI](https://user-images.githubusercontent.com/54821299/66438838-7cb3e580-e9f3-11e9-9265-78c056884dbb.jpg)

- Evidencias:

![SPI_evidence](https://user-images.githubusercontent.com/54821299/66445632-07550e80-ea0d-11e9-82c3-0aaa632c3fee.jpg)

- Código utilizado:

Maestro:

```
# SPI RASPBERRY MASTER

#!/usr/bin/python

import spidev
import time
import RPi.GPIO as GPIO
import sys

CLK = 18
MISO = 23
MOSI = 24
CS = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629

# INTEGRAR LA SALIDA DE DOS BYTES
def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

while True:
    write_pot(0x00) # ENVIAR UN "0"
    print("0")
    while GPIO.input(18) == 1: # LEER EL PULSADOR
        print("1")
        write_pot(0x1FF) # ENVIAR UN "1"
    time.sleep(1)
```

Esclavo:

```
//PROTOCOLO SPI, ARDUINO COMO ESCLAVO 

#include<SPI.h>
#define LEDpin 7 // PIN DE SALIDA

volatile boolean received; // BANDERA
volatile byte Slavereceived,Slavesend; // VARIABLES PARA RECIBIR Y ENVIAR DATOS
int x=0;
void setup()
{
  Serial.begin(9600);
  pinMode(LEDpin,OUTPUT); // SALIDA AL LED              
  pinMode(MISO,OUTPUT); // CONFIGURACION DE MISO COMO SALIDA ,ENVIO DE DATOS AL MASTER 

  SPCR |= _BV(SPE); // SPI EN MODO ESCLAVO
  received = false; // BANDERA DESACTIVADA

  SPI.attachInterrupt(); // INTERRUPCIÓN COMUNICACIÓN SPI
}

ISR (SPI_STC_vect) // INTERRUPCIÓN
{
  Slavereceived = SPDR; // VALOR RECIBIDO DESDE EL MAESTRO
  received = true; //BANDERA ACTIVA 
}

void loop()
{
  if(received) // ESTADO DE LA BANDERA
  {
      digitalWrite(LEDpin,LOW); // LED APAGADO
      Serial.println("LED OFF");
      while (Slavereceived==1) // SEÑAL "1" DESDE EL MAESTRO
      {
        digitalWrite(LEDpin,HIGH); // LED ENCENDIDO
        Serial.println("LED ON");
      }
      
  Slavesend=x;                             
  SPDR = Slavesend; // ENVIAR DATOS AL MAESTRO POR SPDR 
  delay(1000);
  }
}
```

Referencias:
=


- [HetPro (2016)](https://hetpro-store.com/TUTORIALES/python-i2c-uso-y-configuracion/). Configuración I2C en Raspberry PI.
- [Arduino StackOvernet (2014)](https://arduino.stackovernet.com/es/q/5681). Configuración SPI en Arduino UNO
- [Project IoT (2019)](https://projectiot123.com/2019/01/19/spi-interface-of-raspberry-pi-using-python/). Configuración SPI Raspberry PI
- [Core Electronics (2017)](https://core-electronics.com.au/tutorials/arduino-workshop-for-beginners.html). SPI en Arduino

