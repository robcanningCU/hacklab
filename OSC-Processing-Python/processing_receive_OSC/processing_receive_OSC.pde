import oscP5.*;
import netP5.*;

OscP5 oscP5; // invoke the OSC library as an object called oscP5;

void setup() {
  size(400,400);
  oscP5 = new OscP5(this,12000); // get the OSC library to listen on port  12000
  // oscP5.plug connects the oscmessage addressed to "/some/osc/path/1" to the pythonLink function
  // we know this is going to be a string followed by a float - so we put "sf"
  oscP5.plug(this, "pythonLink","/some/osc/path/1", "sf"); 
  oscP5.plug(this, "anotherLink","/some/osc/buttonA", "f");
}
// declare a global string variable called someText which we will draw to the display
// i will update this later with the pythonLink function
String someText = "foo baz bar" ;
Float someNumber = 123.4;

void draw() {
  background(0); 
  textSize(32);
  fill(0, 102, 153);
  text(someText, 10, 30); 
  text(someNumber, 40, 130); 

}

//the below functions which are triggered because the message is plugged "oscP5.plug" above
// any errors in the .plug above or the functions below will result in an error like:
// ERROR @ OscPlug method processing.core.PApplet does not exist in your code.
public void pythonLink(String theValueA, float theValueB){
 println(theValueA);
 println(theValueB); 
 someText = theValueA;
 someNumber = theValueB;

}

public void anotherLink(float theValueA){
 println(theValueA);
}

/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  if(theOscMessage.isPlugged()==false) { // if not already "plugged in above, spit out messages here."
  /* print the address pattern and the typetag of the received OscMessage 
    good for seeing what messages are coming in but mostly you will want to keep this off unless testing */
  //println("### addrpattern\t"+theOscMessage.addrPattern());
  //println("### typetag\t"+theOscMessage.typetag());
  }
}