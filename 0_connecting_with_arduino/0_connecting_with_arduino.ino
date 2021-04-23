
int LED = 13;                   // Activate built-in LED
char dataFrompython;            // Variable for Data recived from python

void setup() {
  Serial.begin(9600);    // ARDUINO BAUD RATE
  pinMode(LED,OUTPUT);   // LED PIN 
  }

void loop() {
  if (Serial.available() > 0){
    dataFrompython =  Serial.read();
    if (dataFrompython == '1'){
       Serial.print("LED ON");
       digitalWrite(LED, HIGH);
    }
    if (dataFrompython == '2'){
       Serial.print("LED OFF");
       digitalWrite(LED, LOW);
    }
  }

}
