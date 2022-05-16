#include <Servo.h>

Servo ser;
Servo ser2;

String x;

String num = "";
String fnum = "";
String fnum2 = "";

char xlst[50];
int t1 = 0;


void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 ser.attach(9);
 ser2.attach(10);
}


void loop() {
   while (!Serial.available()){
    x = "";

    num = "";
    fnum = "";
    fnum2 = "";
    
    xlst[50];
    t1 = 0;
   }
   x = Serial.readString();
   Serial.println(x);
   int i = 0;
   x.toCharArray(xlst,50);
   while (t1 == 0){
    Serial.print("xlst : ");
    Serial.println(xlst);
      if (xlst[i] == ']'){
        fnum2 = num;
        break;
      }
      if (xlst[i] != '[' and xlst[i] != ','){
        num = num + xlst[i];
      }
      if (xlst[i] == ','){
        if (fnum == ""){
          fnum = num;
          num = "";
        }
      }
      i++;
   }
   fnum = fnum.toInt();
   fnum2 = fnum2.toInt();
   Serial.print("final number 1 : ");
   Serial.println(fnum);
   Serial.print("final number 2 : ");
   Serial.println(fnum2);
   ser.write(fnum.toInt());
   ser2.write(fnum2.toInt());

}
