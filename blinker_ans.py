#import GPIO module
 import RPi.GPIO as GPIO
 #import time for sleep function
 import time  
#initialize GPIO to use Raspberry Pi pinouts 
GPIO.setmode(GPIO.BOARD)
 #set pin 7 to output mode
 GPIO.setup(15, GPIO.OUT)
GPIO.setup(14, GPIO.IN)
while True:
    button = GPIO.input(14)
    while button == True:
        print 'waiting'
     #turn on LED and wait 1 second 
    GPIO.output(15,True)
    time.sleep(1)
    #turn off LED and wait 1 second 
    GPIO.output(15,False)
    time.sleep(1)