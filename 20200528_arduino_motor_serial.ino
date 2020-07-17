

int s1 = 8;
int s2 = 9;
int s3 = 10;
int s4 = 11;
int mssg = 0; // mensaje serial 

 
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(s4, OUTPUT);
  
  return;

}

void derecha(){
   Serial.print("derecha");
   digitalWrite(s2, LOW);    // turn the LED off by making the voltage LOW
   digitalWrite(s3, LOW);   // turn the LED on (HIGH is the voltage level)
   delay(60); 
   digitalWrite(s1, HIGH);    // turn the LED off by making the voltage LOW
   digitalWrite(s4, HIGH);   // turn the LED on (HIGH is the voltage level)
   

     
  
  
  }



void izquierda(){
  
  Serial.print("Izquierda");
  digitalWrite(s1, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(s4, LOW);    // turn the LED off by making the voltage LOW
  delay(60);
  digitalWrite(s2, HIGH);    // turn the LED off by making the voltage LOW
  digitalWrite(s3, HIGH);   // turn the LED on (HIGH is the voltage level)


  
  
  
    }

void nunca(){
 
  digitalWrite(s1, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(s2, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(s3, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(s4, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);    
  }
    
void nada(){
   Serial.print("Nada");
  digitalWrite(s1, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(s2, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(s3, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(s4, LOW);    // turn the LED off by making the voltage LOW
  delay(50);    



  
  }





void loop() {






 if (Serial.available()>0) 
   {
      mssg = Serial.parseInt(); // leer serial
      
       delay(20);
   }






if ( mssg == 1)
{
    derecha();
 
  }


if ( mssg == 2)
{

  izquierda();

  }

if ( mssg == 3)
{
  nada();
  }


 

 