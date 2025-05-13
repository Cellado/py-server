import RPi.GPIO as GPIO
import time

class StepMotor:
    def __init__ (self, step_pin, dir_pin, en_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        

        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)


        GPIO.setup(self.en_pin, GPIO.OUT)
        GPIO.output(self.en_pin, GPIO.HIGH)
            
            
    def enable(self):
        GPIO.output(self.en_pin, GPIO.LOW)
    def disable(self):
        GPIO.output(self.en_pin, GPIO.HIGH)
        

    def move(self, steps, delay = 0.001):

        self.enable()
                
        GPIO.output(self.dir_pin, steps > 0)

        for _ in range(abs(steps)):
            GPIO.output(self.step_pin, True)
            time.sleep(delay)
            GPIO.output(self.step_pin, False)
            time.sleep(delay)
                    
        self.disable()
        
