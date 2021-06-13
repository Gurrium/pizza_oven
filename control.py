#! /usr/bin/python3

import RPi.GPIO as GPIO
import adafruit_max31855
import board
import busio
import digitalio
import sys
import time

print("setup: start")
HEATER_PIN = 2
GPIO.setup(HEATER_PIN, GPIO.OUT)

spi = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
cs = digitalio.DigitalInOut(board.D5)
THERMOMETER = adafruit_max31855.MAX31855(spi, cs)

def cleanup():
    print("cleanup: start")
    GPIO.cleanup()

def on():
    print("heater: on")
    GPIO.output(HEATER_PIN, 1)

def off():
    print("heater: off")
    GPIO.output(HEATER_PIN, 0)

def get_temperature():
    tmp = THERMOMETER.temperature
    print(f'temperature: {tmp}')
    return tmp

def main():
    target_temperature = float(sys.argv[1])
    print(f'target temperature: {target_temperature}')
    while True:
        current_temperature = get_temperature()
        if current_temperature > target_temperature:
            off()
        else:
            on()
        time.sleep(2)

try:
    main()
except KeyboardInterrupt:
    cleanup()
    sys.exit(0)
