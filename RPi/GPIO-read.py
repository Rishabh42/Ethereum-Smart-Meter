import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pulse=11

GPIO.setup(pulse,GPIO.IN,pull_up_down=GPIO.PUD_UP)

counter=0

def energy_pulse(pulse):
        global counter
        if GPIO.input(pulse)> 0.5 :
                counter +=1

GPIO.add_event_detect(pulse, GPIO.rising, callback=energy_pulse)

for x in range (0,1000):
	print("energy count is:", counter)
	time.sleep(.1)

GPIO.cleanup()
