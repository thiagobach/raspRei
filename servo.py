import RPi.GPIO as GPIO # import GPIO librery

class servo():
    def __init__(self,servoPort=11,initialPos = 0):
        self.SP = servoPort
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.SP,GPIO.OUT)
        self.servoPos = GPIO.PWM(self.SP,initialPos)
        self.servoPos.start(initialPos)
        print ("Servo Initialized")
        
    def switch(self,straight = True):
        if straight:    
            self.servoPos.start(0)
            print("Train will follow forward")
        else:
            self.servoPos.start(7.5)
            print("Train will be deviated")
    
    def close(self):
        self.servoPos.stop() # stop PWM from GPIO output it is necessary
        GPIO.cleanup()
        print("This servo was disconected")
