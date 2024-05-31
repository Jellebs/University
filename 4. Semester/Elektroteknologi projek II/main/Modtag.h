#ifndef MODTAG_H
#define MODTAG_H

#include <Arduino.h>
#include <Wire.h>
#include <SparkFun_BMI270_Arduino_Library.h>

void modtag_PitchOpsaetning();
void modtag_Knapper(int trykstreng[4]);
void modtag_AccelerometerOpsaetning();
float modtag_Zdata();

#endif