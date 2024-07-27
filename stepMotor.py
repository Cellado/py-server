import RPi.GPIO as GPIO
import time

class StepMotor:
    def __init__ (self, gpio_pins):
        self.gpio_pins = gpio_pins
        GPIO.setmode(GPIO.BOARD)
        for pin in self.gpio_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        self.step_sequence = [
             [1, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 1],
             [1, 0, 0, 1]
         ]
         
    def set_step(self, step):
        for pin, val in zip(self.gpio_pins, step):
            GPIO.output(pin, val)


    def move(self, steps, delay = 0.01):
        step_count = len(self.step_sequence)
        if steps > 0:
            for _ in range(abs(steps)):
                for step in self.step_sequence:
                    self.set_step(step)
                    time.sleep(delay)
        else:
            for _ in range(abs(steps)):
                for step in reversed(self.step_sequence):
                    self.set_step(step)
                    time.sleep(delay)
                    

    def cleanup (self):
        for pin in self.gpio_pins:
            GPIO.output(pin, False)
        GPIO.cleanup()
        

