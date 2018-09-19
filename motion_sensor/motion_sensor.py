import RPi.GPIO as GPIO
import pygame as pg
import time
import os
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(11, GPIO.OUT)         #LED output pin

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

try:
	while True:
		i=GPIO.input(12)
		if i==0:                 #When output from motion sensor is LOW
			#print "No intruders",i
			GPIO.output(11, 0)  #Turn OFF LED
			time.sleep(0.1)
		elif i==1:               #When output from motion sensor is HIGH
			#print("Intruder detected",i)
			GPIO.output(11, 1)  #Turn ON LED
			# pick a MP3 music file you have in the working folder
			# otherwise give the full file path
			# (try other sound file formats too)
			path = "../mp3List/"
			#print(os.path.dirname(path))
			#print(os.path.basename(path))
			files =  os.listdir(path)
			#print(files)
			#print(random.choice(files))
			randomSong = random.choice(files)
			music_file = path + randomSong
			# optional volume 0 to 1.0
			volume = 0.2
			play_music(music_file, volume)
			time.sleep(0.1)
except: # run on exit
	GPIO.cleanup()         # clean up
	print("All cleaned up.")
