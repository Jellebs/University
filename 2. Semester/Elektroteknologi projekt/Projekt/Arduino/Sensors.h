#ifndef SENSORS_H 
#define SENSORS_H
#include <arduino.h>

int lys();
int motion();
int vandKontrol(); 
int smokeDetector(); 
void sensorSetup(); 
void koerSensorer(int previousData[0][2], bool dataChanged); 

#endif