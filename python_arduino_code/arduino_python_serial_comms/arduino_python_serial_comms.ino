// Example demonstrating two-way communications between Arduino and Python 

// Declare a String variable which reads from Serial buffer
String readString; // this will be used to hold the messages coming from Python. 
//  https://www.arduino.cc/en/Serial/ReadString

// the setup where we set stuff up that runs once when the Arduino boots up...
void setup(){
    pinMode(LED_BUILTIN, OUTPUT); // set the built in LED "PIN" up as an OUTPUT
    // pins can be INPUT for sensors etc. or OUTPUT for LEDs, motors etc.
    Serial.begin(9600);  // initialize serial communications at 9600 bps 
    // we need to make sure this is the same in the Python script
    // if we are reading at one speed and writing at another chaos will ensue.. 
  }

// everything in this loop is running non stop while the Arduino is on.
// main function in this case is to listen for messages from Python and
// do "things" when certain messages are recieved.

void loop(){
  while (!Serial.available()) {} // if serial messages are not available do nothing
  // if serial messages are available then and bigger than 0 then...
  while (Serial.available()){ 
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString = c; //makes the string readString
      }
    }
    if (readString.length() >0) // if the message is longer than 0...
    { // send a message back to the Python script whenever something is received
      Serial.println("Message from Arduino: "+ readString);  
      // use the conditional IF statement to do specific things based on what 
      // message Python is sending i.e. what key is being hit
      if (readString == "0"){
        // hitting key one turns the LED on
        digitalWrite(LED_BUILTIN, HIGH);
        } else if (readString == "1"){
        // hitting 1 turns the LED OFF
        digitalWrite(LED_BUILTIN, LOW);
        } else if (readString == "2"){
        // hitting "2" turns the LED on and sends a message back to Python
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println("Hello from the Arduino, someone just hit a '2' key!");
        }
    }
} // ROB CANNING 2017
