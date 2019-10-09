#include <Wire.h> //Librería I2C
#define direccion1 = 0x38 //Definimos la dirección I2C
int LED2 = 13;
void setup() {
  pinMode(LED13, OUTPUT);
  Wire.begin(); //Inicializamos la comunicación I2C
  Serial.begin(9600);
}

void loop() {
  byte cual;
  cual = Leer(direccion1); //Leemos la dirección
  if(bitRead(cual,0)) //leemos el bit recibido por I2C
    digitalWrite(LED13, LOW);
  else
    digitalWrite(LED13, HIGH);

  delay(100);
}

byte Leer(int direccion) {
  byte LeeDato = 0xff; //Creamos la función leer para identificar los datos recibidos
  Wire.requestFrom(direccion,1);
  if(Wire.available()){
    LeeDato = Wire.read();
  }
  return LeeDato;
}
