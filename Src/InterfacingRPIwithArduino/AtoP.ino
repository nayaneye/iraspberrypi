const int ledPin = 13;

void setup()
{ pinMode(ledPin, OUTPUT); 
    Serial.begin(9600); 
}

void loop()
{ 
    if (Serial.available()) { 
        blink(Serial.read() - '0'); // convert the character '1'-'9' to decimal 1-9 
    } 
    delay(500); 
}

void blink(int numberOfTimes){

    for (int i = 0; i < numberOfTimes; i++) { 
        digitalWrite(ledPin, HIGH); 
        delay(100); 
        digitalWrite(ledPin, LOW); 
        delay(100); 
    } 
}
