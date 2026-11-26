const int LDR_PIN = A0;      
const int LED_PIN = 9;       
const int PORIH = 500;       

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int svitlo = analogRead(LDR_PIN); 

  Serial.print("Light = ");
  Serial.println(svitlo);

  if (svitlo < PORIH) {
    digitalWrite(LED_PIN, HIGH); 
  } else {
    digitalWrite(LED_PIN, LOW);  
  }

  delay(200);
}
