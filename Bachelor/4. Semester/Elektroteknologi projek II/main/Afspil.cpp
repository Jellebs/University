#include <Arduino.h>
const int pinnumre[4] = {A1, A2, A3, A4};

void afspil_Lyd(int frekvenser[4], int laengde) {
  for (int i = 0; i<4; i++) {
    tone(pinnumre[i], frekvenser[i], 0);
  }
  delay(laengde); 
  for (int i = 0; i<4; i++) {
    noTone(pinnumre[i]); 
  }
}