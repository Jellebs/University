#include "Sensors.h"
#include "Input.h"
#include "Display.h"
#include "DataTransferFunctions.h"

int previousData[][2] = {
  {0, 1}, 
  {1, 0},
  {2, 1},
  {3, 24}, 
  {4, 20}
};
int i = 0; 

void setup() {
  Serial.begin(9600);
  wireSetup(requestEvent);
}

void requestEvent() { 
  const int ANSWERSIZE = 3;
  byte response[ANSWERSIZE]; 
  intTilBytes(i, previousData[i][1], response);
  i++; 
  Serial.print("Byte as response: ");
  for (int j = 0; j < 3; j++) {
    print(response[j]); 
  }
  Serial.println("");
  if (i > 4) { i = 0; }
  writeData(response); // Tager en byte array af størrelsen ANSWERSIZE. 
}

void loop() {
  // put your main code here, to run repeatedly:

}
