import pygame
import time

from gamedata.CropData import CROP_DATA
from Variables import *
from CropGrowth import *
from InventoryManagement import *
from Selling import *

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)



### VARIABLE PRESETS ###
itemamount = {}
holdingitem = [False, None, 0]
bag = []
inventory = get_inventory()
invImg = {}
cropimg = {}


### FONTS ###
font = pygame.font.SysFont('Calibri', 20, True, False)
goldfont = pygame.font.SysFont('Calibri', 24, True, False)



### HARVESTING SYSTEM ###
def harvest_crop(x,y):
    crop = farming_grid[y][x]
    if crop == 'empty':
        return False  
    
    if crop['mature']:
        bag.append(crop['type'])
        
        if crop['renewable']:
            crop['growth_stage'] = crop['max_stage'] - 1
            crop['growth_timer'] = crop['growth_stages'][crop['growth_stage']-1]
            crop['mature'] = False
            farming_grid[y][x] = crop
            return True
            
        else:
            crop = 'empty'  
            
            farming_grid[y][x] = crop   
            return True
    
    return False


### HITBOX FOR SELLING ###
def sell_hitbox(mouse_pos,button):
    hitbox = pygame.Rect(880,500,320,280)
    if bag != [] and hitbox.collidepoint(mouse_pos) and button[0]:
        return True
    
### SELL BAG ###
def sell():
    global bag
    total = 0
    if bag == []:
        return
    for item in bag:
        total += CROP_DATA[item]['sell_price']
    bag = []
    change_gold('add',total)
        

### RELOAD HOTBAR IMAGES ###
def reload_hotbar():
    
    # Globalize
    global goldImg, goldtext, textImg, hotbarBg, invImg, debug, itemamount, goldimg
    
    # Render images and text
    goldtext = goldfont.render('$' + str(get_gold()), True, BLACK)
    screen.blit(goldimg, [20, 20])
    screen.blit(goldtext, [60,25])
    screen.blit(hotbarBg, [400, 760])
    
    # Load item amounts
    for i, item in enumerate(inventory):
        itemamount[i] = str(get_item_info(item))
        
    # Load crop images within loop    
    for i, item in enumerate(inventory):
        
        ## Debug ##
        if debug == True:
            print(item)
            get_item_info(item)
        
        # Render items and amounts
        invImg[i] = screen.blit(cropimg[item], [(404+i*40), 764])
        screen.blit(font.render(itemamount[i], True, BLACK), [406+i*40,766])
        
    reload_done()


### LOAD IMAGES ###

# Load gold image
goldimg = pygame.image.load('images/gold.png')
goldimg = pygame.transform.scale(goldimg, (32, 32))

# Load hotbar image
hotbarBg = pygame.image.load('images/hotbarbg.png')
hotbarSelected = pygame.image.load('images/hotbarSelected.png')

# Background image
farmingBG = pygame.image.load('images/FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

# Backpack image
Bagpng = pygame.image.load('images/Bag.png')
Bagpng = pygame.transform.scale(Bagpng,[38,38])

# Load inventory images
for item in inventory:
    cropimg[item] = pygame.transform.scale(pygame.image.load('crops/'+get_item_image(item)), (32, 32))



### DEFAULT BUTTON SENSING VALUES
buttonsdown = (False, False, False)
arrowKeys = [False, False, False, False]


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
        ### EVENT LISTENER ###
    for event in pygame.event.get():
        ### QUIT LISTENER ###
        if event.type == pygame.QUIT:
            active = False
        
        ### MOUSE LISTENER ###
        buttonsdown = pygame.mouse.get_pressed()
        
        ### MOUSE POSITION ###
        pos = pygame.mouse.get_pos()    

 
    
    ### SELL CROPS ###
    if sell_hitbox(pos,buttonsdown):
        sell()
        
    ### RELOADING HOTBAR ONCE ZEROED ###
    if zeroed_item():
        holdingitem = [False, None, 0, None]
        zeroed_done()
        trigger_reload()
    
    ### RELOADING HOTBAR ###
    if reload_check():
        inventory = get_inventory()
        reload_hotbar()
    
    
    ### RELOAD IMAGES ###
    screen.blit(farmingBG,[0,0])
    screen.blit(goldimg, [20, 20])
    screen.blit(goldtext, [60,25])
    screen.blit(Bagpng,[800,760])
    screen.blit(font.render(str(len(bag)),True,WHITE),[808,770])    
    
    
    ### CHECK HOVERING AND CLICKING IN HOTBAR ###
    
    # Hover value default
    hovering = False
    
    for i, item in enumerate(inventory):
        
        # Check for hover
        if invImg[i].collidepoint(pos):
            
            # Reload hotbar background and item selected image
            screen.blit(hotbarBg, [400, 760])
            screen.blit(hotbarSelected, [400 + i * 40, 760])
            
            # Redraw all items and values
            for i1, item in enumerate(inventory):
                invImg[i1] = screen.blit(cropimg[item], [(404+i1*40), 764])
                screen.blit(font.render(itemamount[i1], True, BLACK), [406+i1*40,766])
            
            # Click checking for if another item has already been selected
            if holdingitem[2] == 2 and buttonsdown[0] and invImg[i].collidepoint(pos) and not invImg[holdingitem[3]].collidepoint(pos):
                holdingitem = [True, get_inventory()[i], 1, i]
                
            # Click checking (Only apply image once the button has been let go to eliminate issues with timing
            else:
                if buttonsdown[0] and holdingitem[2] == 0:
                    holdingitem[2] = 1
                elif holdingitem[2] == 1 and not buttonsdown[0]:
                    holdingitem = [True, get_inventory()[i], 2, i]
                elif buttonsdown[0] and holdingitem[2] == 2:
                    holdingitem[2] = 3
                elif not buttonsdown[0] and holdingitem[2] == 3:
                    holdingitem = [False, None, 0, None]
            
            # Set hover value to true
            hovering = True
    
    # If hover value is false, reload the hotbar
    if not hovering:
        reload_hotbar()

    # If holding an item, draw square around item
    if holdingitem[0]:
        pygame.draw.rect(screen, BLACK, [(402+holdingitem[3]*40), 764, 36,32], 2)
        
    
    
    #Adds a tick every 5 frames
    tick = 0
    counter += 1
    if counter % 5 == 0:
        tick = 1
        counter = 0
        
        
        
        
    
    
    #Gets location and checks if mouse is pressed        
    if buttonsdown[0]:
        #updating grid to plant crops
        for numY, row in enumerate(grid_hitboxes):
            for numX, rect in enumerate(row):
                if pygame.Rect(rect).collidepoint(pos[0], pos[1]):
                    if farming_grid[numY][numX] == 'empty':
                        if get_item_info(holdingitem[1]) > 0:
                            #Plants a crop and subtracts from inventory
                            plant_crop(numX, numY, holdingitem[1])
                            change_inventory('subtract',holdingitem[1],1)
                    if farming_grid[numY][numX] != 'empty' and holdingitem[1] == None:
                        harvest_crop(numX, numY)
    
    #updating planted crops
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            cropImg = crop_growth(x,y,tick)
            if cropImg != False:
                screen.blit(cropImg,(grid_hitboxes[y][x][:2]))
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()