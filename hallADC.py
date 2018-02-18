import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

class adc_hall():

    def my_callbackA(self,channel):
        arrivalTime = (time.time())
        
        ## Here we have to include position handling.
        self.position = self.position+1
        print(self.position)
        return arrivalTime

    def __init__(self, SensorPin = 16):
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1
        self.value = 0
        self.position = 0
        print(str(time.ctime() )+" - Hall Sensor Reading using ADS1115 Initialized")
        print(str(time.ctime() )+ " - Sensor Gain: " + str(self.GAIN))
        self.forward = True
        #Creates event Detector for the Pin that will interface with ADS1115 (ADS1115 Alert Pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SensorPin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(SensorPin,GPIO.RISING,callback=self.my_callbackA,bouncetime=300)

    def monitor(self, activate = True, Position = 0):
        if activate:
            print(str(time.ctime() )+" - You enabled the position Monitoring.")
            self.adc.start_adc_comparator(0,  # Channel number
                         20000, 100000,  # High threshold value, low threshold value
                         active_low=False, traditional=False, latching=False,
                         num_readings=1, gain=self.GAIN)
        else:
            print(str(time.ctime() )+" - You disabled the position Monitoring.")
            self.adc.stop_adc()
                        
                
                
  
        
if __name__ == "__main__":
    hall = adc_hall()
    hall.monitor(True)
    

    
