Due to the presence of sensors and actuators, test-driven development seems almost impossible in Raspberry Pi. Testing is a determinant of whether objectives are being met in a process, and, performing it as much as possible is a very valid approach. I performed software tests on Raspberry Pi B3 in Python, using a small setup (consisting of one LED, one 330 ohms Resistor, one Breadboard, two Push Buttons and some Jumper Wires). Here is a brief account of steps that I followed:
1) Installing Raspbian on a SD card 
2) Connecting Pi to my laptop using ethernet cable
3) Using VNC Server to gain visual remote access to Pi
4) Connecting the setup to Pi
5) Operating Pi as a remote desktop for programming 
6) Creating a Python file blink.py, which on running in Python Shell will make the LED blink every 0.5 seconds
7) Creating another similar file named reaction.py, which on running works as a Swift Reaction Game. In it, the LED will light up for a random amount of time between 5 to 10 seconds and the name of whichever Button pressed first after the LED goes off is displayed.


References: 
1) http://www.knight-of-pi.org/python-project-setup-test-driven-development/
2) https://www.raspberrypi.org/learning/python-quick-reaction-game/worksheet/
