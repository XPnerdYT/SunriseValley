import pygame
import random
import math
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


### SET FONT ###
font = pygame.font.SysFont('Calibri', 20, True, False)

### LOAD IMAGES ###
background = pygame.image.load('images/background.png')
play = pygame.image.load('images/play.png')
instructions = pygame.image.load('images/instructions.png')
quit = pygame.image.load('images/quit.png')

hplay = pygame.image.load('images/hplay.png')
hinstructions = pygame.image.load('images/hinstructions.png')
hquit = pygame.image.load('images/hquit.png')

cowpng = pygame.image.load('images/cow.png')
cowpng = pygame.transform.scale(cowpng,[112,72])

###SFX###
moo1 = "sfx/cow-1-352653.mp3"
moo2 = "sfx/cow-2-352654.mp3"
moo3 = "sfx/cow-3-352655.mp3"
sfxList = [moo1,moo2,moo3]

###Moving Cow###
cowx, cowy = 100, 100
speed = 2
up, down, left, right = False, True, False, True
def distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

### VELOCITY FOR COW ###
def speed_change(distance,speed):
    if distance < 100 and speed < 8:
        speed += 0.3
        if speed > 8:
            speed = 8
    elif distance < 200 and speed < 4:
        speed += 0.2
        if speed > 4:
            speed = 4
    elif distance < 400 and speed < 3:
        speed += 0.1
        if speed > 3:
            speed = 3
    elif distance > 400 and speed > 2:
        speed -= 0.5
        if speed < 2:
            speed = 2
        
    return speed


### MOVE THE COW AND COLLISIONS ###
def moving_cow(speed):
    global left, right, up, down, cowx, cowy, cow_rect
    cow_rect = pygame.Rect(cowx, cowy, 112, 72)
    screen.blit(cowpng,[cowx,cowy])
    if right:
        cowx += speed
    if left:
        cowx -= speed
    if down:
        cowy += speed
    if up:
        cowy -= speed
    if cowx + 112 >= 1200:
        left = True
        right = False
    if cowx <= 0:
        left = False
        right = True
    if cowy <= 0:
        down = True
        up = False
    if cowy + 72 >= 800:
        down = False
        up = True


### EASTER EGG YOU WEREN'T SUPPOSED TO FIND ###
def cow_moo():
    moo = random.choice(sfxList)
    pygame.mixer.music.load(moo)
    pygame.mixer.music.play()

### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]
numKeys = [False, False, False]
enterKey = False

### CLOCK TICK SETTING ###
clock = pygame.time.Clock()


### GAME LOOP ###
while active:
    ### MOUSE POSITION ###
    pos = pygame.mouse.get_pos()
    
    screen.blit(background, [0, 0])
    
    dist = round(distance(pos[0],pos[1],cowx,cowy))
    speed = speed_change(dist,speed)
    moving_cow(speed)
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
       
        
    ### LOWER BUTTONS ###    
    if playHb.collidepoint(pos) or numKeys[0]:
        screen.blit(hplay, [350, 625])
        if buttonsdown[0] or enterKey:
            subprocess.Popen([sys.executable, "FarmingGame.py"])
            active = False
    elif instructionsHb.collidepoint(pos) or numKeys[1]:
        screen.blit(hinstructions, [540, 625])
        if buttonsdown[0] or enterKey:
            subprocess.Popen([sys.executable, "Instructions.py"])
            active = False            
    elif quitHb.collidepoint(pos) or numKeys[2]:
        screen.blit(hquit, [730, 625]) 
        if buttonsdown[0] or enterKey:
            active = False
    
    ### EASTER EGG YOU WEREN'T SUPPOSED TO SEE ###
    elif cow_rect.collidepoint(pos) and buttonsdown[0]:
        if not pygame.mixer.music.get_busy():
            cow_moo()
        
        
    pygame.display.flip()
    clock.tick(fps)
        
        
pygame.quit()