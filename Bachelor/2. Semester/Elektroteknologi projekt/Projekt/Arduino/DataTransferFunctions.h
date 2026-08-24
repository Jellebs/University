#ifndef DATATRANSFERFUNCTIONS_H
#define DATATRANSFERFUNCTIONS_H
#include <Arduino.h>

void wireSetup(void requestEvent());
void intTilBytes(int key, int vaerdi, byte byteArray[]);
void print(unsigned char byte);
void writeData(byte response[3]);
#endif
