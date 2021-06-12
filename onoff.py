import sys
import time
import RPi.GPIO as GPIO

vin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(vin, GPIO.OUT)

try:
    while True:
        GPIO.output(vin, 1)
        time.sleep(1)
        GPIO.output(vin, 0)
        time.sleep(1) 
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
