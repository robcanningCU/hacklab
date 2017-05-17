import serial, time
import pygame

# pygame is a handy library for doing lots of stuff like controling audio,
# getting keystrokes, drawing stuff to screen... anything you would expect in a
# game - for this example I am simply using it to detect key press events
# to install it you will need to run: sudo pip install pygame

pygame.init() # start and initialise the game engine
pygame.display.set_mode((600,400),0,32) # initialise the default display
# you need to have the game focused for the key strokes to be detected
screen = pygame.display.set_caption('Arduino/Python Serial Link')


# set up the serial port ready to commuicate to the arduino
SPEED = 9600
PORT = '/dev/cu.usbmodem1411' # you may need to change this for your system
# check in the arduino IDE: TOOLS: PORT: to see what address your arduino is at.
ser = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)

# below is a basic function which sends stuff over the serial
def send2ard(msg):
    ser.write(msg);
    print("I am sending a Serial message to the Arduino now!")
    print("The message is: " + msg)

while True:
    # this while statement does 'stuff' when TRUE which is the case whenever the
    # script is running - what it does is listen for events from the game
    for event in pygame.event.get():
        # in particular it is listening for key down events/strokes
        if event.type == pygame.KEYDOWN:
            # if the key is "0" then run the serial send fuction send2ard with
            # message "0" - then print to the console a little message for testing
            if event.key == pygame.K_0:
                send2ard("0");
                # same as above but now listening for the key "1" (pygame.K_1:)
            if event.key == pygame.K_1:
                send2ard("1");
            if event.key == pygame.K_2:
                send2ard("2");

    # this listens for any Serial messages coming from athe Arduino
    # and prints them to the console - this allows two-way comms
        msg = ser.read(ser.inWaiting()) # read all characters in buffer
        if len(msg)>0:
            print (msg);
