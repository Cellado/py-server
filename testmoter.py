import time
import RPi.GPIO as GPIO



step_pin = 23
dir_pin = 24
ms2_pin = 17
ms1_pin = 27
enable_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(ms2_pin, GPIO.OUT)
GPIO.setup(ms1_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)


def set_step(ms1, ms2):
    print("set step function called")
    GPIO.output(ms1_pin, ms1)
    GPIO.output(ms2_pin, ms2)


def move(steps, delay=0.01):
    print("move function called")
    if steps > 0:
        GPIO.output(dir_pin, True)
    else:
        GPIO.output(dir_pin, False)

    for _ in range(abs(steps)):
        GPIO.output(step_pin, True)
        time.sleep(delay)
        GPIO.output(step_pin, False)
        time.sleep(delay)

try:
    set_step(GPIO.HIGH, GPIO.LOW)
    move(2000, delay=0.001)
    print("finished moving")

finally:
    print("clean up")
    GPIO.cleanup()
