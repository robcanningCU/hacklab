#!/usr/bin/python

# simple OSC send script to test processing OSC receive

import OSC # we need to install this OSC library sudo pip install pyosc

c = OSC.OSCClient()
# c.connect(('169.254.89.184', 57120))   # localhost, port 57120
c.connect(('127.0.0.1', 12000))   # localhost, port 57120
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/some/osc/path/1")
oscmsg.append('Hello World!')
oscmsg.append(0.146)

c.send(oscmsg)
