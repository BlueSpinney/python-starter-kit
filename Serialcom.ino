int x;
int o1 = 7;
int state = 0;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 
 pinMode(5,OUTPUT);
 pinMode(7,OUTPUT);
 pinMode(8,OUTPUT);
 pinMode(9,OUTPUT);
 pinMode(10,OUTPUT);
 pinMode(11,OUTPUT);
 pinMode(12,OUTPUT);
 
}
void loop() {
 while (!Serial.available()){
  if (x==1){
    if (state == 0){
       digitalWrite(o1,HIGH);
    }
    else{
      digitalWrite(o1,LOW);
    }
    if (o1 == 12){
      o1 = 6;
      if (state == 0){
        state = 1;
      }
      else{
        state = 0;
      }
    }
    o1 = o1 + 1;
    
  }
  else{
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
    digitalWrite(10,LOW);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);
  }
  delay(75);
 }

 
  x = Serial.readString().toInt();
  if (x== 1){
    digitalWrite(5,HIGH);
  }
  if (x == 0){
    digitalWrite(5,LOW);
  }
  Serial.print(x);
 
}
