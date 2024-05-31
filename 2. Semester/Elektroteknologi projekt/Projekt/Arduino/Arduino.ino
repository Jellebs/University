#include "Sensors.h"
#include "Input.h"
#include "Display.h"
#include "DataTransferFunctions.h"

// 0 = Lys, 1 = Motion, 2 = Røg, 3 = Vandkontrol
int previousData[][2] = {
  {0, 1},   
  {1, 0},
  {2, 1},
  {3, 24}, 
};
int i = 0; 
bool changeInData = false; 

void setup() {
  Serial.begin(9600);
  wireSetup(requestEvent);
  sensorSetup();
}

void requestEvent() { 
  // if (changeInData == false) { return; } 
  const int ANSWERSIZE = 3;
  byte response[ANSWERSIZE]; 
  intTilBytes(i, previousData[i][1], response);
  i++; 
  Serial.print("Byte as response: ");
  for (int j = 0; j < 3; j++) {
    print(response[j]); 
  }
  Serial.println("");
  if (i > 3) { i = 0; }
  writeData(response); // Tager en byte array af størrelsen ANSWERSIZE. 
}

void loop() { 
  koerSensorer(previousData, changeInData); 
  // put your main code here, to run repeatedly:
}

