#ifndef WIFIFUNCTIONS_H
#define WIFIFUNCTIONS_H
#include <Arduino.h>

void initWiFi();
void initFirebase();
void setData(int key, int previousData[][2]);
void isTokenExpired();

#endif 