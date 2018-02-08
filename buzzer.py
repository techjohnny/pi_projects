import time 
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)

try:
   while True:
	gpio.output(11,0)
	time.sleep(.3)
	gpio.output(11,1)
	time.sleep(.3)
except KeyboardInterrupt:
	gpio.cleanup()
	exit
