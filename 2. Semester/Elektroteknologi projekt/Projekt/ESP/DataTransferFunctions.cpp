#include <Wire.h>
#include "DataTransferFunctions.h"

// Defines Slave Address
const int SLAVE_ADDR = 9; 
// Defines Size of Answer in bytes.
// 1 byte key 256 mulige keys, 2 byte value 65.532 mulige værdier. 
const int ANSWERSIZE = 3; 

// Initializes I2C communication as Master
void wireSetup() {
  Wire.begin(); 
  Serial.begin(9600);
}

void recieveData(int data[][2], int key) {
  // Request 3 byte answer from slave.
  Wire.requestFrom(SLAVE_ADDR, ANSWERSIZE); 
  int value = 0; 
  int i = 0; 
  int increasement;
  while (Wire.available()) {
    byte c = Wire.read(); 
    Serial.print("c: "); Serial.println(c);
    switch (i) {
      case 0: 
        key = int((unsigned char)(c)); 
        break; 
      case 1: 
        if (int((unsigned char)(c) == 0)) { break; }
        value = int((unsigned char)(c) << 8); // Hvis 11111111 og den ikke er LSB, må det da betyde, at den skal flyttes med 8 bits. I stedet for 256, bliver den 65532. 256 * (2^(n shifts)). 256 * (2^8) == 65532
        break; 
      case 2:
        value += int((unsigned char)(c));
        break; 
    }
    i++; 
    if (i == 3) { 
      i = 0;  
    }
  }
  Serial.println("");
  Serial.print("Key: "); Serial.println(key); 
  Serial.print("Value: "); Serial.println(value);
  data[key][1] = value; 
  delay(10000);
}








