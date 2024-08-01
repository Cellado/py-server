import RPi.GPIO as GPIO
import time

class StepMotor:
    def __init__ (self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)


    def move(self, steps, delay = 0.01):

        if steps > 0:
            GPIO.output(self.dir_pin, True)
        else:
            GPIO.output(self.dir_pin, False)

        for _ in range(abs(steps)):
            GPIO.output(self.step_pin, True)
            time.sleep(delay)
            GPIO.output(self.step_pin, False)
            time.sleep(delay)


                    

    def cleanup (self):
        GPIO.cleanup()
        

