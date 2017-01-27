#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import pygame

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
 
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
	count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    file = '../mp3/sound.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    
    # Main loop
    while True:
        rctime = rc_time(pin_to_circuit)
        print rctime
	if rctime <= 1000:
		if not pygame.mixer.music.get_busy():
			print "play music"
			pygame.mixer.music.load(file)
			pygame.mixer.music.rewind()
			pygame.mixer.music.play()
	else:
		if pygame.mixer.music.get_busy():
			print "stop music"
			pygame.mixer.music.rewind()
			pygame.mixer.music.stop()

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
