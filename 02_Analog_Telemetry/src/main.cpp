#include <Arduino.h>

const int SENSOR_PIN = A0;
const int LED_NORMAL = 12; // Green
const int LED_ALARM = 11;  // Red
const int THRESHOLD = 920; // 90% mark

void setup() {
    pinMode(LED_NORMAL, OUTPUT);
    pinMode(LED_ALARM, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int val = analogRead(SENSOR_PIN);
    
    if (val >= THRESHOLD) {
        digitalWrite(LED_ALARM, HIGH);
        digitalWrite(LED_NORMAL, LOW);
        Serial.println("!!! CRITICAL THRESHOLD REACHED !!!");
    } else {
        digitalWrite(LED_ALARM, LOW);
        digitalWrite(LED_NORMAL, HIGH);
    }
    delay(50); 
}