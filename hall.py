
"""
This is the class for the hall Sensor 
Pin 1 - VCC (5V)
Pin 2 - GND
Pin 3 - hallPort

Connect pin 1 and 3 with 3kohm resistor for pull up

"""
import RPi.GPIO as GPIO # import GPIO librery
import time

class hallSensor():
    
    def my_callbackA(self,channel):
        self.arrivalTime = (time.time())
        return self.arrivalTime

    def __init__(self,hallPort=18):
        self.arrivalTime = 0
        self.port = hallPort
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.port,GPIO.RISING,callback=self.my_callbackA,bouncetime=300)
        print("Hall sensor started on port %0d" % hallPort)

    def hallReading(self):
        status = GPIO.input(self.port)
        return status

    

if __name__ == "__main__":
    print("Hello friendly stranger!")
    hs1 = hallSensor(18)
    start = time.time()
    while (time.time()-start)<180:
        print(hs1.arrivalTime)

    

        
