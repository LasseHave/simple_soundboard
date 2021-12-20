#!/usr/bin/python3
from os import listdir
import time
import pygame


def playStartSound():
	pygame.mixer.music.load("startup.mp3")
	time.sleep(4)
	pygame.mixer.music.play()

def playSound(key):
	try:
		toPlay = any(item.startswith(key) for item in names)

		toPlay = [filename for filename in names if filename.startswith(key)]
		if pygame.mixer.music.get_busy() == False:
			pygame.mixer.music.load("sounds/" + toPlay[0])
			pygame.mixer.music.play()
	except:
		print("The key " + key + " does not have a sound")



if __name__ == '__main__':
	# Start Up and initial setup
	soundFolderPath = './sounds'
	names = [filename for filename in listdir('sounds')]
	pygame.mixer.init()
	playStartSound()

	import readchar
	pygame.init()

	keyInput = '0'
	# Start Main loop
	print("Ready for input")
	while True:
		keyInput = readchar.readkey()
		print("The key: "+ keyInput + " was pressed")
		playSound(keyInput)

