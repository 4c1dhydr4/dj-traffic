/*
	Archivo Arduino para el proyecto Dj-Traffic
	Las luces del semáforo estarán conectadas a los pones 2,3,4 y 5,6,7 para cada semáforo
	respectivamente como indican las variables
	También puedes configurar un semáforo con las luces para los peatones en los pines
	8, 9 y 10, 11 respectivamente. 
	Red = Rojo, Yellow = Amarillo, Green = Verde en alusión a los colores de un semáforo real.
*/
String inCode = "";
boolean codeComplete = false;
int del = 500, delay_person = 100;//550; //delay_person = tiempo_real/9

int red_vertical = 2, red_horizontal = 5;
int yellow_vertical = 3, yellow_horizontal = 6;
int green_vertical = 4, green_horizontal = 7;

int person_red_vertical = 8, person_red_horizontal = 10;
int person_green_vertical = 9, person_green_horizontal = 11;
 
void setup() {
  Serial.begin(9600);
  inCode.reserve(200);
  for(int i=2;i<13;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,LOW);
  }
}

void loop() {
  active();
}

void reset_inCode(){
  inCode = "";
  codeComplete = false;
}
void active(){
  if (codeComplete) {
    if(inCode == "Vertical_PASS\n"){
      horizontal_reflection();
      while(!Serial.available()){
        vertical_pass();
      }
    }
    if(inCode == "Horizontal_PASS\n"){
      vertical_reflection();
      while(!Serial.available()){
        horizontal_pass();
      }
    }
    reset_inCode();
  }
}
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inCode += inChar;
    if (inChar == '\n') {
      codeComplete = true;
    }
  }
}

void vertical_pass(){
//Vertical en verde y horizontal en rojo
  //Paso peatonal horizontal en verde
  digitalWrite(red_vertical, LOW);
  digitalWrite(yellow_vertical, LOW);
  digitalWrite(green_vertical, HIGH);

  digitalWrite(person_red_vertical, HIGH);
  digitalWrite(person_green_vertical, LOW);

  digitalWrite(red_horizontal, HIGH);
  digitalWrite(yellow_horizontal, LOW);
  digitalWrite(green_horizontal, LOW);

  digitalWrite(person_red_horizontal, LOW);
  digitalWrite(person_green_horizontal, HIGH);
}

void vertical_reflection(){
//Vertical en ambar y horizontal en rojo
  //Paso peatonal horizontal en verde
  digitalWrite(red_vertical, LOW);
  digitalWrite(yellow_vertical, HIGH);
  digitalWrite(green_vertical, LOW);
  
  digitalWrite(red_horizontal, HIGH);
  digitalWrite(yellow_horizontal, LOW);
  digitalWrite(green_horizontal, LOW);
  
  digitalWrite(person_red_vertical, HIGH);
  digitalWrite(person_green_vertical, LOW);
  
  digitalWrite(person_red_horizontal, LOW);
  digitalWrite(person_green_horizontal, HIGH);
  
  delay(delay_person);
  digitalWrite(person_green_horizontal, LOW);
  delay(delay_person);
  digitalWrite(person_green_horizontal, HIGH);
  delay(delay_person);
  digitalWrite(person_green_horizontal, LOW);
  delay(delay_person);
  digitalWrite(person_green_horizontal, HIGH);
  delay(delay_person);
  digitalWrite(person_green_horizontal, LOW);
  delay(delay_person);
  digitalWrite(person_green_horizontal, HIGH);
  delay(delay_person);
  digitalWrite(person_green_horizontal, LOW);
  delay(delay_person);
  digitalWrite(person_green_horizontal, HIGH);
  delay(delay_person);
}

void horizontal_pass(){
//Vertical en rojo y horizontal en verde
  //Paso peatonal vertical en verde
  digitalWrite(red_vertical, HIGH);
  digitalWrite(yellow_vertical, LOW);
  digitalWrite(green_vertical, LOW);

  digitalWrite(person_red_vertical, LOW);
  digitalWrite(person_green_vertical, HIGH);

  digitalWrite(red_horizontal, LOW);
  digitalWrite(yellow_horizontal, LOW);
  digitalWrite(green_horizontal, HIGH);

  digitalWrite(person_red_horizontal, HIGH);
  digitalWrite(person_green_horizontal, LOW);
}

void horizontal_reflection(){
//Vertical en rojo y horizontal en ambar
  //Paso peatonal vertical en verde
  digitalWrite(red_vertical, HIGH);
  digitalWrite(yellow_vertical, LOW);
  digitalWrite(green_vertical, LOW);
  
  digitalWrite(red_horizontal, LOW);
  digitalWrite(yellow_horizontal, HIGH);
  digitalWrite(green_horizontal, LOW);

  digitalWrite(person_red_horizontal, HIGH);
  digitalWrite(person_green_horizontal, LOW);

  digitalWrite(person_red_vertical, LOW);
  digitalWrite(person_green_vertical, HIGH);

  delay(delay_person);
  digitalWrite(person_green_vertical, LOW);
  delay(delay_person);
  digitalWrite(person_green_vertical, HIGH);
  delay(delay_person);
  digitalWrite(person_green_vertical, LOW);  
  delay(delay_person);
  digitalWrite(person_green_vertical, HIGH);
  delay(delay_person);
  digitalWrite(person_green_vertical, LOW);  
  delay(delay_person);
  digitalWrite(person_green_vertical, HIGH);
  delay(delay_person);
  digitalWrite(person_green_vertical, LOW);  
  delay(delay_person);
  digitalWrite(person_green_vertical, HIGH);
  delay(delay_person);
}
