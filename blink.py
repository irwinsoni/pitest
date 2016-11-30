from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BOARD)
LED = 7

GPIO.setup(LED, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(LED, GPIO.LOW)
    sleep(0.5)
    GPIO.output(LED, GPIO.HIGH)
    sleep(0.5)
exit()
