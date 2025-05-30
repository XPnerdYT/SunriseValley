import pygame
import random
from Variables import *

import sys
import subprocess


### WINDOW CONFIGURATION ###
active = True
pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Exercise Set #5")


### SET FONT ###
font = pygame.font.SysFont('Calibri', 20, True, False)


### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]
numKeys = [False, False, False]



### CLOCK TICK SETTING ###
clock = pygame.time.Clock()


### LOAD IMAGES ###
background = pygame.image.load('images/background.png')
play = pygame.image.load('images/play.png')
instructions = pygame.image.load('images/instructions.png')
quit = pygame.image.load('images/quit.png')

hplay = pygame.image.load('images/hplay.png')
hinstructions = pygame.image.load('images/hinstructions.png')
hquit = pygame.image.load('images/hquit.png')



### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]
enterKey = False

### CLOCK TICK SETTING ###
clock = pygame.time.Clock()


### GAME LOOP ###
while active:
    screen.blit(background, [0, 0])
    playHb = screen.blit(play, [350, 625])
    instructionsHb = screen.blit(instructions, [540, 625])
    quitHb = screen.blit(quit, [730, 625])    
    
    
    ### EVENT LISTENER ###
    for event in pygame.event.get():
        ### QUIT LISTENER ###
        if event.type == pygame.QUIT:
            active = False
        
        
        ### MOUSE LISTENER ###
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttonsdown = pygame.mouse.get_pressed()
        # Every time a mouse button is lifted, buttonsdown variable is updated 
        # to account for the lifted button
        if event.type == pygame.MOUSEBUTTONUP:
            buttonsdown = pygame.mouse.get_pressed()
            
        
        ### ARROW KEYS LISTENER ###
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: arrowKeys[0] = True
            if event.key == pygame.K_DOWN: arrowKeys[1] = True
            if event.key == pygame.K_LEFT: arrowKeys[2] = True
            if event.key == pygame.K_RIGHT: arrowKeys[3] = True
            if event.key == pygame.K_1: numKeys[0] = True
            if event.key == pygame.K_2: numKeys[1] = True
            if event.key == pygame.K_3: numKeys[2] = True
            if event.key == pygame.K_RETURN: enterKey = True
        # Every time a arrow key button is lifted, arrowKeys list is updated
        # to account for the lifted key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: arrowKeys[0] = False
            if event.key == pygame.K_DOWN: arrowKeys[1] = False
            if event.key == pygame.K_LEFT: arrowKeys[2] = False
            if event.key == pygame.K_RIGHT: arrowKeys[3] = False
            if event.key == pygame.K_1: numKeys[0] = False
            if event.key == pygame.K_2: numKeys[1] = False
            if event.key == pygame.K_3: numKeys[2] = False
            if event.key == pygame.K_RETURN: enterKey = False
        
            
            
        ### MOUSE POSITION ###
        pos = pygame.mouse.get_pos()
        
        
        ### LOWER BUTTONS ###
        
        if playHb.collidepoint(pos) or numKeys[0]:
            screen.blit(hplay, [350, 625])
            if buttonsdown[0] or enterKey:
                subprocess.Popen([sys.executable, "FarmingGame.py"])
                active = False
        elif instructionsHb.collidepoint(pos) or numKeys[1]:
            screen.blit(hinstructions, [540, 625])
            if buttonsdown[0] or enterKey:
                pass
        elif quitHb.collidepoint(pos) or numKeys[2]:
            screen.blit(hquit, [730, 625]) 
            if buttonsdown[0] or enterKey:
                active = False
        
        
        ### DEBUGGING ###
        if debug: print(buttonsdown, pos, arrowKeys, numKeys, enterKey)
        
        pygame.display.flip()
        clock.tick(30)
        
        
pygame.quit()