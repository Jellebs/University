// Temperature 
#include <DHT.h> 
#define dht_apin "Skriv pin nummer her"
DHT dht(dht_apin, DHT11);

//Light
#define AL_Sensor 1

//Smoke 
#define MQ 1

//Motion
const int PIR = 47; // 

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); 
  pinMode(PIR, INPUT);
  pinMode(4, OUTPUT);
  Serial.begin(9600);

  // Temperature
  dht.begin();
  delay(4000);
}

void loop() {
  int PIR_state;
  int AL_val; 
  int MQ_val; 
  
  //motion(PIR_state);
  //lys(AL_val);
  // temperatur();
  smoke(MQ_val);
}
void motion(int PIR_state){
  PIR_state = digitalRead(PIR);
  if (PIR_state == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH); 
    delay(500); 
    digitalWrite(LED_BUILTIN, LOW);
    delay(500); 
  }
}

void lys(int AL_val){
  AL_val = analogRead(AL_val);
  Serial.print(" AL_val: ");
  Serial.println(AL_val); 
  float Lux = AL_val * 6000.0 / 1023.0;
  Serial.print(" Lux: ");
  Serial.println(Lux);
  delay(10000);
}

void smoke(int MQ_val) {
  MQ_val = analogRead(MQ_val); 
  Serial.print("MQ_Val: ");
  Serial.println(MQ_val);
  delay(1000);
}

void temperatur() {
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
