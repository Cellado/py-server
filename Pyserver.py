import socket

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

host = ''
port = 5000
buffer_size = 1024

sock = socket.socket(socket.AFINET, socket.SOCK_STREAM)
sock.bind((host, port))
s.listen(1)
print(f'Server started on port {port}')

try:
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            command = data.decode('utf-8').strip().lower()
            if command == 'on':
                GPIO.output(Motor1F, GPIO.HIGH)
                GPIO.output(Motor2F, GPIO.HIGH)
                conn.sendall(b'Motor1F HIGH\n')
                conn.sendall(b'Motor2F HIGH\n')
            elif command == 'off':
                GPIO.output(Motor1F, GPIO.LOW)
                GPIO.output(Motor2F, GPIO.LOW)
                conn.sendall(b'Motor1F LOW\n')
                conn.sendall(b'Motor2F LOW\n')
            else:
                conn.sendall(b'Invalid command\n')
finally:
    GPIO.cleanup()
    conn.close()
    s.close()
    
