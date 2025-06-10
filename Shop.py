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


shopHB = {}
shopitems = ['carrot', 'potato', 'tomato', 'wheat', 'blueberry', 'corn', 'pumpkin', 'grape', 'mushroom', 'rgbberry']
hasBeenReleased = 0



### LOAD IMAGES ###

# Load shop images
shopimg = pygame.image.load('images/shop.png')
shopimg = pygame.transform.scale(shopimg, (800, 746))
shopcrops = pygame.image.load('images/shopitems.png')
shopcrops = pygame.transform.scale(shopcrops, (800, 746))


### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)


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
            
        
        ### MOUSE POSITION ###
        pos = pygame.mouse.get_pos()
        
        screen.blit(shopimg,[200,30])
        
        
        for i in range(5):
            shopHB[i] = pygame.draw.rect(screen, BLACK, (250+i*136, 270, 130, 130), 1)
            shopHB[i+5] = pygame.draw.rect(screen, BLACK, (250+i*136, 500, 130, 130), 1)
            
        for i, hitbox in shopHB.items():
            if hitbox.collidepoint(pos):
                if i < 5: 
                    itemY = 270
                    itemN = i
                elif i > 4: 
                    itemY = 500
                    itemN = i - 5
        
                pygame.draw.rect(screen, DARKYELLOW, (250+itemN*136, itemY, 130, 130))
        
                if buttonsdown[0]:
                    pygame.draw.rect(screen, DARKERYELLOW, (250+itemN*136, itemY, 130, 130))
                    hasBeenReleased = 1
                elif not buttonsdown[0] and hasBeenReleased == 1:
                    hasBeenReleased = 0
                    change_inventory("add", shopitems[i], 1)
                    change_gold("subtract", CROP_DATA[shopitems[i]]['seed_cost'])
                    
                    
        
        screen.blit(shopcrops,[200,30])
        
        print(shopHB)
        
        pygame.display.flip()
        clock.tick(fps)
        
pygame.quit()