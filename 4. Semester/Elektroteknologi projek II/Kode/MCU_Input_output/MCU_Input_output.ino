void setup() { 
  hex PA06 = 0x40; // Hex(PA06 = 2^6)
  // PA06 har åbenbart nummeret 0x40 i hexa
  PORT->Group[PORTA].DIR.reg = 0x40; // Sætter PA06 til at være 1, output. 

  
  // Få LED til at blinke
  // Konfigureringen af frekvensen skal være vha. registre. 
  // Hvilke konfigurationer er hvilke i registret? 
  // Fra eksemplet 0x40 -> 000010110001000000000000000000000000 hvor 4 er outputs. Så PA06 må være indeks 5, 7, 8 eller 12. 
  PORT->Group[PORTA].DIR.reg = 0x40; // Sætter PA06 til at være 1, output. 





  //          3. 
  // Få LED til at blinke
  // CPUen's frekvens er 120Mhz 
  // Den ønskede blinken er 5Hz

  // En prescale faktor skal åbenbart køres på
  // Så skal compare counter registeret sættes til 120Mhz/(prescale * 5Hz) - 1 = 23436 for prescale på Samd51 på 1024
  unsigned long cycles = 5B8C; // 23436 ->Hex = 5B8C

  // Det nye register der aktiveres er nu GPIO PA12.   2^12 = 4096 = 0x1000
  PORT->Group[PORTA].DIR.reg |= 0x1000;
  TC3->COUNT16.CC[0].reg = cycles;
  // Med interrupt kode i loopen vil det måske virke. 

}

void loop() {
  // put your main code here, to run repeatedly:
  PORT->Group[PORTA].OUTTGL.reg = 0x40; // Loop kode. I stedet for at sætte PA06 koden til at være 1, så toggler den mellem 0 & 1. 
  delay(100);

  while (Serial.available()) {
    char rxByte = (char)Serial.read(); // Data klar til at indlæses som characters 
    rxByteArray[idxArray++] = rxByte; 
    if (rxByte == "\n") { // Ny linje på data
      rxByteArray[idxArray] = NULL;
      Serial.print("Received data >> "); 
      Serial.print(rxByteArray);
      idxArray = 0; // Starter forfra med nyt data
    }
  }


  // Få LED til at blinke



  //          3. 
  // Få LED til at blinke
  PORT->Group[PORTA].OUTTGL.reg = 0x1000;

}

