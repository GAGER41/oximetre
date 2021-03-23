// Constantes (pins et variables):
const int OX2 =  10;
const int OX3 =  11;


void setup() {
  // Initialisation des pins:
  pinMode(OX2, OUTPUT);
  pinMode(OX3, OUTPUT);
}


void loop() {
  // Infrarouge:
  analogWrite(OX2, 255); // Allumer
  delay(2000);
  analogWrite(OX2, 0);  // Éteindre la LED
  
  // Rouge:
  analogWrite(OX3, 255); // Allumer
  delay(2000);
  analogWrite(OX3, 0);  // Éteindre la LED
}
