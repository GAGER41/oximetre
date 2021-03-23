#include <Calculus.h>
#include <Filters.h>
# include <math.h>
# include <FreqMeasure.h>


// Constantes (pins et variables):
const int OX2 =  10;
const int OX3 =  11;
const int FREQ = 8;
const int PHOT = A0;
// photodiode =  A0 et 5, signal doit rentrer dans les deux pins
float e_r = 0.81;
float e_ir = 0.18;
float eo2_r = 0.08;
float eo2_ir = 0.29;
float ratio;
float oxyg;
float myArray[2000];



void setup() {
  Serial.begin(9600);
  FreqMeasure.begin();
  // Initialisation des pins:
  pinMode(OX2, OUTPUT);
  pinMode(OX3, OUTPUT);
  pinMode(FREQ, INPUT);
}


void loop() {
  // Modulation des LEDs et mesures des signaux max et min:
  float ir_min = 0;
  float ir_max = 0;
  float r_min = 0;
  float r_max = 0;
  
  // Infrarouge:
  analogWrite(OX2, 255); // 85 parce que c'est le tiers du cycle, pwm... non finalement
  delay(100);
  int var = 0;
  while (var < 20000) {
    if (analogRead(PHOT) > ir_max) {
      ir_max = PHOT;
    }

    else if (analogRead(PHOT) < ir_min) {
      ir_min = PHOT;
    }
    var++;
  }
  delay(100);
  analogWrite(OX2, 0);  // Éteindre la LED
  
  // Rouge:
  analogWrite(OX3, 255); // 85 parce que c'est le tiers du cycle, pwm...
  delay(100);
  var = 0;
  while (var < 20000) {
    if (analogRead(PHOT) > r_max) {
      r_max = PHOT;
    }

    else if (analogRead(PHOT) < r_min) {
      r_min = PHOT;
    }
    var++;
  }
  Serial.print("max et min : ");
  Serial.println(r_max);
  Serial.println(r_min);
  Serial.println(ir_max);
  Serial.println(ir_min);
  delay(500);
  // Taux d'oxygénation:
  ratio = (log(r_min/r_max))/(log(ir_min/ir_max));
  oxyg = (e_r-(e_ir*ratio))/(e_r-eo2_r+(eo2_ir-e_ir)*ratio);
  
  Serial.print("Taux d'oxygenation = ");
  Serial.print(oxyg);
  Serial.println(" %");
  delay(500);
  
  // Mesure du pouls:
  if (FreqMeasure.available()) {
    unsigned long count = FreqMeasure.read();
    float freq = FreqMeasure.countToFrequency(count);
    FreqMeasure.end();

    freq = freq * 60; // parce qu'on veut des bpm

    Serial.print("Pouls = ");
    Serial.print(freq); 
    Serial.println(" bpm");
  }
    
  analogWrite(OX3, 0);  // Éteindre la LED
}
