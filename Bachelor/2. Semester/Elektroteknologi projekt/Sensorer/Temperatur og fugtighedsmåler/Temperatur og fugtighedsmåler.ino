#include <DHT.h> 

#define dht_apin "Skriv pin nummer her"
DHT dht(dht_apin, DHT11);


void setup() {
  Serial.begin(9600);
  
}

void loop() {
  Serial.print("\nTemperature:");
  float t = dht.readTemperature();
  delay(300);
  Serial.print(t);
  Serial.print(" Humidity:"); 
  float h=dht.readHumidity();
  delay(300);
  Serial.print(h);
  delay(2000);
}
