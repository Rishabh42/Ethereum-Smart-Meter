import serial
import time

ser=serial.serial(port=ttyUSB0, baudrate=9600,parity=serial.PARITY_ONE,
stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,
timeout=0)

while (1):
	energy=ser.readline()
	print(" current energy value in kwhr: ",energy)
