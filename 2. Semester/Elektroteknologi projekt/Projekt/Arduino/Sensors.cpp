#include "Sensors.h"
#include <DHT.h>

#define AL_Sensor 1                       // Lys

const int PIR = 3;                        // Bevægelse

#define dht_apin "Skriv pin nummer her"   // Temperatur og fugtighed
DHT dht(dht_apin, DHT11);

#define MQ 1                              // Røg
int buzzer = "Skriv pin nummer her";      // Buzzer


int lys() {
  int graensevaerdi; graensevaerdi = 300; // Er lyset over grænseværdien? 
  int AL_val; AL_val = analogRead(AL_val);
  float Lux = AL_val * 6000.0 / 1023.0;
  if (Lux >= graensevaerdi) { 
    return 1;
  } else {
    return 0;
  }
}

int motion() {
  int PIR_state;
  return digitalRead(PIR);
}

void dht_styring() {
  float t; t = dht.readTemperature(); 
  delay(300);
  float h; h = dht.readHumidity();
  delay(300); 
  if (t > 30) { 
    // case 1
    /* if (h < threshold) { 
        Water_plants()
      } */ 
  } else if (t > 0 && t < 30) {
    // case 2
    /* if (h < threshold) { 
      Water_plants()
    } */  
  } else {
    /* if (h < threshold) { 
      Water_plants()
    } */
  }
}

int smokeDetector() {
  int MQ_val; MQ_val = analogRead(MQ_val); 
  int threshold; threshold = 30;
  if (MQ_val > threshold) { return 1; }
  else { return 0; }
}