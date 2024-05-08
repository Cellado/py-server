import socket

import RPi.GPIO as GPIO

# Motor 1
Motor1F = 11
Motor1B = 13

# Motor 2
Motor2F = 29 
Motor2B = 31

#StepMotor 1
Smotor1 = 16
Smotor2 = 18
Smotor3 = 22
Smotor4 = 36

GPIO.setmode(GPIO.BOARD)
# Motor 1
GPIO.setup(Motor1F, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
# Motor 2
GPIO.setup(Motor2F, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)

#StepMotor 1
GPIO.setup(smotor1, GPIO.OUT)
GPIO.setup(smotor2, GPIO.OUT)
GPIO.setup(smotor3, GPIO.OUT)
GPIO.setup(smotor4, GPIO.OUT)

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
                break
            command = data.decode('utf-8').strip().lower()
            if command == 'on':
                GPIO.output(Motor1F, GPIO.HIGH)
                GPIO.output(Motor2F, GPIO.HIGH)
                GPIO.output(smotor1, GPIO.HIGH)
                GPIO.output(smotor2, GPIO.HIGH)
                GPIO.output(smotor3, GPIO.LOW)
                GPIO.output(smotor4, GPIO.LOW)
                print("High")
                conn.sendall(b'Motor1F HIGH\n')
                conn.sendall(b'Motor2F HIGH\n')
            elif command == 'off':
                GPIO.output(Motor1F, GPIO.LOW)
                GPIO.output(Motor2F, GPIO.LOW)
                GPIO.output(smotor3, GPIO.HIGH)
                GPIO.output(smotor4, GPIO.HIGH)
                GPIO.output(smotor1, GPIO.LOW)
                GPIO.output(smotor3, GPIO.LOW)
                print("Low")
                conn.sendall(b'Motor1F LOW\n')
                conn.sendall(b'Motor2F LOW\n')
            else:
                conn.sendall(b'Invalid command\n')

finally:
    print("Finally")
    GPIO.cleanup()
    conn.close()
    sock.close()
    
