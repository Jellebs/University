#include "Display.h"
#include <LiquidCrystal.h>

LiquidCrystal lcd(51, 50, 49, 48, 47, 46); // Rs, Enabler, d4, d5, d6, d7

void chooseDisplay(char inputState) {
  switch (inputState) {
    case '0':
      // menu();
      break; 
    case '*':
      // lys();
      break;
    case '#': 
      // motion();
      break;  
    default:  
      // menu();
      break;
  }
  // delay(tickRate);
}

void menu() {
  lcd.begin(16,2); // Coloumns, Rows 
  lcd.setCursor(5, 0); 
  lcd.print("Menu"); 
  lcd.setCursor(0,1); 
  lcd.print("*: x"); 
  lcd.setCursor(12, 1);
  lcd.print("#: y");
  // input_keypad(true);
}

void createDisplay(char mode[], char navn[], float vaerdi){ // standard for sensor display
  lcd.setCursor(1, 0); 
  lcd.print(mode);
  lcd.setCursor(10, 0); 
  lcd.print("esc: 0");
  lcd.setCursor(1, 1); 
  lcd.print(navn);
  lcd.print(" ");
  lcd.print(vaerdi);
  // input_keypad(false);
}