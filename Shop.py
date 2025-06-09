import pygame
from InventoryManagement import *
from Variables import *
from gamedata.CropData import CROP_DATA


### WINDOW CONFIGURATION ###
active = True
pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise Valley")

pygame_icon = pygame.image.load('images/gameicon.ico')
pygame.display.set_icon(pygame_icon)


shopHB0 = {}
shopHB1 = {}



### LOAD IMAGES ###

# Load gold image
shopimg = pygame.image.load('images/shop.png')
shopimg = pygame.transform.scale(shopimg, (800, 746))
shopcrops = pygame.image.load('images/shopitems.png')
shopcrops = pygame.transform.scale(shopcrops, (800, 746))


### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]


### CLOCK TICK SETTING ###
clock = pygame.time.Clock()

pygame.display.flip()

### GAME LOOP ###
while active:
    
    screen.fill(WHITE)
    
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
        
        screen.blit(shopimg,[200,30])
        
        
        for i in range(5):
            shopHB0[i] = pygame.draw.rect(screen, BLACK, (250+i*136, 270, 130, 130), 1)
            shopHB1[i] = pygame.draw.rect(screen, BLACK, (250+i*136, 500, 130, 130), 1)
            
        for i, hitbox in enumerate(shopHB1):
            if shopHB1[hitbox].collidepoint(pos):
                pygame.draw.rect(screen, DARKYELLOW, (250+i*136, 270, 130, 130))
                
        
        screen.blit(shopcrops,[200,30])
        
        print(shopHB0, shopHB1)
        
        pygame.display.flip()
        clock.tick(fps)
        
pygame.quit()