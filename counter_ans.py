#import GPIO module import Rpi.GPIO as GPIO #import time for sleep function import time  #initialize GPIO to use Raspberry Pi pinouts GPIO.setmode(GPIO.BOARD) #set pin 7 to output mode GPIO.setup(17, GPIO.OUT) GPIO.setup(16, GPIO.IN)  while True:  in = GPIO.input(16)  while in == True:   print “waiting”  #turn on LED and wait 1 second  GPIO.output(17,True)  time.sleep(1)  #turn off LED and wait 1 second  GPIO.output(17,False)  time.sleep(1)