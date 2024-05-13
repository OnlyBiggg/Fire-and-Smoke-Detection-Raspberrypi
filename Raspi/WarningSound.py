import pygame
pygame.mixer.init()
pygame.mixer.music.load("FIRE_ALARM_SOUND.mp3")

def waringSound(flag):
	if flag == False : 
		pygame.mixer.music.play()
def isBusy():
	return pygame.mixer.music.get_busy()
def offWarningSound():
	pygame.mixer.music.stop()
