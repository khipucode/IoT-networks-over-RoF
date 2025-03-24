//Este código estabelece uma ponte de comunicação serial entre a Raspberry Pi e um módulo XBee usando um Arduino. 
//Ele utiliza a biblioteca SoftwareSerial para se comunicar com o XBee pelos pinos 2 (RX) e 3 (TX). 
//Dados recebidos da Raspberry Pi via USB são enviados ao XBee. Dados recebidos do XBee são enviados de volta à Raspberry Pi. 
//Funciona como um repetidor serial bidirecional.

#include <SoftwareSerial.h>

// Definir os pinos para a comunicação com o XBee
SoftwareSerial xbeeSerial(2, 3); // RX no pino 2, TX no pino 3

void setup() {
  Serial.begin(9600);     // Comunicação com a Raspberry Pi (USB)
  xbeeSerial.begin(9600); // Comunicação com o XBee (UART)
}

void loop() {
  if (Serial.available()) {  // Se houver dados vindos da Raspberry Pi
    char c = Serial.read();
    xbeeSerial.write(c);  // Enviar para o XBee
  }

  if (xbeeSerial.available()) { // Se houver dados vindos do XBee
    char c = xbeeSerial.read();
    Serial.write(c);  // Enviar para a Raspberry Pi
  }
}



