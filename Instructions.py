import pygame
import sys
import subprocess

from Variables import *


### WINDOW CONFIGURATION ###
active = True
pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise Valley")

### WINDOW ICON ###
pygame_icon = pygame.image.load('images/gameicon.ico')
pygame.display.set_icon(pygame_icon)


### LOAD IMAGES ###

# Load tutorial image
tutorialimg = pygame.image.load('images/tutorial.png')
backimg = pygame.image.load('images/back.png')


### CLOCK TICK SETTING ###
clock = pygame.time.Clock()

### GAME LOOP ###
while active:
    
    ### EVENT LISTENER ###
    for event in pygame.event.get():
        ### QUIT LISTENER ###
        if event.type == pygame.QUIT:
            active = False
        
    ### MOUSE LISTENER ###
    buttonsdown = pygame.mouse.get_pressed()
    
    ### MOUSE POSITION ###
    pos = pygame.mouse.get_pos()
    
    ### RENDER IMAGES ###
    screen.blit(tutorialimg,[0,0])
    backHB = screen.blit(backimg,[1130,20])
    
    ### BACK BUTTON CHECK PRESS ###
    if backHB.collidepoint(pos) and buttonsdown[0]:
        subprocess.Popen([sys.executable, "Lobby.py"])
        active = False
    
    pygame.display.flip()
    clock.tick(fps)
        
pygame.quit()