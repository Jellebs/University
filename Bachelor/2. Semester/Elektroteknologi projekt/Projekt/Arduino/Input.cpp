#include "Input.h"
#include <Keypad.h>

const byte ROWS = 4; 
const byte COLS = 3; 
byte rowPins[ROWS] = {10, 11, 12, 13}; 
byte colPins[COLS] = {7, 8, 9}; 
char keys[ROWS][COLS] = {
  {'1', '2', '3'}, 
  {'4', '5', '6'}, 
  {'7', '8', '9'},
  {'*', '0', '#'}  
};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void input_keypad(bool default_option, char key) { // Detektor hvilken knap man trykker på, default så er man i menuen, ellers er man i en mode.
  char k = keypad.getKey();  
  if (default_option == false) {
    if (k == '0') {
      key = k; 
    }
  } 
  else {
    if (k != NULL) {
      key = k;
      Serial.println(key);
    }
  }
}