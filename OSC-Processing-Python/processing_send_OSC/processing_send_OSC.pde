import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress myRemoteLocation;

void setup() {
  size(400,400);
  oscP5 = new OscP5(this,12001); // listen on port  12000
  oscP5.plug(this, "pythonlink","/startup");
  myRemoteLocation = new NetAddress("127.0.0.1",12000); // send to port 57120
}

void draw() {
  background(0);  
}

public void pythonlink(String theValueA, String theValueB) {
 println(theValueA);
 println(theValueB); 
}

void mousePressed() {
  /* in the following different ways of creating osc messages are shown by example */
  OscMessage myMessage = new OscMessage("/startup");
  myMessage.add(123); /* add an int to the osc message */
  /* send the message */
  oscP5.send(myMessage, myRemoteLocation); 
}

/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  /* with theOscMessage.isPlugged() you check if the osc message has already been
   * forwarded to a plugged method. if theOscMessage.isPlugged()==true, it has already 
   * been forwared to another method in your sketch. theOscMessage.isPlugged() can 
   * be used for double posting but is not required.
  */  
  if(theOscMessage.isPlugged()==false) {
  /* print the address pattern and the typetag of the received OscMessage */
  println("### received an osc message.");
  println("### addrpattern\t"+theOscMessage.addrPattern());
  println("### typetag\t"+theOscMessage.typetag());
  println(theOscMessage.get(0).stringValue());

  }
}