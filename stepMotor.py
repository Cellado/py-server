import RPi.GPIO as GPIO
import time

class StepMotor:
    def __init__ (self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        
        GPIO.setmode(GPIO.BCM)
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
        
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    motor = StepMotor(step_pin=16, dir_pin=20)
    
    try:
        motor.move(steps=2000, delay=0.04)  # Move forward 200 steps
        time.sleep(1)
        motor.move(steps=-2000, delay=0.04)  # Move backward 200 steps
    finally:
        motor.cleanup()
