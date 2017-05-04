import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
import os
import random
import subprocess

pygame.init()
WIDTH = 1280
HEIGHT = 1024
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 32)


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

emulator_on = False

def get_pid(name):
	return subprocess.check_output(["pidof",name])

def exitEmulator():
	retroarch_pid = get_pid("retroarch")
	retroarch_pid = retroarch_pid.decode('ascii')
	os.system('kill -QUIT ' + retroarch_pid)

def flipImage(flipcount):
	for i in range(flipcount):
		img = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
		windowSurface.blit(img, (0, 0)) #Replace (0, 0) with desired coordinates
		pygame.display.flip()
		time.sleep(0.7)

def randomGame():
	retrolaunch_game = random.choice(os.listdir("/home/pi/RetroPie/roms/nes/"))
	retrolaunch = '/opt/retropie/emulators/retroarch/bin/retroarch', '-L', '/opt/retropie/libretrocores/lr-nestopia/nestopia_libretro.so', '/home/pi/RetroPie/roms/nes/' + retrolaunch_game, '--config=/opt/retropie/configs/all/retroarch.cfg'
	subprocess.Popen(retrolaunch, stdin=None, stdout=None, stderr=None)



while True:
	input_state = GPIO.input(18)
	if input_state == False:
		if emulator_on == True:
			exitEmulator()
			emulator_on = False
		else:
			flipImage(random.randint(6,20))
			emulator_on = True
			randomGame()
