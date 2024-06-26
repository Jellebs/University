#include "Behandl.h"
#include "Noder.h"
using namespace std; 

void behandl_Pitches(int pitches[4], int trykkedeStrenge[4]) {
  for (int i = 0; i < 4; i++) {
    pitches[i] = __vaelgPitch(trykkedeStrenge[i]);
  }
}

int __vaelgPitch(int tryktStreng){ // Raekke-Kolonne (43) 4 række 3 kolonne
    switch(tryktStreng){
        // Åbne strenge
        case 13: 
            return NOTE_A3;
        case 14: 
            return NOTE_E4;
        case 15:
            return NOTE_C4; 
        case 16: 
            return NOTE_G4; 
        
        // Trykket strenge 
        // Foerste række
        case 1: 
            return NOTE_AS3; 
        case 2: 
            return NOTE_B3; 
        case 3: 
            return NOTE_C4; 
        
        // Anden række
        case 4: 
            return NOTE_F4; 
        case 5: 
            return NOTE_FS4; 
        case 6: 
            return NOTE_G4;

        // Tredje række
        case 7: 
            return NOTE_CS4; 
        case 8: 
            return NOTE_D4; 
        case 9: 
            return NOTE_DS4;

        // Fjerde række.
        case 10:
            return NOTE_GS4; 
        case 11: 
            return NOTE_A4; 
        case 12:
            return NOTE_AS4; 
        
        default:
            return 0; 
    }
}
void behandl_Debug(int trykkedeStrenge[4], int pitches[4], float acceleration) {
  // Knapper
  Serial.print("[");
  for (int i = 0; i < 4; i++) {
    Serial.print(trykkedeStrenge[i]);
    if (i < 3) {
      Serial.print(",");
    }
  }
  Serial.print("]\n");
  Serial.print("[");
  for (int i = 0; i < 4; i++) {
    Serial.print(pitches[i]);
    if (i < 3) {
      Serial.print(",");
    }
  }
  Serial.print("]\n");
  Serial.println(acceleration);
  Serial.print("\n\n");
}


