import time
import RPi.GPIO as GPIO

# Motor 1
Motor1F = 11
Motor1B = 13

# Motor 2
Motor2F = 29 
Motor2B = 31

GPIO.setmode(GPIO.BOARD)
# Motor 1
GPIO.setup(Motor1F, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
# Motor 2
GPIO.setup(Motor2F, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)

try:
    print("testing...")
    GPIO.output(Motor1F, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2F, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.HIGH)
    time.sleep(10)

finally:
    GPIO.cleanup()
