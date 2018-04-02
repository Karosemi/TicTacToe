#include <CapacitiveSensor.h>
CapacitiveSensor   cs_4_2 = CapacitiveSensor(4,2);
CapacitiveSensor   cs_4_3 = CapacitiveSensor(4,3);
CapacitiveSensor   cs_4_5 = CapacitiveSensor(4,5);
CapacitiveSensor   cs_4_6 = CapacitiveSensor(4,6);
CapacitiveSensor   cs_4_7 = CapacitiveSensor(4,7);
CapacitiveSensor   cs_4_8 = CapacitiveSensor(4,8);
CapacitiveSensor   cs_4_9 = CapacitiveSensor(4,9);
CapacitiveSensor   cs_4_10 = CapacitiveSensor(4,10);
CapacitiveSensor   cs_4_11 = CapacitiveSensor(4,11);
int Red=12;
int Blue=13;
void setup() {
  Serial.begin(9600);
  pinMode(Red,OUTPUT);
  pinMode(Blue,OUTPUT);
  // use the same baud-rate as the python side
}
int u;
void loop() {
  
  if(Serial.available()>0)
  { u=Serial.read();
  ;
  
  if(u=='1'){
    digitalWrite(Blue,HIGH);
    digitalWrite(Red,LOW);
  }
   else if (u='2'){
   digitalWrite(Blue,LOW);
    digitalWrite(Red,HIGH);
    
    }
    }
  long total1_2 =  cs_4_2.capacitiveSensor(30);
  long total2_3 =  cs_4_3.capacitiveSensor(30);
  long total3_5 =  cs_4_5.capacitiveSensor(30);
  long total4_6 =  cs_4_6.capacitiveSensor(30);
  long total5_7 =  cs_4_7.capacitiveSensor(30);
  long total6_8 =  cs_4_8.capacitiveSensor(30);
  long total7_9 =  cs_4_9.capacitiveSensor(30);
  long total8_10 =  cs_4_10.capacitiveSensor(30);
  long total9_11 =  cs_4_11.capacitiveSensor(30);
  if(total1_2>200){
  Serial.println("1");
  }
  else if(total2_3>200){
  Serial.println("2");}
  else if(total3_5>200){
  Serial.println("3");}
  else if(total4_6>200){
  Serial.println("4");}
  else if(total5_7>300){
  Serial.println("5");}
  else if(total6_8>200){
  Serial.println("6");}
  else if(total7_9>200){
  Serial.println("7");}
  else if(total8_10>200){
  Serial.println("8");}
  else if(total9_11>200){
  Serial.println("9");}
  delay(100);
}
