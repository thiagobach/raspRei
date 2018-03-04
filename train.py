##initialize Motor]
from time import sleep
import MotorDriver
locomotive = MotorDriver.motor(23,24,25)

#initialize Hall
import hallADC as hall
hallSensor = hall.adc_hall()
hallSensor.monitor()


if __name__ == "__main__":
    hallSensor.pass_paras_to_station(hallSensor.forward)
    while True:
        if hallSensor.orderMoving == False:
            print("What should I do Mr. Server?")
            locomotive.runMotor(50, hallSensor.orderForward, hallSensor.orderMoving)
            hallSensor.pass_paras_to_station("t")
            sleep(3)
            
        if hallSensor.orderMoving == True:
            locomotive.runMotor(50, hallSensor.orderForward, hallSensor.orderMoving)
            

