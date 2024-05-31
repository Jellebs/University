#include "Behandl.h"
#include "Modtag.h"
#include "Afspil.h"

int trykkedeStrenge[4] = {2, 4, 15, 11};
int pitches[4] = {400, 200, 100, 300};
int frekvens = 1400; 
float acceleration = 5;
int interval = 1; 
const int pinnumre[4] = {A1, A2, A3, A4};

void setup() {
  // put your setup code here, to run once:
  modtag_PitchOpsaetning();
  modtag_AccelerometerOpsaetning(); 
}


void loop() {
  modtag_Knapper(trykkedeStrenge); 
  behandl_Pitches(pitches, trykkedeStrenge);
  
  acceleration = modtag_Zdata();

  if (abs(acceleration) > 2) {
    afspil_Lyd(pitches, 1000); 
    behandl_Debug(trykkedeStrenge, pitches, acceleration);
  }
}
