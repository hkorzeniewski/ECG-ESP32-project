#include <Arduino.h>
#include "WiFi.h" // ESP32 WiFi include
//#include "WiFiConfig.h" // My WiFi configuration.

const int heartPin = 32;

const char *ssid = "2.4G-Vectra-WiFi-91370A";
const char *password = "ng7vh344w4zh0q17";

const uint16_t port = 8090;
const char * host = "192.168.0.27";

WiFiClient client;


void setup() {
    disableCore0WDT();
    Serial.begin(115200);
    delay(5);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.println("...");
    }
   
    Serial.print("WiFi connected with IP: ");
    Serial.println(WiFi.localIP());
 
}


void loop() {
//    int heartValue = analogRead(heartPin);
//    Serial.println(heartValue);
//    for (int i = 0;i<10;i++){
//       int heartValue = analogRead(heartPin);
//       arr[i] = heartValue;
//       delay(10);
//    }
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
        delay(500);
        return;
    }

//    int heartValue = analogRead(heartPin);
    client.print(readVoltage(heartPin));
    Serial.println(readVoltage(heartPin));
    delay(4); 

    

   client.stop();
   
}

float readVoltage(byte pin){
   float reading = analogRead(pin); // Reference voltage is 3v3 so maximum reading is 3v3 = 4095 in range 0 to 4095
   if(reading < 1 || reading > 4095) return 0;
   // return -0.000000000009824 * pow(reading,3) + 0.000000016557283 * pow(reading,2) + 0.000854596860691 * reading + 0.065440348345433;
   return -0.000000000000016 * pow(reading,4) + 0.000000000118171 * pow(reading,3)- 0.000000301211691 * pow(reading,2)+ 0.001109019271794 * reading + 0.034143524634089;
}
