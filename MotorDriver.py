"""
    
    As now the motors are connected to the board in the following fashion:
        Port 23 - Input 2 pin
        Port 24 - Input 1 pin 
        Port 25 - Enable pin
        The driver is the L293D
        Supply voltage = 6V
"""

import RPi.GPIO as GPIO # import GPIO librery
from time import sleep
import hallADC as hall


class motor():
   def __init__(self,Input1Pin,Input2Pin,EnablePin):
        self.IAp = Input1Pin
        self.IBp = Input2Pin
        self.ENp = EnablePin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IAp,GPIO.OUT)
        GPIO.setup(self.IBp,GPIO.OUT)
        GPIO.setup(self.ENp,GPIO.OUT)
        self.pwm=GPIO.PWM(self.ENp,50)
        self.pwm.start(0) # starting it with 50% dutycycle
        #Motor1A = 24 # set GPIO-02 as Input 1 of the controller IC
        #Motor1B = 23 # set GPIO-03 as Input 2 of the controller IC 
        #Motor1E = 25 # set GPIO-04 as Enable pin 1 of the controller IC
        print ("This motor is ready to rock and roll")

   def runMotor(self,Speed=50,forward=True, moving = True):
      #print("Forward is set as: "+str(forward))
      #print("Moving is set as: " +str(moving))

      self.pwm.ChangeDutyCycle(Speed)
      if moving==True:
         GPIO.output(self.ENp,GPIO.HIGH)
         if forward:
            GPIO.output(self.IBp,GPIO.LOW)
            GPIO.output(self.IAp,GPIO.HIGH)
            hall.forward = "forward"
            #print ("Motor is running forward")
         else:
            GPIO.output(self.IBp,GPIO.HIGH)
            GPIO.output(self.IAp,GPIO.LOW)
            hall.forward = "backward"
           # print ("Motor is running backwards")
            
      if moving == False:
         GPIO.output(self.ENp,GPIO.LOW)
         GPIO.output(self.IBp,GPIO.LOW)
         GPIO.output(self.IAp,GPIO.LOW)
         #print("Motor stopped")
        
   def close(self):
        self.pwm.stop()# stop PWM from GPIO output it is necessary
        #GPIO.cleanup()
        print ("Motors are turned Off")

if __name__ == "__main__":
   hs1 = hall.adc_hall()
   hs1.monitor()
   locomotive = motor(23,24,25)

   locomotive.runMotor(100,True,True)
   sleep(1)
   locomotive.runMotor(100,False,True)
   sleep(1)
   
   locomotive.close()
