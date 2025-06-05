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


### VARIABLE PRESETS ###
itemamount = {}
holdingitem = [False, 'empty', 0]
inventory = get_inventory()
invImg = {}
cropimg = {}


### FONTS ###
font = pygame.font.SysFont('Calibri', 16, True, False)
goldfont = pygame.font.SysFont('Calibri', 24, True, False)


### RELOAD HOTBAR IMAGES ###
def reload_hotbar():
    
    screen.fill(BLACK)
    
    # Globalize
    global goldImg, textImg, hotbarBg, invImg, debug, itemamount, goldimg
    
    # Render images and text
    goldtext = goldfont.render('$' + str(get_gold()), True, WHITE)
    screen.blit(goldimg, [20, 20])
    screen.blit(goldtext, [60,25])
    screen.blit(hotbarBg, [400, 760])
    
    # Load item amounts
    for i, item in enumerate(inventory):
        itemamount[i] = str(get_item_info(item))
        
    # Load crop images within loop    
    for i, item in enumerate(inventory):
        
        ## Debug ##
        if debug == False:
            print(item)
            get_item_info(item)
        
        # Render items and amounts
        invImg[i] = screen.blit(cropimg[i], [(404+i*40), 764])
        screen.blit(font.render(itemamount[i], True, BLACK), [406+i*40,766])
        
    reload_done()


### LOAD IMAGES ###

# Load gold image
goldimg = pygame.image.load('images/gold.png')
goldimg = pygame.transform.scale(goldimg, (32, 32))

# Load hotbar image
hotbarBg = pygame.image.load('images/hotbarbg.png')
hotbarSelected = pygame.image.load('images/hotbarSelected.png')

# Load inventory images
for i, item in enumerate(inventory):
    cropimg[i] = pygame.transform.scale(pygame.image.load('crops/'+get_item_image(item)), (32, 32))


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
        
        
        ### RELOADING HOTBAR ###
        if reload_check() == True:
            inventory = get_inventory()
            reload_hotbar()
        
        
        ### CHECK HOVER ###
        hovering = False
        for i, item in enumerate(inventory):
            if invImg[i].collidepoint(pos):
                screen.blit(hotbarSelected, [400 + i * 40, 760])
                screen.blit(cropimg[i], [(404+i*40), 764])
                screen.blit(font.render(itemamount[i], True, BLACK), [406+i*40,766])
                
                if buttonsdown[0]:
                    holdingitem = [True, item, holdingitem[2]+1, i]
                hovering = True
            
        if not hovering:
            reload_hotbar()

        if holdingitem[0]:
            pygame.draw.rect(screen, BLACK, [(402+holdingitem[3]*40), 764, 36,32], 2)
        
        if buttonsdown[0] and holdingitem[2] == 2:
            holdingitem = [False, 'empty', 0]
        

        ### DEBUGGING ###
        if debug:
            print(change_inventory("add", 'tomato', 4))
            print(change_gold('add', 100))            
            print(reload_check())
            print(invImg)            
            print(buttonsdown, pos, arrowKeys)
        
        
        pygame.display.flip()
        clock.tick(fps)
        
pygame.quit()