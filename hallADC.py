"""
This is the module that controls the hall sensor on the train.
The ahll sensor is influenced by the noise created by the motor, therefore
we are using a Analog to Digital Converter (ADC) to mitigate this effect.

The sensor used is a Adafruit ADS1115.

Due to the necessity of using interrupts, this module controls the state of the
train. Other modules will look for the orders in this module.
(self.orderMoving and self. orderForward).


"""



import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from websocket import create_connection
import logging


class adc_hall():

    def my_callbackA(self,channel):
        self.logger.info("I found a magnet!")
        self.pass_paras_to_station("h")
        

        

    def pass_paras_to_station(self,message):

        ws = create_connection("ws://192.168.3.12:13254")
        self.logger.info("Open")
        self.logger.info("Sending staus={}".format(message))
        ws.send(message)
        result = ws.recv()
        self.logger.info("Received '{}'".format(result))

        orderForwardString=result.split(' ')[0]
        orderMovingString=result.split(' ')[1]

        if orderForwardString == "True":
            self.orderForward = True
        else:
            self.orderForward = False


        if orderMovingString == "True":
            self.orderMoving = True
        else:
            self.orderMoving = False
    
            
        
        print(type(self.orderForward))

        print("The order recieved was Forward= " +str(self.orderForward) + " Moving = "+str(self.orderMoving))
        ws.close()
        self.logger.info("Close")
        
        
    def __init__(self, SensorPin = 16):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

        
        self.orderForward = False
        self.orderMoving = False
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1
        self.value = 0
        self.position = 0
        self.logger.info("Hall Sensor Initialized")
        self.forward = "forward"
        #Creates event Detector for the Pin that will interface with ADS1115 (ADS1115 Alert Pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SensorPin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(SensorPin,GPIO.RISING,callback=self.my_callbackA,bouncetime=300)

    def monitor(self, activate = True):
        if activate:
            self.logger.info("You enabled the position Monitoring.")
            self.adc.start_adc_comparator(0,  # Channel number
                         20000, 100000,  # High threshold value, low threshold value
                         active_low=False, traditional=False, latching=False,
                         num_readings=1, gain=self.GAIN)
        else:
            self.logger.info("You disabled the position Monitoring.")
            self.adc.stop_adc()
        
if __name__ == "__main__":
    hall = adc_hall()
    hall.monitor(True)
    

    
