#Test Run
#Reagan
#2025-05-30

import pygame
import time

from CropData import CROP_DATA

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)

def plant_crop(x,y,crop_type):
    if farming_grid[y][x] == 'empty':
        crop_grown = {
            'type' : crop_type,
            'growth_stage' : 0,
            'growth_timer' : 0,
            'growth_stages': CROP_DATA[crop_type]['growth_stages'],
            'max_stage': CROP_DATA[crop_type]['max_stage'],
            'mature': False
            }
        farming_grid[y][x] = crop_grown

def crop_growth(x,y):
    crop = farming_grid[y][x]
    
    if crop != 'empty':
        print(crop)
    
    if crop == 'empty':
        return False
    
    if crop['mature'] == True:
        return False
    
    if not crop['mature']:
        crop['growth_timer'] += 1
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1        
        
    if crop['growth_stage'] == crop['max_stage']:
        crop['mature'] = True            
    
    return True  

#Colours
BLACK = (0,0,0)
RED = (255,0,0)

#Images
farmingBG = pygame.image.load('FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

#Creating the farming grid's stored data
farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(10):
        farming_row.append('empty')
    farming_grid.append(farming_row)
for item in farming_grid:
    print(item)

grid_hitboxes = []
for y in range(len(farming_grid)):
    grid_hitboxes_row = []
    for x in range(len(farming_grid)):
        grid_hitboxes_row.append([116+75*x-5*y,341+y*40-5*x,72,37])
    grid_hitboxes.append(grid_hitboxes_row)
for item in grid_hitboxes:
    print(item)

#Grid to store whether a crop is growing or not    
growth_grid = []
for y in range(10):
    growth_row = []
    for x in range(10):
        growth_row.append(False)
    growth_grid.append(growth_row)
for item in growth_grid:
    print(item)

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    screen.blit(farmingBG,[0,0])
    
    #Displaying hitboxes
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid)):
            pygame.draw.rect(screen,RED,[116+75*x-5*y,341+y*40-5*x,72,37],1)
    
    #Gets location and checks if mouse is pressed        
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        
        #updating grid to plant crops
        for numY, row in enumerate(grid_hitboxes):
            for numX, rect in enumerate(row):
                if pygame.Rect(rect).collidepoint(mouseX, mouseY):
                    #'carrot' should become a variable for a crop that is selected by the player
                    plant_crop(numX, numY, 'carrot')
    
    #updating planted crops
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            crop_growth(x,y)
                

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
            
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
