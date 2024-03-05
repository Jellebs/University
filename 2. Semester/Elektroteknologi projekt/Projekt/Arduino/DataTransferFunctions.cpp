#include "DataTransferFunctions.h"
#include <Wire.h>

void wireSetup(void requestEvent()) {
  const int SLAVE_ADDR = 9;
  Wire.begin(SLAVE_ADDR);
  Wire.onRequest(requestEvent);
}

void intTilBytes(int key, int vaerdi, byte byteArray[]){
  int tmp=vaerdi;
  int tmpKey = key;
  Serial.print("tmpKey: "); Serial.println(tmpKey);
  Serial.print("tmp: "); Serial.println(tmp);
  byteArray[0] = (tmpKey & 0xFF);
  
  for(int i = 2;i > 0; i--) {
    byteArray[i] = (tmp & 0xFF); 
    tmp=tmp>>8;
  }
  
}

void print(unsigned char byte) {
  for (int i = 7; i >= 0; i--) {
    int b = byte >> i;
    if (b & 1)
        Serial.print("1");
    else
        Serial.print("0");
}
}
void writeData(byte response[3]) { Wire.write(response, sizeof(response)); }