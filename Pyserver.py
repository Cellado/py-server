import socket
import threading 
import RPi.GPIO as GPIO
import time
from stepMotor import StepMotor


#StepMotor 1
motor_pins1 = [16, 18, 22, 36]
motor_pins2 = [3, 5, 7, 11]

Smotor1 = StepMotor(motor_pins1)
Smotor2 = StepMotor(motor_pins2)

host = ''
port = 5138
buffer_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print(f'Server started on port {port}')


def sim_move(motor1, move_amount1, motor2, move_amount2):
    thread1 = threading.Thread(target=move_motor, args=(motor1, move_amount1))
    thread2 = threading.Thread(target=move_motor, args=(motor2, move_amount2))
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
            if command == 'on':
                sim_move(Smotor1, 10, Smotor2, 50)
                print("Right")
                conn.sendall(b'signal "on" recived\n')
            elif command == 'off':
                sim_move(Smotor1, -10, Smotor2, -50)
                print("Low")
                conn.sendall(b'signal "off" recived\n')
            elif command == 'close':
                print("closing")
                conn.sendall(b'signal "close" recived\n')
                GPIO.cleanup()
                conn.close()
                sock.close()
                break
            else:
                conn.sendall(b'Invalid command\n')

finally:
    print("Finally")
    GPIO.cleanup()
    conn.close()
    sock.close()
    
