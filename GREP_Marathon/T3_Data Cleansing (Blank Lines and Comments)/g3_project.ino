// Arduino LED Blink
void setup() {
  pinMode(13, OUTPUT); // Set pin 13 as output
}



// Main loop
void loop() {
  digitalWrite(13, HIGH);
  delay(1000);          
  
  digitalWrite(13, LOW);
  delay(1000);
}
# Config end
