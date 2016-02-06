//Testing
#include <Wire.h>

int pinI1=8;//define I1 interface
int pinI2=11;//define I2 interface
int speedpinA=9;//enable motor A
int pinI3=12;//define I3 interface
int pinI4=13;//define I4 interface
int speedpinB=10;//enable motor B
int spead=127;//define the spead of motor
int c = 0; //set c to 0
const int pingPin = 7; //Sets sensor pin number

void setup() {
  pinMode(pinI1,OUTPUT);
  pinMode(pinI2,OUTPUT);
  pinMode(speedpinA,OUTPUT);
  pinMode(pinI3,OUTPUT);
  pinMode(pinI4,OUTPUT);
  pinMode(speedpinB,OUTPUT);
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
}

void loop() {
  //c = 0;

  if(c == 1){
    Serial.println(c);
    forward();
    c = 0;
  }else if(c == 2){
    Serial.println(c);
    left();
    c = 0;
  }else if(c == 3){
    Serial.println(c);
    backward();
    c = 0;
  }else if(c == 4){
    Serial.println(c);
    right();
    c = 0;
  }else if(c == 5){
    Serial.println(c);
    stop();
    c = 0;
  }else{
    //Serial.println(c);
    c = 0;
  }
  delay(500);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  //while (1 < Wire.available()) { // loop through all but the last
  c = Wire.read(); // receive byte as a character
    //Serial.print(c);         // print the character
  //}
  //int x = Wire.read();    // receive byte as an integer
  //Serial.println(x);         // print the integer
}

void forward()
{
     analogWrite(speedpinA,spead);//input a simulation value to set the speed
     analogWrite(speedpinB,spead);
     digitalWrite(pinI4,HIGH);//turn DC Motor B move clockwise
     digitalWrite(pinI3,LOW);
     digitalWrite(pinI2,LOW);//turn DC Motor A move anticlockwise
     digitalWrite(pinI1,HIGH);
}
void backward()//
{
     analogWrite(speedpinA,spead);//input a simulation value to set the speed
     analogWrite(speedpinB,spead);
     digitalWrite(pinI4,LOW);//turn DC Motor B move anticlockwise
     digitalWrite(pinI3,HIGH);
     digitalWrite(pinI2,HIGH);//turn DC Motor A move clockwise
     digitalWrite(pinI1,LOW);
}
void left()//
{
     analogWrite(speedpinA,spead);//input a simulation value to set the speed
     analogWrite(speedpinB,spead);
     digitalWrite(pinI4,HIGH);//turn DC Motor B move clockwise
     digitalWrite(pinI3,LOW);
     digitalWrite(pinI2,HIGH);//turn DC Motor A move clockwise
     digitalWrite(pinI1,LOW);
}
void right()//
{
     analogWrite(speedpinA,spead);//input a simulation value to set the speed
     analogWrite(speedpinB,spead);
     digitalWrite(pinI4,LOW);//turn DC Motor B move anticlockwise
     digitalWrite(pinI3,HIGH);
     digitalWrite(pinI2,LOW);//turn DC Motor A move clockwise
     digitalWrite(pinI1,HIGH);
}
void stop()//
{
     digitalWrite(speedpinA,LOW);// Unenble the pin, to stop the motor. this should be done to avid damaging the motor.
     digitalWrite(speedpinB,LOW);
     delay(1000);

}

int readsensor()
{
  int senseTrue = 0;
   // establish variables for duration of the ping,
  // and the distance result in inches and centimeters:
  long duration, inches, cm;

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  // convert the time into a distance
  inches = microsecondsToInches(duration);

  if (inches >= 6){
    return(10);
  }else{
    return(0);
  }
}
long microsecondsToInches(long microseconds) {
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}

int readVoltage(){
  float temp;
  voltageVal = analogRead (0); //read the value from voltage sensor.
  temp = voltageVal/4.092; //resolution value to store
  voltageVal = (int) temp ;
  calcVoltageVal = ((voltageVal% 100) / 10); //calculate stepped down voltage
  return(calcVoltageVal);
}