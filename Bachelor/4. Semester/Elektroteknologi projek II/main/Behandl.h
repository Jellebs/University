#ifndef BEHANDL_H
#define BEHANDL_H

#include <Arduino.h>


void behandl_Pitches(int pitches[4], int trykkedeStrenge[4]);
int __vaelgPitch(int tryktStreng);
void behandl_Debug(int trykkedeStrenge[4], int pitches[4], float acceleration);
#endif
