#include <ArduinoJson.h>
#include <Servo.h>

String json;
int positions[6];
StaticJsonDocument<100> docReceived; // Json document to receive data
StaticJsonDocument<100> docTransmit; // Json document to transmit data
Servo srv1,srv2,srv3,srv4,srv5,srv6;  // create servo objects to control a servo
int posLimit_lower = 70;
int posLimit_upper = 170;
int posLimit_inv_lower = 10;
int posLimit_inv_upper = 110;

void setup() {
  Serial.begin(19200);
  Serial.setTimeout(10);
  srv1.attach(3);  // attaches the servo 1 on pin 3 to the servo object
  srv2.attach(5);  // attaches the servo 2 on pin 5 to the servo object
  srv3.attach(6);  // attaches the servo 3 on pin 6 to the servo object
  srv4.attach(9);  // attaches the servo 4 on pin 9 to the servo object
  srv5.attach(10);  // attaches the servo 5 on pin 10 to the servo object
  srv6.attach(11);  // attaches the servo 6 on pin 11 to the servo object

  srv1.write(90);
  srv2.write(90);
  srv3.write(90);
  srv4.write(90);
  srv5.write(90);
  srv6.write(90);
  
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

    

    positions[0] = docReceived["pos1"];
    positions[1] = docReceived["pos2"];
    positions[2] = docReceived["pos3"];
    positions[3] = docReceived["pos4"];
    positions[4] = docReceived["pos5"];
    positions[5] = docReceived["pos6"];
    int counter = docReceived["counter"];

    for(int i=0;i<6;i++){
      if(i==0 || i==2 || i==4){
        if((positions[i]<posLimit_lower)){
          positions[i] = posLimit_lower;
        } else if ((positions[i]>posLimit_upper)){
          positions[i] = posLimit_upper;
        }
      } else {
        if((positions[i]<posLimit_inv_lower)){
          positions[i] = posLimit_inv_lower;
        } else if ((positions[i]>posLimit_inv_upper)){
          positions[i] = posLimit_inv_upper;
        }
      }
    }
    
    srv1.write(positions[0]);
    srv2.write(positions[1]);
    srv3.write(positions[2]);
    srv4.write(positions[3]);
    srv5.write(positions[4]);
    srv6.write(positions[5]);

    docTransmit["counter"] = counter;

    serializeJson(docTransmit, Serial);
   
  }
}
