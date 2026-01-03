#include <Arduino.h>

void setup() {
  // Start the "Telephone line" to the Mac at 9600 baud
  Serial.begin(9600); 
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.println("--- HYBRID LINK ONLINE ---");
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); 
  Serial.println("SIGNAL: HIGH (5V)");
  delay(1000); 
  
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("SIGNAL: LOW  (0V)");
  delay(1000);
}