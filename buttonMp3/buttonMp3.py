#!/usr/bin/env python3
########################################################################
# Filename    : ButtonLED.py
# Description : Controlling an led by button.
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import pygame as pg

ledPin = 11    # define the ledPin
buttonPin = 12    # define the buttonPin

def setup():
	print ('Program is starting...')
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set buttonPin's mode is input, and pull up to high level(3.3V)

def loop():
	while True:
		if GPIO.input(buttonPin)==GPIO.LOW:
			GPIO.output(ledPin,GPIO.HIGH)
			print ('led on ...')
			
			# pick a MP3 music file you have in the working folder
                        # otherwise give the full file path
                        # (try other sound file formats too)
                        music_file = "chewie.mp3"
                        # optional volume 0 to 1.0
                        volume = 0.2
                        play_music(music_file, volume)
			
		else :
			GPIO.output(ledPin,GPIO.LOW)
			

def destroy():
	GPIO.output(ledPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

def play_music(music_file, volume=0.8):
   
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


