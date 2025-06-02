import pygame
from InventoryManagement import *
from gamedata.CropData import CROP_DATA
from Variables import *


pygame_icon = pygame.image.load('images/gameicon.ico')
pygame.display.set_icon(pygame_icon)




### WINDOW CONFIGURATION ###
active = True
pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise Valley")



font = pygame.font.SysFont('Calibri', 16, True, False)
goldfont = pygame.font.SysFont('Calibri', 24, True, False)




### LOAD IMAGES ###

# Load gold info
goldimg = pygame.image.load('images/gold.png')
goldimg = pygame.transform.scale(goldimg, (32, 32))
screen.blit(goldimg, [20, 20])
# ----
textImg = goldfont.render('$' + str(get_gold()), True, WHITE)
screen.blit(textImg, [60,25])

# Load hotbar image
hotbarBg = pygame.image.load('images/hotbarbg.png')
screen.blit(hotbarBg, [400, 760])

# Load crop images within loop
i = 0
for item in get_inventory():
    ## Debug ##
    if debug:
        print(item)
        get_item_info(item)
    
    cropimg = pygame.image.load('crops/'+get_item_image(item))
    cropimg = pygame.transform.scale(cropimg, (32, 32))
    screen.blit(cropimg, [(404+i*40), 764])
    
    textImg = font.render(str(get_item_info(item)), True, BLACK)
    screen.blit(textImg, [406+i*40,766])
    
    i += 1


### SET FONT ###
font = pygame.font.SysFont('Calibri', 20, True, False)


### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]


### CLOCK TICK SETTING ###
clock = pygame.time.Clock()

pygame.display.flip()


### GAME LOOP ###
while active:
    
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
        # Every time a arrow key button is lifted, arrowKeys list is updated
        # to account for the lifted key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: arrowKeys[0] = False
            if event.key == pygame.K_DOWN: arrowKeys[1] = False
            if event.key == pygame.K_LEFT: arrowKeys[2] = False
            if event.key == pygame.K_RIGHT: arrowKeys[3] = False
        
        
        ### MOUSE POSITION ###
        pos = pygame.mouse.get_pos()
        
        
        ### DEBUGGING ###
        if debug: 
            print(buttonsdown, pos, arrowKeys)
        
        pygame.display.flip()
        clock.tick(fps)
        
pygame.quit()