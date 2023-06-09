//LCD 
#include <LiquidCrystal.h> 
LiquidCrystal lcd(12, 11, 10, 9, 8, 7); 

// Temperatur
#include <DHT.h> 
#define dht_apin 6
DHT dht(dht_apin, DHT11);

// Light 
#define AL_Sensor 1 

// Keypad 
#include <Keypad.h>
const byte ROWS = 4; 
const byte COLS = 3; 
byte rowPins[ROWS] = {28, 30, 32, 34}; 
byte colPins[COLS] = {22, 24, 26}; 
char keys[ROWS][COLS] = {
  {'1', '2', '3'}, 
  {'4', '5', '6'}, 
  {'7', '8', '9'},
  {'*', '0', '#'}  
};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Hello World
//int s = 0, m = 0; // seconds and minutes. 


void setup() {
  lcd.begin(16,2); 
  Serial.begin(9600); // Bruges også til keypad
  // put your setup code here, to run once:
}

void loop() {
  menu();
}

void menu() {
  char key = keypad.getKey(); 
  lcd.setCursor(1,0); 
  lcd.print("Selection mode");
  lcd.setCursor(1,1); 
  lcd.print("*: Temp #Light");
  
  if (key == '*') {
    temperature();
    lcd.clear();
  } else if (key == '#') {
    light();
    lcd.clear();
  } 
}

void temperature() {
  lcd.setCursor(1,0);
  lcd.print("Temp mode 0: esc");
  lcd.setCursor(2,1);
  lcd.print("Temp: ");
  float t = dht.readTemperature(); 
  delay(300);
  lcd.print(t);
}
void light() {
  int AL_val = analogRead(AL_val);
  lcd.setCursor(1,0);
  lcd.print("Light mode 0: esc");
  lcd.setCursor(2,1);
  lcd.print("Light: ");
  float lux = AL_val * 6000.0 / 1023.0;
  delay(300);
  lcd.print(lux);
}
void helloWorld();
// HelloWorld();
  /* HELLO WORLD
  lcd.setCursor(2,0); 
  lcd.print("Hello World"); 
  lcd.setCursor(6,1); 
  lcd.print(m);
  lcd.print(": "); 
  lcd.print(s);
  s++;
  delay(1000); 
  if (s == 60) {
    s= 0; 
    m++;
    lcd.clear();
  }
  */ 
  // put your main code here, to run repeatedly:
