import RPi.GPIO as GPIO # import GPIO librery
from time import sleep

class servo():
    def __init__(self,servoPort=18):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPort,GPIO.OUT)
        self.servoPos = GPIO.PWM(servoPort,50)
        #self.servoPos.start(initialPos)
        print ("Servo Initialized")
        
    def switch(self,position):
            
            self.servoPos.start(position)
            sleep(0.5)
            self.servoPos.stop()
            
            
    def close(self):
        self.servoPos.stop()
        GPIO.cleanup()
        print("This servo was disconected")


if __name__ == "__main__":
    #deviate 1.0
    #straight 4.0
    S1 = servo(14)
    S2 = servo(15)
    S3 = servo(18)
    S4 = servo(23)
    
    
    S1.switch(4.0)
    S2.switch(4.0)
    S3.switch(4.0)
    S4.switch(4.0)
    sleep(5)
    S1.switch(1.0)
    S2.switch(1.0)
    S3.switch(1.0)
    S4.switch(1.0)
    S1.close
