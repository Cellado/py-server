import socket
import RPi.GPIO as GPIO
from stepMotor import StepMotor

#StepMotor 1
motor_pins1 = [16, 18, 22, 36]

Smotor1 = StepMotor(motor_pins1)

host = ''
port = 5138
buffer_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print(f'Server started on port {port}')

try:
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(buffer_size)
            if not data:
                print("invalid date... breaking connection")
                conn.sendall(b'invalid data\n')
                break
            command = data.decode('utf-8').strip().lower()
            if command == 'on':
                Smotor1.move(10)
                print("High")
                conn.sendall(b'signal "on" recived\n')
            elif command == 'off':
                Smotor1.move(10)
                print("Low")
                conn.sendall(b'signal "off" recived\n')
            else:
                conn.sendall(b'Invalid command\n')

finally:
    print("Finally")
    GPIO.cleanup()
    conn.close()
    sock.close()
    
