import pygame
import time
import random
import sys
import subprocess

from gamedata.CropData import CROP_DATA
from Variables import *
from CropGrowth import *
from InventoryManagement import *
from gamedata.FarmingGrid import farming_grid

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise Valley")

### WINDOW ICON ###
pygame_icon = pygame.image.load('images/gameicon.ico')
pygame.display.set_icon(pygame_icon)

### VARIABLE PRESETS ###
itemamount = {}
holdingitem = [False, None, 0]
inventory = get_inventory()
invImg = {}
hotbarimg = {}
counter = 0
clock = pygame.time.Clock()
active = True
shop_open = False
playlist = []
shovel = False
shopHB = {}
shopitems = ['carrot', 'potato', 'tomato', 'wheat', 'blueberry', 'corn', 'pumpkin', 'grape', 'mushroom', 'rgbberry']
hasBeenReleased = 0


### FONTS ###
font = pygame.font.SysFont('Calibri', 18, True, False)
goldfont = pygame.font.SysFont('Calibri', 24, True, False)

### LOAD GAME DATA ###
with open('gamedata/Bag.json', 'r') as bagJson:
    bag = json.load(bagJson)
    
### SAVE GAME DATA ###
def save():
    save_inventory()
    save_gold()    
    with open('gamedata/FarmingGrid.py', 'w') as gridPy:
        gridPy.write("farming_grid = " + repr(farming_grid))
    with open('gamedata/Bag.json', 'w') as bagJson:
        json.dump(bag, bagJson)  



### MUSIC ###

# Choosing music randomly then playing it
songs = ["sfx/1-07. Haggstrom.mp3","sfx/gentle-fields-194622.mp3","sfx/11. Village from Your Past [Ocarina of Time].mp3","sfx/01. Stardew Valley Overture.mp3"]
def play_music():
    song = random.choice(songs)
    nextsong = random.choice(songs)    
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    pygame.mixer.music.queue(nextsong)



### HARVESTING SYSTEM ###
def harvest_crop(x,y):
    crop = farming_grid[y][x]
    if crop == "empty":
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
            crop = "empty"  
            
            farming_grid[y][x] = crop   
            return True
    
    return False


### HITBOX FOR SELLING ###
def sell_hitbox(mouse_pos,button):
    hitbox = pygame.Rect(880,500,320,280)
    if bag != [] and hitbox.collidepoint(mouse_pos) and button[0] and not shop_open:
        return True

### HITBOX FOR SHOP ###
def shop_hitbox(mouse_pos,button):
    hitbox = pygame.draw.rect(screen, BLACK, (900,170,270,280), 5)
    if hitbox.collidepoint(mouse_pos) and button[0]:
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
    global goldImg, goldtext, textImg, hotbarBg, invImg, itemamount, goldimg, hotbarimg, inventory
    
    inventory = get_inventory()
    
    # Render images and text
    goldtext = goldfont.render('$' + str(get_gold()), True, BLACK)
    screen.blit(goldimg, [15, 15])
    screen.blit(goldtext, [55,20])
    screen.blit(hotbarBg, [400, 760])
        
    # Load crop images within loop    
    for i, item in enumerate(inventory):
        itemamount[i] = str(get_item_info(item))
        
        # Render items and amounts
        invImg[i] = screen.blit(hotbarimg[item], [(404+i*40), 764])
        screen.blit(font.render(itemamount[i], True, WHITE), [406+i*40,766])
        
    reload_done()

### SHOP ###
def open_shop():
    # Globalize
    global shopimg, screen, shopHB, pos, buttonsdown, hasBeenReleased, shopitems, shop_open, blurredBG, justOpened
    
    # Draw all images for the shop
    screen.blit(blurredBG,[0,0])
    screen.blit(shopimg,[200,40])
    close = pygame.draw.rect(screen, BLACK, (825, 68, 107, 21), 1)

    # Check if shop was just opened
    if justOpened:
        for i in range(5):
            # Make hitboxes
            shopHB[i] = pygame.draw.rect(screen, BLACK, (250+i*136, 280, 130, 130), 1)
            shopHB[i+5] = pygame.draw.rect(screen, BLACK, (250+i*136, 510, 130, 130), 1)
    
    # Item collision and buying
    for i, hitbox in shopHB.items():
        
        # If hovering
        if hitbox.collidepoint(pos):
            
            # Row height settings
            if i < 5: 
                itemY = 280
                itemN = i
            elif i > 4: 
                itemY = 510
                itemN = i - 5
            
            # Hover background
            pygame.draw.rect(screen, DARKYELLOW, (250+itemN*136, itemY, 130, 130))
            
            # Once clicked, check gold amount then buy, then reload everything
            if buttonsdown[0]:
                pygame.draw.rect(screen, DARKERYELLOW, (250+itemN*136, itemY, 130, 130))
                hasBeenReleased = 1
            elif not buttonsdown[0] and hasBeenReleased == 1:
                if CROP_DATA[shopitems[i]]['seed_cost'] <= gold['gold']:
                    hasBeenReleased = 0
                    change_inventory("add", shopitems[i], 1)
                    change_gold("subtract", CROP_DATA[shopitems[i]]['seed_cost'])
                    reload_hotbar()
    
    # Close button
    if close.collidepoint(pos) and buttonsdown[0]:
        shop_open = False
    
    # Render all crops on top of everything else
    screen.blit(shopcrops,[200,40])
    
    # Reset justOpened value since already opened
    justOpened = False


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
blurredBG = pygame.image.load('images/BlurredBackground.png')
blurredBG = pygame.transform.scale(blurredBG,[1200,800])

# Backpack image
Bagpng = pygame.image.load('images/Bag.png')
Bagpng = pygame.transform.scale(Bagpng,[38,38])

# Load shop images
shopimg = pygame.image.load('images/shop.png')
shopimg = pygame.transform.scale(shopimg, (800, 746))

shopcrops = pygame.image.load('images/shopitems.png')
shopcrops = pygame.transform.scale(shopcrops, (800, 746))

# Load shovel image
shovelimg = pygame.image.load('images/shovel.png')
shovelimg = pygame.transform.scale(shovelimg,[96,96])
shovelRect = pygame.Rect(0,180,96,96)

# Shovel cursor
shovelcursor = pygame.image.load('images/shovelcursor.png')
shovelcursor = pygame.transform.scale(shovelcursor,[16,16])

# Back button
backimg = pygame.image.load('images/back.png')


# Load crop images
for item in CROP_DATA:
    hotbarimg[item] = pygame.transform.scale(pygame.image.load('crops/' + get_item_image(item)), (32, 32))

#Bee
beeR = pygame.image.load('images/beeRight.png')
beeR = pygame.transform.scale(beeR,[32,32])
beeL = pygame.image.load('images/beeLeft.png')
beeL = pygame.transform.scale(beeL,[32,32])

def moving_bee():
    global bee_pos,bee_direction, bee_timer, bee_speed
    
    #Moving bee
    bee_pos[0] += bee_direction[0] * bee_speed[0]
    bee_pos[1] += bee_direction[1] * bee_speed[1]

    #Keeping bee in set boundary
    if bee_pos[0] <= 100: 
        bee_pos[0] = 101
        bee_direction[0] *= -1
    elif bee_pos[0] >= 1100:
        bee_pos[0] = 1099
        bee_direction[0] *= -1
    
    if bee_pos[1] <= 100: 
        bee_pos[1] = 101
        bee_direction[1] *= -1
    elif bee_pos[1] >= 700:
        bee_pos[1] = 699
        bee_direction[1] *= -1
        
    if bee_direction[0] > 0:
        screen.blit(beeR, bee_pos)
    else:
        screen.blit(beeL, bee_pos)

### FARMING GRID HITBOXES ###
grid_hitboxes = []
for y in range(len(farming_grid)):
    grid_hitboxes_row = []
    for x in range(len(farming_grid)):
        grid_hitboxes_row.append([121+75*x-5*y,345+y*40-5*x,70,39])
    grid_hitboxes.append(grid_hitboxes_row)

#Base variables for bee function
bee_speed = [1,1]
bee_timer = 0
bee_direction = [1,1]
bee_pos = [random.randint(200,1000),random.randint(200,600)]

while active:
    
    ### EVENT LISTENER ###
    for event in pygame.event.get():
        ### QUIT LISTENER ###
        if event.type == pygame.QUIT:
            active = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shovelRect.collidepoint(pos) and event.button == 1 and not shop_open:
                if shovel == False:
                    shovel = True
                elif shovel == True:
                    shovel = False
                holdingitem = [False,None,0,None]

    
    ### MOUSE LISTENER ###
    buttonsdown = pygame.mouse.get_pressed()
    
    ### MOUSE POSITION ###
    pos = pygame.mouse.get_pos()
    
    
    ### PLAY MUSIC ###
    if not pygame.mixer.music.get_busy():
        play_music()
        
    
    ### SELL CROPS ###
    if sell_hitbox(pos,buttonsdown):
        sell()
    
    ### SHOP HITBOX ###
    if shop_hitbox(pos,buttonsdown) and not shop_open:
        shop_open = True
    
    ### SHOP OPENED VALUE FOR EFFICIENCY IN THE SHOP LOOP (IF THE SHOP HAS ALREADY BEEN OPENED, DON'T RELOAD CERTAIN THINGS LIKE HITBOXES) ###
    if not shop_open:
        justOpened = True
        
    ### RELOADING HOTBAR ONCE ZEROED ###
    if zeroed_item():
        holdingitem = [False, None, 0, None]
        zeroed_done()
        trigger_reload()
    
    ### RELOADING HOTBAR ###
    if reload_check():
        reload_hotbar()
    
    
    ### RELOAD IMAGES WHICH ARE BEHIND THE SHOP WHEN OPENED ###
    screen.blit(farmingBG,[0,0])
    screen.blit(shovelimg,[0,180])
    backHB = screen.blit(backimg,[1130,20])
    moving_bee()
    ### CHECK SHOP OPEN STATUS, IF TRUE, SHOP IS RENDERED ###
    if shop_open:
        open_shop()    
    
    ### RELOAD IMAGES WHICH ARE ON TOP OF THE SHOP WHEN OPENED ###
    screen.blit(goldimg, [15, 15])
    screen.blit(goldfont.render('$' + str(get_gold()), True, BLACK), [55,20])
    screen.blit(hotbarBg, [400, 760])
        
    screen.blit(Bagpng,[800,760])
    screen.blit(font.render(str(len(bag)),True,WHITE),[810,770])
    
    
    ### BACK BUTTON CHECK PRESS ###
    if backHB.collidepoint(pos) and buttonsdown[0] and not shop_open:
        subprocess.Popen([sys.executable, "Lobby.py"])
        active = False    
    
    #Adds a tick every 5 frames
    tick = 0
    counter += 1
    if counter % 5 == 0:
        tick = 1
        counter = 0
    
    
    #Gets location and checks if mouse is pressed
    if buttonsdown[0] and not shop_open:
        #updating grid to plant crops
        for numY, row in enumerate(grid_hitboxes):
            for numX, rect in enumerate(row):
                if pygame.Rect(rect).collidepoint(pos[0], pos[1]):
                    
                    #Removing crops if shovel is selected
                    if shovel:
                        farming_grid[numY][numX] = "empty"
                        
                    if farming_grid[numY][numX] == "empty":
                        if get_item_info(holdingitem[1]) > 0:
                            #Plants a crop and subtracts from inventory
                            plant_crop(numX, numY, holdingitem[1])
                            change_inventory('subtract',holdingitem[1],1)
                            
                    if farming_grid[numY][numX] != "empty" and holdingitem[1] == None:
                        harvest_crop(numX, numY)
                        
    
    #updating planted crops
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            cropImg = crop_growth(x,y,tick)
            if not shop_open:
                if cropImg != None:
                    screen.blit(cropImg,(grid_hitboxes[y][x][:2]))
    
    

   
    # Load crop images within loop    
    for i, item in enumerate(inventory):            
        # Render items and amounts
        screen.blit(hotbarimg[item], [(404+i*40), 764])
        screen.blit(font.render(itemamount[i], True, WHITE), [406+i*40,766])  
    
    ### CHECK HOVERING AND CLICKING IN HOTBAR ###
    
    # Hover value default
    hovering = False
    
    for i, item in enumerate(inventory):
        
        # Check for hover
        if invImg[i].collidepoint(pos):
            screen.blit(hotbarSelected, [400 + i * 40, 760])
            
            # Redraw item and amount
            invImg[i] = screen.blit(hotbarimg[item], [(404+i*40), 764])
            screen.blit(font.render(itemamount[i], True, WHITE), [406+i*40,766])
            
            # Click checking for if another item has already been selected
            if holdingitem[2] == 2 and buttonsdown[0] and invImg[i].collidepoint(pos) and not invImg[holdingitem[3]].collidepoint(pos):
                holdingitem = [True, inventory[i], 1, i]
                shovel = False
            
            # Click checking (Only apply image once the button has been let go to eliminate issues with timing)
            else:
                shovel = False
                if buttonsdown[0] and holdingitem[2] == 0:
                    holdingitem[2] = 1
                elif holdingitem[2] == 1 and not buttonsdown[0]:
                    holdingitem = [True, inventory[i], 2, i]
                elif buttonsdown[0] and holdingitem[2] == 2:
                    holdingitem[2] = 3
                elif not buttonsdown[0] and holdingitem[2] == 3:
                    holdingitem = [False, None, 0, None]
            
            # Set hover value to true
            hovering = True
    
    # If holding an item, draw square around item
    if holdingitem[0]:
        pygame.draw.rect(screen, BLACK, [(402+holdingitem[3]*40), 764, 36,32], 2)
        
    
    #Making shovel cursor if shovel is selected
    if shovel:
        pygame.mouse.set_visible(False)
        screen.blit(shovelcursor,[pos[0],pos[1]])
    if not shovel:
        pygame.mouse.set_visible(True)
    
    if tick == 1: #Autosaving every tick
        save()
    
            

    pygame.display.flip()
    clock.tick(fps)


pygame.quit()
