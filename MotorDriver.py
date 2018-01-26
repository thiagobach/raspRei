import RPi.GPIO as GPIO # import GPIO librery
from time import sleep


#Setup the GPIO
GPIO.setmode(GPIO.BCM)
Motor1A = 24 # set GPIO-02 as Input 1 of the controller IC
Motor1B = 23 # set GPIO-03 as Input 2 of the controller IC 
Motor1E = 25 # set GPIO-04 as Enable pin 1 of the controller IC
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
pwm=GPIO.PWM(Motor1E,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle

def runMotor(Speed,forward):
    pwm.ChangeDutyCycle(Speed)
    GPIO.output(Motor1E,GPIO.HIGH)

    if forward:
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1A,GPIO.HIGH)
    else:
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1A,GPIO.LOW)
        
    
    
def stop():
    GPIO.output(Motor1E,GPIO.LOW)

def turnOff():
    pwm.stop() # stop PWM from GPIO output it is necessary
    GPIO.cleanup()
    print("Off")

runMotor(100,False)
sleep(3)

runMotor(50,False)
sleep(3)

runMotor(30,False)
sleep(3)

runMotor(100,True)
sleep(3)


stop()
turnOff()
