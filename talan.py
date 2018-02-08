import RPi.GPIO as GPIO
import time 
count=0;
def lightit():
      
       
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(18,GPIO.OUT) 
		print " LED on" 
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		print "LED off"
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)	
while(1):
        count+=1;  
	print(count); 
	lightit(); 

