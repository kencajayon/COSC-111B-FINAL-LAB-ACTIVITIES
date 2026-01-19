const int BUTTON_PIN = 2;
const String GROUP_NUMBER = "Group_4"; 

int lastButtonState = HIGH; 
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP); 
  Serial.begin(9600);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    static int confirmedButtonState = HIGH;
    
    if (reading == LOW && confirmedButtonState == HIGH) {
      Serial.println(GROUP_NUMBER);
    }
    confirmedButtonState = reading;
  }

  lastButtonState = reading;
}