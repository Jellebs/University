#include "Sensors.h"
#include <DHT.h>

#define AL_Sensor A2                      // Lys # A2

const int PIR = 13;                        // Bevægelse #D13

int moistureSensor = A3;                   // Soil moisture sensor # A3
bool moistureFlag = false;  

#define MQ A1                              // Røg # A1

bool dataHasChanged = false; 

int lys() {
  int graensevaerdi; graensevaerdi = 300; // Er lyset over grænseværdien? 
  int AL_val; AL_val = analogRead(AL_val);
  float Lux = AL_val * 6000.0 / 1023.0;
  if (Lux >= graensevaerdi) { 
    dataHasChanged = true;    
    return 1;
  } else {
    dataHasChanged = true;
    return 0;
  }
}

int motion() {
  return digitalRead(PIR); 
}

int vandKontrol() {
  int moistureValue = analogRead(moistureSensor); 
  if ( (moistureValue >= 500 ) && ( moistureFlag == false) ) {  // Der mangler vand
    moistureFlag = true;
    dataHasChanged = true;
    return 1;
  } else { // Der mangler ikke vand
    moistureFlag = false;
    dataHasChanged = true;
    return 0;
  }
}

int smokeDetector() {
  int MQ_val; MQ_val = analogRead(MQ); 
  int threshold; threshold = 30;
  if (MQ_val > threshold) { dataHasChanged = true; return 1;}
  else { dataHasChanged = true; return 0;}
}

void sensorSetup(){
  pinMode(moistureSensor, INPUT);
}

void koerSensorer(int previousData[0][2], bool dataChanged) {
  // 0 = Lys, 1 = Motion, 2 = Røg, 3 = Vandkontrol  
  previousData[0][2] = lys();
  previousData[1][1] = motion();
  previousData[2][1] = smokeDetector();
  previousData[3][1] = vandKontrol();
  if (dataHasChanged) {     // The data has been set
    dataChanged = true;     // Pointer
    dataHasChanged = false; // Reset 
  }
}
