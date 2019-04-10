import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

pulse=3

GPIO.setup(pulse,GPIO.IN,pull_up_down=GPIO.PUD_UP)

counter=0
reading=0

def energy_pulse(pulse):
    global counter
    global reading	
    if GPIO.input(pulse)> 0.5 :
        counter +=1
	    reading = counter * 0.3125
        print("energy count is:", reading)

GPIO.add_event_detect(pulse, GPIO.RISING, callback=energy_pulse)

done=False;
while not done:
    try:
        time.sleep(4);
        print("Updating");
    except KeyboardInterrupt:
        print("Program Ended");
        done=True;
GPIO.cleanup()

