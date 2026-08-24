#include <WiFiMulti.h>
#include <Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"
#include "WifiFunctions.h"

#define WIFI_SSID "Laptop"
#define WIFI_PASSWORD "testtest"
#define API_KEY "AIzaSyDaydxHp5fgtEBNIE2IJ3wRKWq3To11sww"
#define DATABASE_URL "https://intelligent-home-control-default-rtdb.europe-west1.firebasedatabase.app/"

// Arduino user informations
#define USER_EMAIL "au689481@au.uni.dk"
#define USER_PASSWORD "12345678"

unsigned long sendDataPrevMillis = 0; 
bool signupOK = false; 
int ldrData = 0; 
float voltage = 0.0; 

FirebaseData fbdo; 
FirebaseAuth auth; 
FirebaseConfig config;

WiFiMulti wifiMulti; 

// Init WIFI
void initWiFi() {
  if (wifiMulti.run() == WL_CONNECTED) { Serial.println("Connection already established"); return; } 
  
  // Hvis ingen forbindelse, fortsæt:
  Serial.print("Connecting");
  wifiMulti.addAP(WIFI_SSID, WIFI_PASSWORD); 
  int i = 0; 
  while (wifiMulti.run() != WL_CONNECTED) {
    Serial.print("."); delay(500); 
    if (i == 25){
      Serial.println(""); 
      Serial.print("Timed out trying to connect to the network");
      break;
    }
    i++;
  }
  if (i == 25) { return; } // Timed out
  Serial.println("Connected");
}

void initFirebase() {
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  // Authentication
  auth.user.email = USER_EMAIL; 
  auth.user.password = USER_PASSWORD;

  Firebase.reconnectWiFi(true); 
  fbdo.setResponseSize(4096); 

  config.token_status_callback = tokenStatusCallback;
  config.max_token_generation_retry = 5; 

  // init firebase
  Firebase.begin(&config, &auth);
}

//                              Upload data                             //
void setData(int key, int previousData[][2]){
  if (Firebase.ready() != true && (millis() - sendDataPrevMillis > 15000 || sendDataPrevMillis == 0) != true){ return; }
  sendDataPrevMillis = millis();
  if (Firebase.RTDB.setInt(&fbdo, key, previousData[key][1])) {
    Serial.println("Succesfully set int data");
  } else {
    Serial.println("Failed to set data with reason: " + fbdo.errorReason());
  }
  delay(300);
}

void isTokenExpired() {
  if (Firebase.isTokenExpired()){
    Firebase.refreshToken(&config);
    Serial.println("Refresh token");
    delay(5000);
  }
}