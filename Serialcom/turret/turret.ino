int recorx = 0;
int recory = 0;

int corx = 0;
int cory = 0;

int count = 0;


void setup() {
  Serial.begin(112500);
  Serial.setTimeout(1);

}

void loop() {
  while (!Serial.available()){
    
  }
  if (count == 0){
    for (int i = 0;i < Serial.readString().toInt();i++){
      
    }
  }
  

}
