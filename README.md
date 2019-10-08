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

![Tabla](https://raw.githubusercontent.com/Andres-04/RSP_I2C_SPI/master/Imagen1.png?token=ANCIDM3GPGLMPSHRCFHR3KS5TSWGO)

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
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

- Diagrama de bloques implementado:
Imagen

- Criterios de diseño
Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo I2C y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

- Esquematico del circuito
Imagen

- Código utilizado
Maestro:
Codigoooooo
Esclavo:
Codigoooooo

Implementación del protocolo SPI
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

- Diagrama de bloques implementado:
Imagen

- Criterios de diseño
Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo I2C y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

- Esquematico del circuito
Imagen

- Código utilizado
Maestro:
Codigoooooo
Esclavo:
Codigoooooo



https://hetpro-store.com/TUTORIALES/python-i2c-uso-y-configuracion/
https://arduino.stackovernet.com/es/q/5681 - Para SPI
https://projectiot123.com/2019/01/19/spi-interface-of-raspberry-pi-using-python/ SPI RSP
https://core-electronics.com.au/tutorials/arduino-workshop-for-beginners.html SPI Arduino
