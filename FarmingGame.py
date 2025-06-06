import pygame
import time

from gamedata.CropData import CROP_DATA
from Variables import *
from CropGrowth import *
from InventoryManagement import *

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)







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




#Images
farmingBG = pygame.image.load('images/FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

grid_hitboxes = []
for y in range(len(farming_grid)):
    grid_hitboxes_row = []
    for x in range(len(farming_grid)):
        grid_hitboxes_row.append([121+75*x-5*y,345+y*40-5*x,70,39])
    grid_hitboxes.append(grid_hitboxes_row)

counter = 0
clock = pygame.time.Clock()
active = True


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
    


    
    
    screen.blit(farmingBG,[0,0])
    
    
    ### RELOADING HOTBAR ###
    if reload_check() == True:
        inventory = get_inventory()
        reload_hotbar()
    
    
    ### CHECK HOVER ###
    hovering = False
    for i, item in enumerate(inventory):
        if invImg[i].collidepoint(pos):
            screen.blit(hotbarBg, [400, 760])
            screen.blit(hotbarSelected, [400 + i * 40, 760])

            for i1, item in enumerate(inventory):
                invImg[i1] = screen.blit(cropimg[i1], [(404+i1*40), 764])
                screen.blit(font.render(itemamount[i1], True, BLACK), [406+i1*40,766])

            hovering = True

            # Move click handling into the event loop
            for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if event.button == 1 and invImg[i].collidepoint(event.pos):
                    holdingitem = [True, item, 1, i]
    if not hovering:
        reload_hotbar()

    if holdingitem[0]:
        pygame.draw.rect(screen, BLACK, [(402+holdingitem[3]*40), 764, 36,32], 2)
    
    if buttonsdown[0] and holdingitem[2] == 2:
        holdingitem = [False, 'empty', 0]    

        
    
    #Add a feature where player selects crops, for now we can just change this variable to test different crops
    selected = 'blueberry'
    
    #Adds a tick every 5 frames
    tick = 0
    counter += 1
    if counter % 5 == 0:
        tick = 1
        counter = 0
        
        
        
        
    
    
    #Gets location and checks if mouse is pressed        
    if pygame.mouse.get_pressed()[0]:
        
        
        #updating grid to plant crops
        for numY, row in enumerate(grid_hitboxes):
            for numX, rect in enumerate(row):
                if pygame.Rect(rect).collidepoint(pos[0], pos[1]):
                    if farming_grid[numY][numX] == 'empty':
                        plant_crop(numX, numY, selected)
                    else:
                        harvest_crop(numX, numY)
    
    #updating planted crops
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            cropImg = crop_growth(x,y,tick)
            if cropImg != False:
                screen.blit(cropImg,(grid_hitboxes[y][x][:2]))
                       
            
    pygame.display.flip()
    clock.tick(fps)
    