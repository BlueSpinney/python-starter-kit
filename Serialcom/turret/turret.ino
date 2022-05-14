#include <Servo.h>

Servo serv1;
Servo serv2;


int recorx = 0;
int recory = 0;

int corx = 0;
int cory = 0;

int count = 0;

int servox = 0;
int servoy = 0;

void setup() {
  Serial.begin(112500);
  Serial.setTimeout(1);

  serv1.attach(9);
  serv2.attach(10);

}

void loop() {
  while (!Serial.available()){
    
  }
  for (int i = 0;i < Serial.readString().toInt() - servox;i++){
    serv1.write(servox + i);
    servox = servox + i;
  }
  delay(500);
  for (int i = 0;i < Serial.readString().toInt() - servoy;i++){
    serv2.write(servox + i);
    servoy = servoy + i;
  }  
}
