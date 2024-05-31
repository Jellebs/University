#include <Arduino.h>
#include <Wire.h>
#include <SparkFun_BMI270_Arduino_Library.h>
#include "Modtag.h"

// #include <Keyboard.h>

const int ROW = 4; // rows
const int COL = 3; // col

char keys[ROW][COL] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

void modtag_PitchOpsaetning(){
  for (int k = 16; k < 20; k++) {
    PORT->Group[PORTA].DIR.reg |= 1 << k; // Set PAk as an output
  }
  for (int l = 11; l < 14; l++) {
    PORT->Group[PORTB].DIR.reg &= ~(1 << l); // Sæt PBl til input
    PORT->Group[PORTB].PINCFG[l].reg = 0b00000110; // Aktiver pull resistor og input buffer for PBl
    PORT->Group[PORTB].OUTCLR.reg |= 1 << l; // Sæt pull resistor til at pulldown for PBl
  }
  Serial.begin(9600);
}

void modtag_Knapper(int trykstreng[4]) {
  bool buttonPressed = false;
  for (int i = 16; i < 20; i++) {
    PORT->Group[PORTA].OUTSET.reg |= 1 << i; // Set logic high on PAi
    delay(5); // Delay
    for (int j = 11; j < 14; j++) {
      if (PORT->Group[PORTB].IN.reg & (1 << j)) {
        delay(50);
        int row = i - 16; // find row
        int col = j - 11; // find col
        char key = keys[row][col];
        PORT->Group[PORTA].OUTCLR.reg |= 1 << i; // Toggle tilbage til low
        if (key >= '1' && key <= '9') {
          trykstreng[row] = key - '0'; // konverter char til int 
          // Serial.println(trykstreng[row]);
    }   else if (key == '*') {
          trykstreng[row] = 10; // sæt en int værdi for '*'
          // Serial.println(trykstreng[row]);
    }   else if (key == '0') {
          trykstreng[row] = 11; // sæt en int værdi for '#'
          // Serial.println(trykstreng[row]);
    }   else if (key == '#') {
          trykstreng[row] = 12; // sæt en int værdi for '#'
          // Serial.println(trykstreng[row]);
    }
        buttonPressed = true; // Set flag to true if any button is pressed
        delay (100);      
      }
    }
    PORT->Group[PORTA].OUTCLR.reg |= 1 << i; // Toggle back to low
  }

  if (!buttonPressed) {
   trykstreng[0] = 13;
   trykstreng[1] = 14;
   trykstreng[2] = 15;
   trykstreng[3] = 16;
  }
  
  delay(50);
}







// Accelerometer
BMI270 imu;

// I2C address selection
uint8_t i2cAddress = BMI2_I2C_PRIM_ADDR; // 0x68
// uint8_t i2cAddress = BMI2_I2C_SEC_ADDR; // 0x69


void modtag_AccelerometerOpsaetning() {
  Serial.println("Til sidst her");
  
  Serial.begin(115200);
  Wire.begin();
  Serial.println("Nu er jeg her");
  // Check if sensor is connected and initialize
  // Address is optional (defaults to 0x14)
  while(imu.beginI2C(i2cAddress) != BMI2_OK) {
    // Not connected, inform user
    Serial.println("ikke connected");
    // Wait a bit to see if connection is established
    delay(1000);
  }
  Serial.println("Nu her");
  Serial.println("BMA400 connected!");
}

float modtag_Zdata() {
  imu.getSensorData();
  delay(20);
  return imu.data.accelZ;
}

