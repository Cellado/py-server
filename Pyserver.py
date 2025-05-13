import socket
import threading 
import RPi.GPIO as GPIO
import time
from stepMotor import StepMotor

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#StepMotor 1

Smotor1 = StepMotor(step_pin=16, dir_pin=18, en_pin=22)
Smotor2 = StepMotor(step_pin=13 , dir_pin=15, en_pin=31)

host = ''
port = 5138
buffer_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print(f'Server started on port {port}')


def move_motor (motor, steps):
    motor.move(steps, delay=0.0001)

def sim_move(motor1, steps1, motor2, steps2):
    thread1 = threading.Thread(target=move_motor, args=(motor1, steps1))
    thread2 = threading.Thread(target=move_motor, args=(motor2, steps2))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
try:
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(buffer_size)
            command = data.decode('utf-8').strip().lower()
            if not data:
                conn.sendall(b'No data recived\n')
                break
            if command == 'on':
                sim_move(Smotor1, 1, Smotor2, 1)
                print("Right")
                conn.sendall(b'signal "on" recived\n')
            elif command == 'off':
                sim_move(Smotor1, -1, Smotor2, -1)
                print("Left")
                conn.sendall(b'signal "off" recived\n')
            elif command == 'close':
                print("closing")
                conn.sendall(b'signal "close" recived\n')
                conn.close()
                sock.close()
                GPIO.cleanup()
                break
            else:
                conn.sendall(b'Invalid command\n')

finally:
    print("Finally")
    GPIO.cleanup()
    conn.close()
    sock.close()
    
