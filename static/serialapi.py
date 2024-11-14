import serial

ser =serial.serial('/dev/ttyUSB0')
ser.baudrate = 115200
print(ser.name)
ser.write(b'hello')
ser.close