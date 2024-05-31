#include <random>
#include "DataTransferFunctions.h"
#include "WifiFunctions.h"

// 0 = Lys, 1 = Motion, 2 = Røg, 3 = Temperatur
int previousData[][2] = {
  {0, 1}, 
  {1, 0}, 
  {2, 1}, 
  {3, 24}, 
};
int key = 0;
void setup() {
  Serial.begin(921600);
  wireSetup();
  initWiFi();
  initFirebase();
}

void loop() {
  isTokenExpired(); 
  recieveData(previousData, key);
  sendData();
}

void sendData(){
  setData(previousData[key][0], previousData); 
}





