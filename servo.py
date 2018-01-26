import RPi.GPIO as GPIO # import GPIO librery
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)


def turnOff():
    pwm.stop() # stop PWM from GPIO output it is necessary
    GPIO.cleanup()
    print("Off")

    
pwm.start(2)
sleep(1)
pwm.start(5)
sleep(1)
pwm.start(7.5)
sleep(1)

pwm.start(2)
sleep(1)
pwm.start(5)
sleep(1)
pwm.start(7.5)
sleep(1)

pwm.start(2)
sleep(1)
pwm.start(5)
sleep(1)
pwm.start(7.5)
sleep(1)


turnOff()
