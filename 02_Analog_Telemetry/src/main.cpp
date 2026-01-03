#include <Arduino.h>

// We use 'A0' because it's an Analog Input pin
const int sensorPin = A0; 

void setup() {
  // Start the serial pipe at 9600 bits per second
  Serial.begin(9600); 
  Serial.println("--- SYSTEM INITIALIZED: READING FIELD DATA ---");
}


// Added conditional logic layer to simulate a threshold which will what is normal or not normal
// similar to how a water or even a chemical tank level system needs to "scream" or alert if it hit 90%
void loop() {
int rawValue = analogRead(A0); 
  int percentage = map(rawValue, 0, 1023, 0, 100);
  
  Serial.print("LEVEL: ");
  Serial.print(percentage);
  Serial.print("%");

  // --- SAFETY LOGIC --- 
  if (percentage > 90) {
    Serial.println(" | [!] ALARM: CRITICAL HIGH LEVEL [!]");
  } else if (percentage < 10) {
    Serial.println(" | [!] ALARM: LOW FEED DETECTED [!]");
  } else {
    Serial.println(" | System Nominal");
  }

  delay(200);
}