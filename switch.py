import RPi.GPIO as GPIO
import time
import webbrowser
import pygame
from pygame.locals import *
import os
import random
import subprocess
from subprocess import check_output

#pygame.init()
WIDTH = 1280
HEIGHT = 1024
#windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 32)


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

emulator_on = False

def get_pid(name):
	return check_output(["pidof",name])

def exitEmulator():
#	print('exitEmulator')
	retroarch_pid = get_pid("retroarch")
#	emulation_pid = get_pid("emulationstatio")
	retroarch_pid = retroarch_pid.decode('ascii')
#	emulation_pid = emulation_pid.decode('ascii')
#	print('kill -QUIT ' + retroarch_pid)
	os.system('kill -QUIT ' +retroarch_pid)
	#print('kill -QUIT ' + emulation_pid)

def flipImage(flipcount):
	for i in range(flipcount):
		img = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
		windowSurface.blit(img, (0, 0)) #Replace (0, 0) with desired coordinates
		pygame.display.flip()
		time.sleep(0.7)


while True:
	input_state = GPIO.input(18)
	if input_state == False:
		if emulator_on == True:
			exitEmulator()
#			print('Exit Emulator')
			emulator_on = False
		else:
			pygame.init()		#possible move to top
			windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME, 32)
			img1 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img2 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img3 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img4 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img5 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img6 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img7 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			img8 = pygame.image.load("mario/" + random.choice(os.listdir("/home/pi/mario/")))
			flipImage(2)
#			print('Button Pressed')
#			windowSurface.blit(img1, (0, 0)) #Replace (0, 0) with desired coordinates
#			pygame.display.flip()
#			time.sleep(0.7)
			windowSurface.blit(img2, (0, 0)) #Replace (0, 0) with desired coordinates
			pygame.display.flip()
			time.sleep(0.7)
			windowSurface.blit(img3, (0, 0)) #Replace (0, 0) with desired coordinates
			pygame.display.flip()
			pygame.quit()		#possible not necessary
			emulator_on = True
#			print('Launch Emulator')
			retrolaunch = '/opt/retropie/emulators/retroarch/bin/retroarch', '-L', '/opt/retropie/libretrocores/lr-nestopia/nestopia_libretro.so', '/home/pi/RetroPie/roms/nes/Battletoads.nes', '--config=/opt/retropie/configs/all/retroarch.cfg'
#			os.system('/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-nestopia/nestopia_libretro.so /home/pi/RetroPie/roms/nes/Battletoads.nes --config /opt/retropie/configs/all/retroarch.cfg')
			subprocess.Popen(retrolaunch, stdin=None, stdout=None, stderr=None)

