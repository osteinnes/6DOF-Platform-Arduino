#include <ArduinoJson.h>
#include <Servo.h>

String json;
StaticJsonDocument<100> docReceived; // Json document to receive data
StaticJsonDocument<100> docTransmit; // Json document to transmit data
Servo srv1,srv2,srv3,srv4,srv5,srv6;  // create servo objects to control a servo

void setup() {
  Serial.begin(19200);
  Serial.setTimeout(10);
  srv1.attach(3);  // attaches the servo 1 on pin 3 to the servo object
  srv2.attach(5);  // attaches the servo 2 on pin 5 to the servo object
  srv3.attach(6);  // attaches the servo 3 on pin 6 to the servo object
  srv4.attach(9);  // attaches the servo 4 on pin 9 to the servo object
  srv5.attach(10);  // attaches the servo 5 on pin 10 to the servo object
  srv6.attach(11);  // attaches the servo 6 on pin 11 to the servo object

  srv1.write(0);
  srv2.write(0);
  srv3.write(0);
  srv4.write(0);
  srv5.write(0);
  srv6.write(0);
  
}

void loop() {
   
  if(Serial.available()> 0){
    json = Serial.readString();

    DeserializationError error = deserializeJson(docReceived, json);

    if (error) {
      return;
      //Serial.print("deserializeJson() failed with code ");
      //Serial.println(error.c_str());
    }

    int pos1 = docReceived["pos1"];
    int pos2 = docReceived["pos2"];
    int pos3 = docReceived["pos3"];
    int pos4 = docReceived["pos4"];
    int pos5 = docReceived["pos5"];
    int pos6 = docReceived["pos6"];
    int counter = docReceived["counter"];

    srv1.write(pos1);
    srv2.write(pos2);
    srv3.write(pos3);
    srv4.write(pos4);
    srv5.write(pos5);
    srv6.write(pos6);

    docTransmit["counter"] = counter;

    serializeJson(docTransmit, Serial);
   
  }
}
